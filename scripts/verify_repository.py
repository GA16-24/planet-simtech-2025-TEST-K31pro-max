from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def main() -> None:
    require_clean = "--require-clean" in sys.argv
    required = [
        "README.md",
        "PROVENANCE.md",
        "EXCLUSION_LOG.md",
        "decisions.tsv",
        "data/parameters.yml",
        "sources/registry.yml",
        "compliance/regeln.md",
        "compliance/layout_referenz.md",
        "compliance/checklist.md",
        "review/model_configuration.md",
        "review/rubric.md",
        "review/README.md",
        "output/model/results.json",
        "output/model/manifest.json",
        "output/pdf/TEST-K31pro-max.pdf",
        "output/presentation/Blautopf_Finale.pdf",
        "output/presentation/Blautopf_Finale.mp4",
        "presentation/speaker_notes.md",
        "presentation/jury_qa.md",
        "presentation/rehearsal.md",
        "presentation/rights.md",
    ]
    for relative in required:
        require((ROOT / relative).is_file(), f"Fehlt: {relative}")

    with (ROOT / "decisions.tsv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle, delimiter="\t"))
    require(bool(rows) and rows[0] == ["ts", "phase", "decision", "why", "evidence", "result"], "Entscheidungsprotokoll hat falsche Spalten")
    for index, row in enumerate(rows[1:], start=2):
        require(len(row) == 6, f"decisions.tsv Zeile {index} hat {len(row)} statt 6 Zellen")

    with (ROOT / "sources" / "registry.yml").open(encoding="utf-8") as handle:
        registry = yaml.safe_load(handle)
    ids = [entry["id"] for entry in registry]
    require(len(ids) == len(set(ids)), "Quellen-IDs sind nicht eindeutig")
    for entry in registry:
        require(bool(entry.get("url") or entry.get("doi")), f"Quelle {entry['id']} ohne URL oder DOI")
        require(bool(entry.get("accessed")), f"Quelle {entry['id']} ohne Abrufdatum")

    manifest_path = ROOT / "output" / "model" / "manifest.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for relative, expected in manifest.items():
            path = ROOT / relative
            require(path.is_file(), f"Manifestdatei fehlt: {relative}")
            if path.is_file():
                actual = hashlib.sha256(path.read_bytes()).hexdigest()
                require(actual == expected, f"Hashabweichung: {relative}")

    if require_clean:
        status = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, check=True, capture_output=True, text=True).stdout
        require(not status.strip(), f"Git-Arbeitsbaum ist nicht sauber:\n{status}")

    if ERRORS:
        for error in ERRORS:
            print(f"FEHLER: {error}")
        sys.exit(1)
    print("Repositoryprüfung bestanden: Pflichtdateien, TSV, Quellenregister und Modellhashes")


if __name__ == "__main__":
    main()
