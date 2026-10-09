# zotero_handsfree.ps1 - import English_Zotero_library.json into the local
# Zotero (connector + local API on 127.0.0.1:23119, the same stack a Zotero
# MCP wraps) and rewrite ITEM uris in projects\English.docx to real itemKeys.
# ASCII-only (Windows PowerShell 5.1). Exit 0 = all 54 mapped + relinked.

$ErrorActionPreference = 'Continue'
Set-Location (Join-Path $PSScriptRoot '..')

$ZoteroBase = 'http://127.0.0.1:23119'
$LibRel = 'projects\English_Zotero_library.json'
$DocRel = 'projects\English.docx'
$OutRel = 'results\status\zotero_handsfree.json'
$MapRel = 'results\status\zotero_uri_map.json'

function Write-Log($msg) { Write-Output $msg }

function Save-Status($obj) {
    $dir = Split-Path -Parent $OutRel
    if (-not (Test-Path -LiteralPath $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    $okStr = 'false'
    if ($obj.ok) { $okStr = 'true' }
    $lines = New-Object System.Collections.Generic.List[string]
    [void]$lines.Add('{')
    [void]$lines.Add('  "ok": ' + $okStr + ',')
    [void]$lines.Add('  "zotero_ping": ' + $(if ($obj.zotero_ping) { 'true' } else { 'false' }) + ',')
    [void]$lines.Add('  "local_api": ' + $(if ($obj.local_api) { 'true' } else { 'false' }) + ',')
    [void]$lines.Add('  "imported": ' + [int]$obj.imported + ',')
    [void]$lines.Add('  "already": ' + [int]$obj.already + ',')
    [void]$lines.Add('  "mapped": ' + [int]$obj.mapped + ',')
    [void]$lines.Add('  "relinked_uris": ' + [int]$obj.relinked_uris + ',')
    $wr = [string]$obj.word_refresh
    $wr = $wr.Replace('\', '\\').Replace('"', '\"')
    [void]$lines.Add('  "word_refresh": "' + $wr + '",')
    $err = [string]$obj.error
    $err = $err.Replace('\', '\\').Replace('"', '\"')
    [void]$lines.Add('  "error": "' + $err + '"')
    [void]$lines.Add('}')
    $utf8 = New-Object System.Text.UTF8Encoding $false
    [IO.File]::WriteAllLines((Join-Path (Get-Location) $OutRel), $lines.ToArray(), $utf8)
}

function Invoke-LocalHttp {
    param(
        [string]$Method,
        [string]$Url,
        [string]$Body,
        [hashtable]$Headers,
        [int]$TimeoutSec = 120
    )
    $req = [System.Net.HttpWebRequest]::Create($Url)
    $req.Method = $Method
    $req.Timeout = $TimeoutSec * 1000
    $req.ReadWriteTimeout = $TimeoutSec * 1000
    $req.Proxy = $null
    $req.KeepAlive = $false
    $req.AutomaticDecompression = [System.Net.DecompressionMethods]::GZip -bor [System.Net.DecompressionMethods]::Deflate
    if ($Headers) {
        foreach ($k in $Headers.Keys) {
            $lk = ([string]$k).ToLowerInvariant()
            if ($lk -eq 'content-type') { $req.ContentType = [string]$Headers[$k] }
            elseif ($lk -eq 'accept') { $req.Accept = [string]$Headers[$k] }
            else { [void]$req.Headers.Add([string]$k, [string]$Headers[$k]) }
        }
    }
    if ($null -ne $Body -and $Method -ne 'GET' -and $Method -ne 'HEAD') {
        $bytes = [Text.Encoding]::UTF8.GetBytes($Body)
        $req.ContentLength = $bytes.Length
        $st = $req.GetRequestStream()
        $st.Write($bytes, 0, $bytes.Length)
        $st.Close()
    }
    $resp = $null
    try {
        $resp = $req.GetResponse()
    } catch [System.Net.WebException] {
        $resp = $_.Exception.Response
        if (-not $resp) { throw }
    }
    $code = [int]$resp.StatusCode
    $sr = New-Object IO.StreamReader($resp.GetResponseStream())
    $text = $sr.ReadToEnd()
    $sr.Close()
    $resp.Close()
    return @{ Status = $code; Body = $text }
}

function Normalize-Doi([string]$raw) {
    if (-not $raw) { return '' }
    $d = $raw.Trim()
    $d = $d -replace '^https?://(dx\.)?doi\.org/', ''
    $d = $d -replace '^doi:\s*', ''
    return $d.ToLowerInvariant().Trim()
}

function Convert-CslToConnectorItem($csl) {
    $ck = [string]$csl.'citation-key'
    if (-not $ck) { $ck = [string]$csl.id }
    $creators = New-Object System.Collections.Generic.List[object]
    foreach ($a in @($csl.author)) {
        $creators.Add(@{
            creatorType = 'author'
            firstName   = [string]$a.given
            lastName    = [string]$a.family
        })
    }
    $date = ''
    if ($csl.issued -and $csl.issued.'date-parts') {
        $dp0 = @($csl.issued.'date-parts')
        if ($dp0.Count -gt 0) {
            $parts = @($dp0[0])
            $date = ($parts | ForEach-Object { [string]$_ }) -join '-'
        }
    }
    $item = @{
        itemType          = 'journalArticle'
        title             = [string]$csl.title
        creators          = $creators
        date              = $date
        publicationTitle  = [string]$csl.'container-title'
        volume            = [string]$csl.volume
        issue             = [string]$csl.issue
        pages             = [string]$csl.page
        DOI               = [string]$csl.DOI
        extra             = ('Citation Key: ' + $ck)
    }
    return $item
}

function Get-ItemUri($it) {
    if ($null -eq $it) { return '' }
    try {
        $href = [string]$it.links.alternate.href
        if ($href -match '^https?://zotero\.org/') { return $href }
    } catch {}
    $key = [string]$it.key
    if (-not $key) {
        try { $key = [string]$it.data.key } catch { $key = '' }
    }
    if (-not $key) { return '' }
    $libId = ''
    try { $libId = [string]$it.library.id } catch { $libId = '' }
    if ($libId -and $libId -ne '0' -and $libId -ne 'local') {
        return ('http://zotero.org/users/' + $libId + '/items/' + $key)
    }
    return ('http://zotero.org/users/local/items/' + $key)
}

function Find-ZoteroItemByDoi([string]$doi) {
    $nd = Normalize-Doi $doi
    if (-not $nd) { return $null }
    $q = [uri]::EscapeDataString($doi)
    $url = $ZoteroBase + '/api/users/0/items?q=' + $q + '&qmode=everything&itemType=journalArticle&limit=25'
    $headers = @{
        'Zotero-API-Version' = '3'
        'Accept'             = 'application/json'
    }
    $r = Invoke-LocalHttp -Method GET -Url $url -Headers $headers -TimeoutSec 30
    if ($r.Status -lt 200 -or $r.Status -ge 300) { return $null }
    if (-not $r.Body) { return $null }
    $arr = $r.Body | ConvertFrom-Json
    foreach ($it in @($arr)) {
        $got = ''
        try { $got = Normalize-Doi ([string]$it.data.DOI) } catch { $got = '' }
        if ($got -and $got -eq $nd) { return $it }
    }
    return $null
}

function New-DocxFromFolder([string]$folder, [string]$outPath) {
    if (Test-Path -LiteralPath $outPath) { Remove-Item -LiteralPath $outPath -Force }
    $zip = [System.IO.Compression.ZipFile]::Open($outPath, 'Create')
    $base = (Resolve-Path -LiteralPath $folder).Path.TrimEnd('\')
    Get-ChildItem -LiteralPath $folder -Recurse -File | ForEach-Object {
        $full = $_.FullName
        $rel = $full.Substring($base.Length + 1).Replace('\', '/')
        [void][System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(
            $zip, $full, $rel, [System.IO.Compression.CompressionLevel]::Optimal)
    }
    $zip.Dispose()
}

function Test-FileLocked([string]$path) {
    try {
        $fs = [IO.File]::Open($path, 'Open', 'ReadWrite', 'None')
        $fs.Close()
        return $false
    } catch {
        return $true
    }
}

$status = @{
    ok            = $false
    zotero_ping   = $false
    local_api     = $false
    imported      = 0
    already       = 0
    mapped        = 0
    relinked_uris = 0
    word_refresh  = 'skipped'
    error         = ''
}

if (-not (Test-Path -LiteralPath $LibRel)) {
    $status.error = 'missing library json'
    Save-Status $status
    Write-Log 'FAIL missing projects\English_Zotero_library.json'
    exit 3
}
if (-not (Test-Path -LiteralPath $DocRel)) {
    $status.error = 'missing English.docx'
    Save-Status $status
    Write-Log 'FAIL missing projects\English.docx'
    exit 3
}

Write-Log '== zotero hands-free: ping 127.0.0.1:23119'
try {
    $ping = Invoke-LocalHttp -Method GET -Url ($ZoteroBase + '/connector/ping') -TimeoutSec 5
    if ($ping.Status -ge 200 -and $ping.Status -lt 500) {
        $status.zotero_ping = $true
        Write-Log ('   OK connector ping HTTP ' + $ping.Status)
    } else {
        Write-Log ('   FAIL connector ping HTTP ' + $ping.Status)
    }
} catch {
    Write-Log ('   FAIL connector ping: ' + $_.Exception.Message)
}
if (-not $status.zotero_ping) {
    $status.error = 'Zotero not running on 127.0.0.1:23119 (start Zotero, keep Better BibTeX if you use it)'
    Save-Status $status
    exit 2
}

try {
    $api = Invoke-LocalHttp -Method GET -Url ($ZoteroBase + '/api/') -Headers @{ 'Zotero-API-Version' = '3' } -TimeoutSec 5
    if ($api.Status -ge 200 -and $api.Status -lt 300) {
        $status.local_api = $true
        Write-Log ('   OK local API HTTP ' + $api.Status)
    } else {
        Write-Log ('   WARN local API HTTP ' + $api.Status + ' (will still try /api/users/0/items)')
    }
} catch {
    Write-Log ('   WARN local API: ' + $_.Exception.Message)
}

$rawLib = Get-Content -LiteralPath $LibRel -Raw -Encoding UTF8
$library = $rawLib | ConvertFrom-Json
$nLib = @($library).Count
Write-Log ('== library items: ' + $nLib)

$missing = New-Object System.Collections.Generic.List[object]
$uriByCitekey = @{}

foreach ($csl in @($library)) {
    $ck = [string]$csl.'citation-key'
    $doi = [string]$csl.DOI
    $found = $null
    try { $found = Find-ZoteroItemByDoi $doi } catch {
        Write-Log ('   WARN search ' + $ck + ': ' + $_.Exception.Message)
    }
    if ($found) {
        $uri = Get-ItemUri $found
        if ($uri) {
            $uriByCitekey[$ck] = $uri
            $status.already = [int]$status.already + 1
        } else {
            $missing.Add($csl)
        }
    } else {
        $missing.Add($csl)
    }
}
Write-Log ('   already in Zotero: ' + $status.already + '  missing: ' + $missing.Count)

if ($missing.Count -gt 0) {
    Write-Log ('== importing ' + $missing.Count + ' items via /connector/saveItems')
    $payloadItems = New-Object System.Collections.Generic.List[object]
    foreach ($csl in $missing) { $payloadItems.Add((Convert-CslToConnectorItem $csl)) }
    $session = [guid]::NewGuid().ToString()
    $wrapper = @{
        sessionID = $session
        uri       = 'https://local.invalid/english-zotero-library'
        items     = $payloadItems
    }
    $body = $wrapper | ConvertTo-Json -Depth 12 -Compress
    if ($payloadItems.Count -eq 1 -and $body -notmatch '"items":\[') {
        $body = $body.Replace('"items":{', '"items":[{')
        if ($body.EndsWith('}}')) {
            $body = $body.Substring(0, $body.Length - 2) + '}]}'
        }
    }
    $hdr = @{
        'Content-Type'                      = 'application/json'
        'X-Zotero-Connector-API-Version'    = '3'
    }
    try {
        $save = Invoke-LocalHttp -Method POST -Url ($ZoteroBase + '/connector/saveItems') -Body $body -Headers $hdr -TimeoutSec 180
        Write-Log ('   saveItems HTTP ' + $save.Status)
        if ($save.Status -eq 201 -or ($save.Status -ge 200 -and $save.Status -lt 300)) {
            $status.imported = $missing.Count
        } elseif ($save.Status -eq 409) {
            $session = [guid]::NewGuid().ToString()
            Write-Log '   SESSION_EXISTS - retry with new session'
            $wrapper.sessionID = $session
            $body = $wrapper | ConvertTo-Json -Depth 12 -Compress
            $save = Invoke-LocalHttp -Method POST -Url ($ZoteroBase + '/connector/saveItems') -Body $body -Headers $hdr -TimeoutSec 180
            Write-Log ('   saveItems retry HTTP ' + $save.Status)
            if ($save.Status -eq 201 -or ($save.Status -ge 200 -and $save.Status -lt 300)) {
                $status.imported = $missing.Count
            } else {
                $status.error = ('saveItems HTTP ' + $save.Status)
            }
        } else {
            $status.error = ('saveItems HTTP ' + $save.Status + ' ' + $save.Body)
        }
    } catch {
        $status.error = ('saveItems: ' + $_.Exception.Message)
        Write-Log ('   FAIL ' + $status.error)
    }
    Start-Sleep -Seconds 2
    foreach ($csl in $missing) {
        $ck = [string]$csl.'citation-key'
        $doi = [string]$csl.DOI
        $found = $null
        try { $found = Find-ZoteroItemByDoi $doi } catch {}
        if ($found) {
            $uri = Get-ItemUri $found
            if ($uri) { $uriByCitekey[$ck] = $uri }
        }
    }
}

$status.mapped = $uriByCitekey.Keys.Count
Write-Log ('== mapped citekey -> uri: ' + $status.mapped + ' / ' + $nLib)

if ($status.mapped -lt $nLib) {
    $py = $null
    foreach ($cand in @('python', 'py', 'python3')) {
        $cmd = Get-Command $cand -ErrorAction SilentlyContinue
        if ($cmd) { $py = $cmd.Source; break }
    }
    $dbSrc = Join-Path $env:USERPROFILE 'Zotero\zotero.sqlite'
    $lookupPy = Join-Path (Get-Location) 'code\zotero_sqlite_lookup.py'
    if ($py -and (Test-Path -LiteralPath $lookupPy) -and (Test-Path -LiteralPath $dbSrc)) {
        Write-Log '== sqlite DOI lookup fallback'
        try {
            $pyOut = & $py $lookupPy $LibRel $dbSrc 2>$null
            if ($pyOut) {
                $sqlMap = $pyOut | ConvertFrom-Json
                foreach ($p in $sqlMap.PSObject.Properties) {
                    if (-not $uriByCitekey.ContainsKey($p.Name)) {
                        $uriByCitekey[$p.Name] = [string]$p.Value
                    }
                }
                $status.mapped = $uriByCitekey.Keys.Count
                Write-Log ('   after sqlite mapped=' + $status.mapped)
            }
        } catch {
            Write-Log ('   WARN sqlite lookup: ' + $_.Exception.Message)
        }
    }
}

$mapDir = Split-Path -Parent $MapRel
if (-not (Test-Path -LiteralPath $mapDir)) {
    New-Item -ItemType Directory -Path $mapDir -Force | Out-Null
}
$mapLines = New-Object System.Collections.Generic.List[string]
[void]$mapLines.Add('{')
$keysSorted = @($uriByCitekey.Keys | Sort-Object)
for ($i = 0; $i -lt $keysSorted.Count; $i++) {
    $k = [string]$keysSorted[$i]
    $u = [string]$uriByCitekey[$k]
    $u = $u.Replace('\', '\\').Replace('"', '\"')
    $comma = ','
    if ($i -eq $keysSorted.Count - 1) { $comma = '' }
    [void]$mapLines.Add('  "' + $k + '": "' + $u + '"' + $comma)
}
[void]$mapLines.Add('}')
$utf8 = New-Object System.Text.UTF8Encoding $false
[IO.File]::WriteAllLines((Join-Path (Get-Location) $MapRel), $mapLines.ToArray(), $utf8)

if ($status.mapped -lt $nLib) {
    $status.error = ('mapped ' + $status.mapped + ' of ' + $nLib)
    Save-Status $status
    Write-Log ('FAIL ' + $status.error)
    exit 3
}

$docPath = (Resolve-Path -LiteralPath $DocRel).Path
if (Test-FileLocked $docPath) {
    $status.error = 'English.docx is locked - close Word and retry'
    Save-Status $status
    Write-Log ('FAIL ' + $status.error)
    exit 4
}

Write-Log '== relink ITEM uris in English.docx'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$tmp = Join-Path $env:TEMP ('zotero_relink_' + [guid]::NewGuid().ToString('n'))
[System.IO.Compression.ZipFile]::ExtractToDirectory($docPath, $tmp)
$replaced = 0
$xmlFiles = Get-ChildItem -LiteralPath $tmp -Recurse -File | Where-Object { $_.Extension -eq '.xml' }
foreach ($xf in $xmlFiles) {
    $t = [IO.File]::ReadAllText($xf.FullName)
    $orig = $t
    foreach ($ck in $uriByCitekey.Keys) {
        $old = 'http://zotero.org/users/local/items/' + $ck
        $new = [string]$uriByCitekey[$ck]
        if ($t.Contains($old)) {
            $hits = ([regex]::Matches($t, [regex]::Escape($old))).Count
            $t = $t.Replace($old, $new)
            $replaced = $replaced + $hits
        }
    }
    if ($t -ne $orig) {
        [IO.File]::WriteAllText($xf.FullName, $t, $utf8)
    }
}
$status.relinked_uris = $replaced
Write-Log ('   replaced uri occurrences: ' + $replaced)
$outTmp = Join-Path $env:TEMP ('zotero_relink_out_' + [guid]::NewGuid().ToString('n') + '.docx')
New-DocxFromFolder $tmp $outTmp
Copy-Item -LiteralPath $outTmp -Destination $docPath -Force
Remove-Item -LiteralPath $outTmp -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath $tmp -Recurse -Force -ErrorAction SilentlyContinue

$del = 'deliverable\English.docx'
$delDir = Split-Path -Parent $del
if (Test-Path -LiteralPath $delDir) {
    Copy-Item -LiteralPath $docPath -Destination $del -Force
}

if ($replaced -lt 1) {
    $status.error = 'relink replaced 0 uris'
    Save-Status $status
    Write-Log ('FAIL ' + $status.error)
    exit 5
}

Write-Log '== Word COM ZoteroRefresh'
$word = $null
$doc = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    try { $word.DisplayAlerts = 0 } catch {}
    $doc = $word.Documents.Open($docPath, $false, $false)
    Start-Sleep -Seconds 2
    $ran = $false
    foreach ($macro in @('ZoteroRefresh', 'Zotero.ZoteroRefresh', 'Zotero.dotm!ZoteroRefresh')) {
        try {
            Write-Log ('   try Run ' + $macro)
            $word.Run($macro)
            $ran = $true
            $status.word_refresh = ('ok:' + $macro)
            Write-Log ('   OK Run ' + $macro)
            break
        } catch {
            Write-Log ('   skip ' + $macro + ': ' + $_.Exception.Message)
        }
    }
    if (-not $ran) {
        $status.word_refresh = 'macro-not-found'
    }
    try { $doc.Save() } catch {}
} catch {
    $status.word_refresh = ('failed:' + $_.Exception.Message)
    Write-Log ('   WARN Word COM: ' + $_.Exception.Message)
} finally {
    if ($doc) {
        try { $doc.Close($true) } catch { try { $doc.Close() } catch {} }
        [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($doc)
    }
    if ($word) {
        try { $word.Quit() } catch {}
        [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($word)
    }
    $doc = $null
    $word = $null
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}

$status.ok = $true
$status.error = ''
Save-Status $status
Write-Log ('== zotero hands-free done mapped=' + $status.mapped + ' relinked=' + $status.relinked_uris + ' refresh=' + $status.word_refresh)
exit 0
