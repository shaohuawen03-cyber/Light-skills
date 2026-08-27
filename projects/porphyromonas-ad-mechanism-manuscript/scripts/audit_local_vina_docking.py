#!/usr/bin/env python3
"""Audit the local three-run AutoDock Vina summary used by the standalone reports."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "quality_reports" / "local_vina_docking_audit.json"
SOURCE = ROOT / "source_materials" / "md_results" / "local_vina_docking_summary.csv"
RAW = ROOT / "docking" / "Summary_Vina_Docking.csv"
EXPECTED = {
    "ALLLHRC": (-9.288, -9.184, 0.109, "run_1"),
    "FCLHLQLR": (-9.27, -8.958, 0.479, "run_1"),
    "FLLHTTR": (-9.597, -8.768, 1.411, "run_1"),
    "HLLTLKKHV": (-8.884, -8.690, 0.196, "run_1"),
    "HLPLLHRCC": (-8.352, -8.283, 0.071, "run_2"),
    "HVLLLRQCA": (-8.251, -8.073, 0.160, "run_2"),
    "LLHLPKRTT": (-9.006, -8.886, 0.161, "run_3"),
    "LLHPLRC": (-8.908, -8.781, 0.110, "run_2"),
    "LLHPLRL": (-8.942, -8.910, 0.046, "run_1"),
    "WLLVHLKK": (-8.941, -8.639, 0.263, "run_3"),
    "YHHLLCRR": (-9.028, -8.617, 0.430, "run_2"),
    "YLSLLQR": (-9.494, -9.437, 0.085, "run_3"),
}
AA = set("ACDEFGHIKLMNPQRSTVWY")


def load(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["Ligand"].strip().upper(): row for row in csv.DictReader(handle)}


def main() -> int:
    clean = load(SOURCE)
    raw = load(RAW)
    rows = []
    for sequence, (best, mean, sd, run) in EXPECTED.items():
        item = clean[sequence]
        raw_item = raw[sequence]
        rows.append({
            "sequence": sequence,
            "length": len(sequence),
            "valid_standard_amino_acids": set(sequence) <= AA,
            "best_matches": float(item["Best_Affinity_kcal_mol"]) == best,
            "mean_matches": float(item["Mean_Affinity_kcal_mol"]) == mean,
            "sd_matches": float(item["SD_Affinity"]) == sd,
            "best_run_matches": item["Best_Run"] == run,
            "n_success_is_3": int(item["N_Success"]) == 3,
            "raw_best_matches_clean": float(raw_item["Best_Affinity_kcal_mol"]) == best,
            "raw_mean_matches_clean": float(raw_item["Mean_Affinity_kcal_mol"]) == mean,
            "raw_sd_matches_clean": float(raw_item["SD_Affinity"]) == sd,
        })
    best_values = [EXPECTED[name][0] for name in EXPECTED]
    mean_values = [EXPECTED[name][1] for name in EXPECTED]
    checks = {
        "twelve_unique_sequences": len(clean) == len(EXPECTED) == 12,
        "all_sequences_7_to_9_aa": all(7 <= len(name) <= 9 for name in EXPECTED),
        "all_use_standard_amino_acids": all(set(name) <= AA for name in EXPECTED),
        "every_ligand_has_three_successful_runs": all(row["n_success_is_3"] for row in rows),
        "clean_table_matches_expected_values": all(
            row["best_matches"] and row["mean_matches"] and row["sd_matches"] and row["best_run_matches"]
            for row in rows
        ),
        "raw_numeric_fields_match_clean_table": all(
            row["raw_best_matches_clean"] and row["raw_mean_matches_clean"] and row["raw_sd_matches_clean"]
            for row in rows
        ),
        "best_score_range_matches": round(min(best_values), 3) == -9.597 and round(max(best_values), 3) == -8.251,
        "mean_score_range_matches": round(min(mean_values), 3) == -9.437 and round(max(mean_values), 3) == -8.073,
        "fllhttr_has_largest_sd": EXPECTED["FLLHTTR"][2] == max(item[2] for item in EXPECTED.values()),
        "ylsllqr_has_strongest_mean": EXPECTED["YLSLLQR"][1] == min(mean_values),
        "clean_table_has_no_pdbqt_path_column": "Best_PDBQT" not in next(iter(clean.values())),
    }
    report = {
        "schema": "local.vina_docking_summary_audit.v1",
        "source_boundary": (
            "Numeric docking scores are taken from the user-uploaded local three-run Vina summary. "
            "Hydrogen-bond geometry and PAS labels continue to describe the best-scoring pose. "
            "Individual PDBQT files and docking configuration logs are not archived in this package."
        ),
        "rows": rows,
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "verdict": "PASS" if all(checks.values()) else "FAIL",
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
