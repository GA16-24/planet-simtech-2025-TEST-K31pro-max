from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    if len(sys.argv) != 2 or not sys.argv[1].startswith("round"):
        raise SystemExit("Verwendung: council_prompt.py roundN")
    round_name = sys.argv[1]
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.strip()
    template = (ROOT / "review" / "council_prompt.md").read_text(encoding="utf-8")
    prompt = template.replace("RUNDE", round_name).replace("COMMIT", commit).replace("REPO", str(ROOT))
    destination = ROOT / "review" / "rounds" / round_name / "prompt.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(prompt, encoding="utf-8")
    print(destination)


if __name__ == "__main__":
    main()
