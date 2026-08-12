#!/usr/bin/env python3
"""Deterministic aggregate-only statistics audit for revision_v2.

No inferential statistics are performed because subject/sample-level outcomes are absent.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "revision_v2" / "statistics_audit.json"

c = {
    "healthy_raw_sorfs": 11_269_961,
    "periodontitis_raw_sorfs": 11_721_988,
    "healthy_filtered": 31_510,
    "periodontitis_filtered": 33_786,
    "healthy_short": 30_557,
    "healthy_long": 953,
    "periodontitis_short": 32_754,
    "periodontitis_long": 1_032,
    "healthy_bbb_short": 3_359,
    "healthy_bbb_long": 40,
    "periodontitis_bbb_short": 3_446,
    "periodontitis_bbb_long": 72,
    "ntx_evaluated": 3_299,
    "ntx_not_evaluated": 219,
    "ntx_positive": 923,
    "metal_positive_source_reported": 111,
    "chel_ge_025": 15,
    "main_frs_lt_050": 12,
    "strict_frs_lt_045": 8,
}


def pct(n: int, d: int) -> float:
    return 100.0 * n / d

checks = {
    "healthy_length_branches_sum_to_filtered": c["healthy_short"] + c["healthy_long"] == c["healthy_filtered"],
    "periodontitis_length_branches_sum_to_filtered": c["periodontitis_short"] + c["periodontitis_long"] == c["periodontitis_filtered"],
    "healthy_bbb_not_above_branch_denominators": c["healthy_bbb_short"] <= c["healthy_short"] and c["healthy_bbb_long"] <= c["healthy_long"],
    "periodontitis_bbb_not_above_branch_denominators": c["periodontitis_bbb_short"] <= c["periodontitis_short"] and c["periodontitis_bbb_long"] <= c["periodontitis_long"],
    "ntx_partition_sums_to_periodontitis_bbb": c["ntx_evaluated"] + c["ntx_not_evaluated"] == c["periodontitis_bbb_short"] + c["periodontitis_bbb_long"],
    "ntx_positive_not_above_evaluated": c["ntx_positive"] <= c["ntx_evaluated"],
    "reported_downstream_counts_are_monotone": c["strict_frs_lt_045"] <= c["main_frs_lt_050"] <= c["chel_ge_025"] <= c["metal_positive_source_reported"],
}

metrics = {
    "healthy_filtered_retention_pct": pct(c["healthy_filtered"], c["healthy_raw_sorfs"]),
    "periodontitis_filtered_retention_pct": pct(c["periodontitis_filtered"], c["periodontitis_raw_sorfs"]),
    "healthy_bbb_short_pct": pct(c["healthy_bbb_short"], c["healthy_short"]),
    "healthy_bbb_long_pct": pct(c["healthy_bbb_long"], c["healthy_long"]),
    "periodontitis_bbb_short_pct": pct(c["periodontitis_bbb_short"], c["periodontitis_short"]),
    "periodontitis_bbb_long_pct": pct(c["periodontitis_bbb_long"], c["periodontitis_long"]),
    "periodontitis_bbb_combined_count": c["periodontitis_bbb_short"] + c["periodontitis_bbb_long"],
    "periodontitis_bbb_short_share_pct": pct(c["periodontitis_bbb_short"], c["periodontitis_bbb_short"] + c["periodontitis_bbb_long"]),
    "ntx_coverage_pct": pct(c["ntx_evaluated"], c["periodontitis_bbb_short"] + c["periodontitis_bbb_long"]),
    "ntx_positive_among_evaluated_pct": pct(c["ntx_positive"], c["ntx_evaluated"]),
    "chel_among_reported_metal_positive_pct": pct(c["chel_ge_025"], c["metal_positive_source_reported"]),
    "main_among_reported_metal_positive_pct": pct(c["main_frs_lt_050"], c["metal_positive_source_reported"]),
    "strict_among_reported_metal_positive_pct": pct(c["strict_frs_lt_045"], c["metal_positive_source_reported"]),
    "strict_retained_from_main_pct": pct(c["strict_frs_lt_045"], c["main_frs_lt_050"]),
}

payload = {
    "analysis_scope": "aggregate descriptive audit only",
    "biological_experimental_unit": "participant/sample; row-level values unavailable",
    "candidate_counts_are_not_independent_biological_replicates": True,
    "inferential_statistics_performed": False,
    "counts": c,
    "checks": checks,
    "metrics_unrounded": metrics,
    "all_checks_pass": all(checks.values()),
    "boundary": "The source narrative places the 111 metal-positive candidates after NTxPred2, but no row-level handoff was supplied; 111/923 is intentionally not reported as an audited transition rate.",
}
OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(OUT)
print(f"all_checks_pass={payload['all_checks_pass']}")
