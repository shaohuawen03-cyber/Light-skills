# External skill provenance / 外部技能来源

Checked and applied on 2026-08-12. External repositories were shallow/sparse cloned to temporary workspace paths for instruction review; they are not vendored into this project.

| Requested stage | Skill | Repository | Pinned commit reviewed | Licence/status note |
| --- | --- | --- | --- | --- |
| 1 Topic | `scientific-brainstorming` v1.1 | https://github.com/K-Dense-AI/scientific-agent-skills | `5ad4aae76bc40257b914367afacc6fd686a282d5` | MIT; proposals are not findings; preserve assumptions, adversarial review and decision logs. |
| 2 Search | `nature-academic-search` v2.0.0 | https://github.com/Yuan1z0825/nature-skills | `1ea82ffff20f40077bf84b74182f55eeaf3d111d` | Multi-source routing; structured-source first; unavailable services remain unavailable. |
| 3 Review | `literature-review` v1.7 | https://github.com/K-Dense-AI/scientific-agent-skills | `5ad4aae76bc40257b914367afacc6fd686a282d5` | MIT. Its mandatory AI-generated-schematic instruction is not followed for manuscript data figures because this project adopts the stricter programmatic-figure integrity rule; a programmatic evidence map may be used instead. |
| 4 Coordination | `academic-research-suite` adapter v0.1.24; vendored ARS v3.19.0 | https://github.com/Imbad0202/academic-research-skills-codex | `1f17aa452f5a7def3eb906c181e6ae9d80f91f77` | Adapter source reviewed. ARS upstream content is CC-BY-NC 4.0; this project records attribution and applies workflow principles without redistributing the suite. |
| 5 Statistics | `nature-statistics` | https://github.com/Yuan1z0825/nature-skills | `1ea82ffff20f40077bf84b74182f55eeaf3d111d` | Reporting/audit skill, not a substitute for reanalysis without raw data. |
| 6 Figure | `scientific-visualization` v1.1 and `nature-figure` | both repositories above | commits above | Only programmatic figures; no generative image model for scientific data or evidence. |
| 7 Writing | `nature-writing` | https://github.com/Yuan1z0825/nature-skills | `1ea82ffff20f40077bf84b74182f55eeaf3d111d` | Evidence-first argument rebuilding. |
| 8 Polishing | `nature-polishing` | https://github.com/Yuan1z0825/nature-skills | `1ea82ffff20f40077bf84b74182f55eeaf3d111d` | Meaning preservation and anti-overclaim take precedence over stylistic fluency. |
| 9 Submission | ARS formatting/integrity guidance plus repository `light-venue-matching`/`light-typesetting` | sources above and this repository | pinned external commits above; local commit recorded at delivery | Journal selection remains a user decision; no portal submission is performed. |

## Capability substitutions

- The academic-search MCP server, Scopus, Web of Science and institutional subscriptions are not mounted. Searches therefore use accessible structured/web sources and record coverage as bounded rather than systematic/exhaustive.
- No external unpublished manuscript text is uploaded. Search queries use broad topic/method terms.
- R, Pandoc, Office/LibreOffice and LaTeX availability are checked at execution time; absent tools are recorded rather than silently replaced with false claims.
