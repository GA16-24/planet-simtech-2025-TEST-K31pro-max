from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRESENTATION = ROOT / "presentation"
OUT = ROOT / "output" / "presentation"
BUILD = ROOT / "tmp" / "video_build"
AUDIO = PRESENTATION / "audio"
SLIDES = ROOT / "tmp" / "presentation_pages"
VIDEO = OUT / "Blautopf_Finale.mp4"


def run(command: list[str], stdout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=True, text=True, stdout=stdout)


def duration(path: Path) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def timestamp(seconds: float, vtt: bool = True) -> str:
    millis = int(round(seconds * 1000))
    hours, remainder = divmod(millis, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    secs, ms = divmod(remainder, 1000)
    separator = "," if vtt else "."
    return f"{hours:02d}:{minutes:02d}:{secs:02d}{separator}{ms:03d}"


def main() -> None:
    regenerate = "--regenerate-tts" in sys.argv
    narration = json.loads((PRESENTATION / "narration.json").read_text(encoding="utf-8"))
    images = sorted(SLIDES.glob("slide-*.png"))
    if len(images) != len(narration):
        raise RuntimeError(f"{len(images)} Folienbilder für {len(narration)} Sprechabschnitte")
    BUILD.mkdir(parents=True, exist_ok=True)
    AUDIO.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)

    raw_durations = []
    for index, slide in enumerate(narration, start=1):
        audio = AUDIO / f"slide_{index:02d}.wav"
        if regenerate or not audio.exists():
            raw_audio = BUILD / f"slide_{index:02d}_espeak.wav"
            run(["espeak-ng", "-v", "de", "-s", "170", "-p", "40", "-a", "180", "-w", str(raw_audio), slide["narration"]])
            run([
                "ffmpeg", "-y", "-v", "error", "-i", str(raw_audio),
                "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                "-ar", "24000", "-ac", "1", "-c:a", "pcm_s16le", str(audio),
            ])
        raw_durations.append(duration(audio))
    tempo = max(1.0, (sum(raw_durations) + 0.35 * len(narration)) / 290.0)
    if tempo > 1.20:
        raise RuntimeError(f"Erforderlicher Tempofaktor {tempo:.3f} wäre nicht mehr verständlich")

    segments = []
    for index, (slide, image) in enumerate(zip(narration, images), start=1):
        audio = AUDIO / f"slide_{index:02d}.wav"
        processed_audio = BUILD / f"slide_{index:02d}_processed.wav"
        run([
            "ffmpeg", "-y", "-v", "error", "-i", str(audio),
            "-af", f"atempo={tempo:.6f}", "-ar", "24000", "-ac", "1", "-c:a", "pcm_s16le", str(processed_audio),
        ])
        audio_duration = duration(processed_audio)
        segment_duration = audio_duration + 0.35
        segment = BUILD / f"segment_{index:02d}.mp4"
        run([
            "ffmpeg", "-y", "-v", "error", "-loop", "1", "-i", str(image), "-i", str(processed_audio),
            "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:white,setsar=1,format=yuv420p", "-r", "30",
            "-af", "apad=pad_dur=0.35", "-t", f"{segment_duration:.6f}",
            "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
            "-movflags", "+faststart", str(segment),
        ])
        segments.append({
            "slide": index,
            "title": slide["title"],
            "audio_duration_s": audio_duration,
            "segment_duration_s": segment_duration,
            "narration": slide["narration"],
            "sources": slide["sources"],
            "image": str(image.relative_to(ROOT)),
            "audio": str(audio.relative_to(ROOT)),
        })

    concat = BUILD / "concat.txt"
    concat.write_text("".join(f"file '{BUILD / f'segment_{index:02d}.mp4'}'\n" for index in range(1, len(segments) + 1)), encoding="utf-8")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", "-movflags", "+faststart", str(VIDEO)])
    total = duration(VIDEO)
    if total > 295.0:
        raise RuntimeError(f"Videodauer {total:.3f}s überschreitet die interne Grenze von 295s")

    cursor = 0.0
    vtt = ["WEBVTT", ""]
    notes = ["# Sprechtext und Quellen", "", f"Die Vertonung verwendet eSpeak NG 1.52.0 mit deutscher Stimme. Der Tempofaktor nach der Laufzeitmessung beträgt {tempo:.4f}. Es handelt sich nicht um eine menschliche Live-Präsentation.", ""]
    for segment in segments:
        segment["start_s"] = cursor
        cursor += segment["segment_duration_s"]
        segment["end_s"] = cursor
        notes.extend([
            f"## Folie {segment['slide']}. {segment['title']}",
            "",
            f"Zeit {timestamp(segment['start_s'], False)} bis {timestamp(segment['end_s'], False)}, effektive Dauer {segment['segment_duration_s']:.2f} s.",
            "",
            segment["narration"],
            "",
            "Quellen und Belege:",
            *[f"- {source}" for source in segment["sources"]],
            "",
        ])
        sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", segment["narration"]) if part.strip()]
        words = sum(len(sentence.split()) for sentence in sentences)
        sentence_start = segment["start_s"]
        for sentence in sentences:
            share = len(sentence.split()) / words
            sentence_end = sentence_start + share * segment["audio_duration_s"]
            vtt.extend([f"{timestamp(sentence_start)} --> {timestamp(sentence_end)}", sentence, ""])
            sentence_start = sentence_end

    (OUT / "Blautopf_Finale.vtt").write_text("\n".join(vtt), encoding="utf-8")
    (PRESENTATION / "speaker_notes.md").write_text("\n".join(notes), encoding="utf-8")
    timings = {
        "video": str(VIDEO.relative_to(ROOT)),
        "duration_s": total,
        "maximum_allowed_s": 300.0,
        "internal_limit_s": 295.0,
        "subtitle_alignment": "word-proportional, not forced alignment",
        "slides": segments,
    }
    (PRESENTATION / "timings.json").write_text(json.dumps(timings, ensure_ascii=False, indent=2), encoding="utf-8")
    rehearsal = [
        "# Dokumentierte Zeitprobe",
        "",
        f"Technische Laufzeitmessung am {datetime.now(timezone.utc).date().isoformat()} mit `ffprobe` an der tatsächlich erzeugten MP4-Datei.",
        "",
        "| Folie | Sprache in s | Segment in s | Summe in s |",
        "| --- | ---: | ---: | ---: |",
    ]
    for segment in segments:
        rehearsal.append(f"| {segment['slide']} | {segment['audio_duration_s']:.2f} | {segment['segment_duration_s']:.2f} | {segment['end_s']:.2f} |")
    rehearsal.extend([
        "",
        f"Gesamtdauer der fertigen MP4-Datei: {total:.3f} s, entsprechend {int(total // 60)}:{total % 60:04.1f} min.",
        "Offizielles Maximum: 300 s. Interne Produktionsgrenze: 295 s. Ergebnis: bestanden.",
        "",
        "Die Zeitprobe misst die reale synthetische Sprachfassung und die kodierte Videodatei. Sie ist keine behauptete menschliche Live-Probe. Vor einer echten Finalteilnahme müssen die präsentierenden Personen eine eigene Probe mit Rollenverteilung, Technik und Fragen durchführen und dokumentieren.",
        "",
        "Die VTT-Satzzeiten werden proportional zur Wortzahl der Sprechtexte und zur gemessenen Audiodauer berechnet. Sie sind nicht durch Forced Alignment verifiziert. Vor einer Abgabe sind sie manuell zu prüfen.",
        "",
        "Die zusätzliche Echtzeit-Wiedergabe und ihre Messung werden nach dem Export in diesem Dokument ergänzt. Die Integritätsprüfung durch Decodierung steht in `output/presentation/verification.json`.",
        "",
    ])
    (PRESENTATION / "rehearsal.md").write_text("\n".join(rehearsal), encoding="utf-8")
    print(f"Video erzeugt: {VIDEO}, {total:.3f}s, {len(segments)} Folien")


if __name__ == "__main__":
    main()
