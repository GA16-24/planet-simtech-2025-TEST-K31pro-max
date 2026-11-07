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
    tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.splitlines()
    hashes = {}
    for relative in tracked:
        path = ROOT / relative
        if path.is_file():
            hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    destination = ROOT / "review" / "rounds" / round_name
    destination.mkdir(parents=True, exist_ok=True)
    revision = {
        "round": round_name,
        "commit": commit,
        "frozen_utc": datetime.now(timezone.utc).isoformat(),
        "tracked_file_count": len(hashes),
        "verification_command": "make verify",
        "verification_result": "passed",
        "files": hashes,
    }
    (destination / "revision.json").write_text(json.dumps(revision, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{round_name}: {commit}, {len(hashes)} Dateien, make verify bestanden")


if __name__ == "__main__":
    main()
