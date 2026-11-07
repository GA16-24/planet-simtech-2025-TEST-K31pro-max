from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    report = PdfReader(ROOT / "output" / "pdf" / "TEST-K31pro-max.pdf")
    texts = [page.extract_text() or "" for page in report.pages]
    bibliography_start = next(index for index, text in enumerate(texts) if "Literaturverzeichnis" in text)
    model = json.loads((ROOT / "output" / "model" / "results.json").read_text(encoding="utf-8"))
    presentation = json.loads((ROOT / "output" / "presentation" / "verification.json").read_text(encoding="utf-8"))
    playback_path = ROOT / "output" / "presentation" / "playback.json"
    playback = json.loads(playback_path.read_text(encoding="utf-8")) if playback_path.exists() else None
    summary = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "report": {
            "physical_pages": len(report.pages),
            "main_pages": bibliography_start - 1,
            "bibliography_and_appendix_pages": len(report.pages) - bibliography_start,
            "main_limit": 10,
            "back_limit": 5,
        },
        "model_validation": model["validation"],
        "presentation": presentation,
        "playback": playback,
    }
    (ROOT / "output" / "verification_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary["report"], ensure_ascii=False))


if __name__ == "__main__":
    main()
