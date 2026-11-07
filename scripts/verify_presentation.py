from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pdfplumber
from PIL import Image, ImageStat
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "presentation"
PDF = OUT / "Blautopf_Finale.pdf"
VIDEO = OUT / "Blautopf_Finale.mp4"
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def main() -> None:
    for path in [PDF, VIDEO, OUT / "Blautopf_Finale.vtt", ROOT / "presentation" / "speaker_notes.md", ROOT / "presentation" / "timings.json", ROOT / "presentation" / "rehearsal.md"]:
        require(path.is_file(), f"Fehlt: {path}")
    if ERRORS:
        finish()
    reader = PdfReader(PDF)
    require(len(reader.pages) == 10, f"Folienzahl {len(reader.pages)} statt 10")
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    text = text.replace("\u2011", "-").replace("\u2010", "-")
    for required in ["877,8", "952,0", "12,48", "Schlussfolgerung", "KI-Offenlegung"]:
        require(required in text, f"Folieninhalt fehlt: {required}")
    for forbidden in ["TODO", "TBD", "???", "—"]:
        require(forbidden not in text, f"Unerwünschter Folientext: {forbidden}")

    with pdfplumber.open(PDF) as pdf:
        for index, page in enumerate(pdf.pages):
            require(abs(page.width / page.height - 16 / 9) < 0.01, f"Folie {index + 1} ist nicht 16:9")

    probe = subprocess.run([
        "ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(VIDEO)
    ], check=True, capture_output=True, text=True)
    media = json.loads(probe.stdout)
    video_streams = [stream for stream in media["streams"] if stream["codec_type"] == "video"]
    audio_streams = [stream for stream in media["streams"] if stream["codec_type"] == "audio"]
    require(len(video_streams) == 1, "MP4 braucht genau einen Videostream")
    require(len(audio_streams) == 1, "MP4 braucht genau einen Audiostream")
    video = video_streams[0]
    audio = audio_streams[0]
    require(video["codec_name"] == "h264", f"Videocodec {video['codec_name']} statt H.264")
    require(audio["codec_name"] == "aac", f"Audiocodec {audio['codec_name']} statt AAC")
    require(video["width"] == 1920 and video["height"] == 1080, "Video ist nicht 1920 x 1080")
    require(video["pix_fmt"] == "yuv420p", "Video-Pixelformat ist nicht yuv420p")
    duration = float(media["format"]["duration"])
    require(0.0 < duration <= 300.0, f"Videodauer {duration:.3f}s überschreitet 300s")
    require(duration <= 295.0, f"Videodauer {duration:.3f}s überschreitet interne 295s")

    timings = json.loads((ROOT / "presentation" / "timings.json").read_text(encoding="utf-8"))
    require(abs(timings["duration_s"] - duration) < 0.05, "timings.json weicht von MP4 ab")
    require(len(timings["slides"]) == 10, "timings.json enthält nicht zehn Segmente")
    require(abs(timings["slides"][-1]["end_s"] - duration) < 0.20, "Segmentsumme weicht um mehr als die Zeitbasisrundung von MP4 ab")

    subprocess.run(["ffmpeg", "-v", "error", "-i", str(VIDEO), "-f", "null", "-"], check=True)
    frames = ROOT / "tmp" / "video_frames"
    frames.mkdir(parents=True, exist_ok=True)
    for index, fraction in enumerate([0.02, 0.25, 0.50, 0.75, 0.96], start=1):
        subprocess.run([
            "ffmpeg", "-y", "-v", "error", "-ss", f"{duration * fraction:.3f}", "-i", str(VIDEO),
            "-frames:v", "1", str(frames / f"frame_{index}.png")
        ], check=True)
    for path in sorted(frames.glob("frame_*.png")):
        with Image.open(path).convert("L") as image:
            require(image.size == (1920, 1080), f"Falsche Framegröße: {path.name}")
            require(ImageStat.Stat(image).stddev[0] > 8.0, f"Videoframe wirkt leer: {path.name}")

    report = {
        "duration_s": duration,
        "video_codec": video["codec_name"],
        "audio_codec": audio["codec_name"],
        "width": video["width"],
        "height": video["height"],
        "slide_count": len(reader.pages),
        "segment_count": len(timings["slides"]),
        "full_decode_passed": True,
        "rendered_frames_checked": len(list(frames.glob("frame_*.png"))),
        "live_human_delivery_verified": False,
        "all_automated_checks_passed": not ERRORS,
    }
    (OUT / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    finish()


def finish() -> None:
    if ERRORS:
        for error in ERRORS:
            print(f"FEHLER: {error}")
        sys.exit(1)
    print("Präsentationsprüfung bestanden: PDF, MP4, Codecs, Dauer, Segmente und Videoframes")


if __name__ == "__main__":
    main()
