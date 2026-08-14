#!/usr/bin/env python3
"""Audit sequence composition and arithmetic of the user-designated external v0.4 docking summary."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "revision_v3" / "external_docking_audit.json"
SOURCE_COMMIT = "e28c06db0614512eeb2bca217d2f9a760e804051"
DATA = [
    ("FLLHTTR", -9.60, 0.08),
    ("YLSLLQR", -9.49, 0.05),
    ("ALLLHRC", -9.29, 0.11),
    ("FCLHLQLR", -9.27, 0.09),
    ("YHHLLCRR", -9.03, 0.07),
    ("LLHLPKRTT", -9.01, 0.06),
    ("LLHPLRL", -8.94, 0.10),
    ("WLLVHLKK", -8.94, 0.04),
    ("LLHPLRC", -8.91, 0.08),
    ("HLLTLKKHV", -8.88, 0.05),
    ("HLPLLHRCC", -8.35, 0.12),
    ("HVLLLRQCA", -8.25, 0.09),
]
AA = set("ACDEFGHIKLMNPQRSTVWY")


def main() -> int:
    rows = []
    for sequence, mean, sd in DATA:
        rows.append({
            "sequence": sequence,
            "length": len(sequence),
            "histidine": sequence.count("H"),
            "cysteine": sequence.count("C"),
            "basic_R_plus_K": sequence.count("R") + sequence.count("K"),
            "aromatic_F_plus_Y_plus_W": sum(sequence.count(aa) for aa in "FYW"),
            "reported_vina_mean_kcal_per_mol": mean,
            "reported_sd_kcal_per_mol": sd,
            "valid_standard_amino_acids": set(sequence) <= AA,
        })
    checks = {
        "twelve_unique_sequences": len(rows) == len({row["sequence"] for row in rows}) == 12,
        "all_sequences_7_to_9_aa": all(7 <= row["length"] <= 9 for row in rows),
        "eleven_contain_histidine": sum(row["histidine"] > 0 for row in rows) == 11,
        "six_contain_cysteine": sum(row["cysteine"] > 0 for row in rows) == 6,
        "all_contain_basic_residue": all(row["basic_R_plus_K"] > 0 for row in rows),
        "all_use_standard_amino_acids": all(row["valid_standard_amino_acids"] for row in rows),
        "reported_means_are_nondecreasing_as_listed": all(
            rows[i]["reported_vina_mean_kcal_per_mol"] <= rows[i + 1]["reported_vina_mean_kcal_per_mol"]
            for i in range(len(rows) - 1)
        ),
        "reported_score_range_matches": min(row["reported_vina_mean_kcal_per_mol"] for row in rows) == -9.60
        and max(row["reported_vina_mean_kcal_per_mol"] for row in rows) == -8.25,
        "reported_sd_range_matches": min(row["reported_sd_kcal_per_mol"] for row in rows) == 0.04
        and max(row["reported_sd_kcal_per_mol"] for row in rows) == 0.12,
    }
    report = {
        "schema": "local.external_docking_summary_audit.v1",
        "external_repository_commit": SOURCE_COMMIT,
        "source_boundary": (
            "Sequences and Vina mean±SD values are transcribed from the user-designated external v0.4 report. "
            "Composition and arithmetic are recomputed here; docking was not rerun and raw docking artefacts were unavailable."
        ),
        "rows": rows,
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "verdict": "PASS" if all(checks.values()) else "FAIL",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
