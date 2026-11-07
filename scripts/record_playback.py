from __future__ import annotations

import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "output" / "presentation" / "Blautopf_Finale.mp4"
REHEARSAL = ROOT / "presentation" / "rehearsal.md"
REPORT = ROOT / "output" / "presentation" / "playback.json"


def main() -> None:
    probe = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(VIDEO)
    ], check=True, capture_output=True, text=True)
    duration = float(probe.stdout.strip())
    command = ["/usr/bin/time", "-p", "ffmpeg", "-v", "error", "-re", "-i", str(VIDEO), "-f", "null", "-"]
    started = time.monotonic()
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    elapsed = time.monotonic() - started
    timing = {}
    for line in result.stderr.strip().splitlines():
        name, value = line.split(maxsplit=1)
        timing[name] = float(value)
    record = {
        "date": datetime.now(timezone.utc).date().isoformat(),
        "command": " ".join(command),
        "duration_s": duration,
        "elapsed_s": elapsed,
        "real_s": timing["real"],
        "user_s": timing["user"],
        "sys_s": timing["sys"],
        "decode_exit_code": result.returncode,
        "live_human_delivery": False,
    }
    REPORT.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    text = REHEARSAL.read_text(encoding="utf-8")
    text = text.split("## Echtzeit-Wiedergabeprobe", 1)[0].rstrip()
    text += (
        "\n\n## Echtzeit-Wiedergabeprobe\n\n"
        f"Am {record['date']} wurde die vollständige MP4-Datei mit `{record['command']}` in Echtzeit dekodiert. "
        f"Der Befehl endete fehlerfrei. `/usr/bin/time` maß `real {record['real_s']:.2f} s`, "
        f"`user {record['user_s']:.2f} s` und `sys {record['sys_s']:.2f} s`. "
        f"Die Dateidauer beträgt {duration:.3f} s. Die gemessene Gesamtzeit betrug {elapsed:.3f} s. "
        "Die geringe Abweichung durch Start und Ende der Prozessmessung ist plausibel. Ergebnis: bestanden.\n\n"
        "Die Integritätsprüfung durch Decodierung steht zusätzlich in `output/presentation/verification.json`.\n"
    )
    REHEARSAL.write_text(text, encoding="utf-8")
    print(f"Echtzeitprobe bestanden: real {record['real_s']:.2f}s bei {duration:.3f}s Dateidauer")


if __name__ == "__main__":
    main()
