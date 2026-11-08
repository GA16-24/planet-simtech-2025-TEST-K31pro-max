from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    if len(sys.argv) != 2 or not sys.argv[1].startswith("round"):
        raise SystemExit("Verwendung: freeze_revision.py roundN")
    round_name = sys.argv[1]
    status = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, check=True, capture_output=True, text=True).stdout
    if status.strip():
        raise SystemExit(f"Einfrieren verlangt einen sauberen Commit:\n{status}")
    subprocess.run(["make", "verify"], cwd=ROOT, check=True)
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.strip()
    tracked_raw = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True).stdout
    tracked = [part.decode("utf-8") for part in tracked_raw.split(b"\0") if part]
    tree_raw = subprocess.run(["git", "ls-tree", "-r", "-z", "--name-only", commit], cwd=ROOT, check=True, capture_output=True).stdout
    tree_files = {part.decode("utf-8") for part in tree_raw.split(b"\0") if part}
    if set(tracked) != tree_files:
        raise SystemExit(f"Dateimenge oder Pfade stimmen nicht mit dem Commit überein: {len(tracked)} gegen {len(tree_files)}")
    status_after = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, check=True, capture_output=True, text=True).stdout
    if status_after.strip():
        raise SystemExit(f"Die Prüfung hat den Arbeitsbaum verändert:\n{status_after}")
    hashes = {}
    for relative in tracked:
        path = ROOT / relative
        if not path.is_file():
            raise SystemExit(f"Versionierte Datei fehlt: {relative}")
        committed = subprocess.run(["git", "show", f"{commit}:{relative}"], cwd=ROOT, check=True, capture_output=True).stdout
        if committed != path.read_bytes():
            raise SystemExit(f"Arbeitsdatei weicht vom Commit ab: {relative}")
        hashes[relative] = hashlib.sha256(committed).hexdigest()
    destination = ROOT / "review" / "rounds" / round_name
    destination.mkdir(parents=True, exist_ok=True)
    revision = {
        "round": round_name,
        "commit": commit,
        "frozen_utc": datetime.now(timezone.utc).isoformat(),
        "tracked_file_count": len(hashes),
        "verification_command": "make verify",
        "verification_result": "passed",
        "paper_reproduction_commands": ["make model test report", "make review-package"],
        "historical_presentation_checks_included": True,
        "delivery_scope": "Research Paper only; historical presentation checks are outside the delivery scope",
        "files": hashes,
    }
    (destination / "revision.json").write_text(json.dumps(revision, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{round_name}: {commit}, {len(hashes)} Dateien, make verify bestanden")


if __name__ == "__main__":
    main()
