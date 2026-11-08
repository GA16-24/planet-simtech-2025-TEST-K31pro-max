from __future__ import annotations

import shutil
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "review" / "rendered"


def montage(paths: list[Path], destination: Path, columns: int, width: int) -> None:
    rows = (len(paths) + columns - 1) // columns
    ratio = 1.414 if "report" in destination.name else 0.5625
    height = int(width * ratio)
    label = 26
    canvas = Image.new("RGB", (columns * width, rows * (height + label)), (236, 239, 241))
    draw = ImageDraw.Draw(canvas)
    for index, path in enumerate(paths):
        image = Image.open(path).convert("RGB")
        image.thumbnail((width, height))
        x = (index % columns) * width
        y = (index // columns) * (height + label)
        canvas.paste(image, (x, y + label))
        draw.text((x + 6, y + 6), path.stem, fill=(0, 0, 0))
    canvas.save(destination)


def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    report_dest = DEST / "report_pages"
    slides_dest = DEST / "presentation_pages"
    frames_dest = DEST / "video_frames"
    for source, destination in [
        (ROOT / "tmp" / "report_pages", report_dest),
        (ROOT / "tmp" / "presentation_pages", slides_dest),
        (ROOT / "tmp" / "video_frames", frames_dest),
    ]:
        if destination.exists():
            shutil.rmtree(destination)
        if source.exists():
            shutil.copytree(source, destination)
    report_pages = sorted(report_dest.glob("page-*.png"))
    if not report_pages:
        raise FileNotFoundError("Keine gerenderten Berichtsseiten gefunden")
    montage(report_pages, DEST / "report_contact.png", 3, 500)
    for source, contact in [(slides_dest, DEST / "presentation_contact.png"), (frames_dest, DEST / "video_contact.png")]:
        images = sorted(source.glob("*.png"))
        if images:
            montage(images, contact, 2, 640)
        elif contact.exists():
            contact.unlink()
    print(f"Review-Artefakte in {DEST}")


if __name__ == "__main__":
    main()
