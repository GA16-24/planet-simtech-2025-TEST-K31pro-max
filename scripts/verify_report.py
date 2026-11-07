from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import pdfplumber
from PIL import Image, ImageStat
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "output" / "pdf" / "TEST-K31pro-max.pdf"
RENDER = ROOT / "tmp" / "report_pages"
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def main() -> None:
    require(PDF.is_file(), f"Fehlt: {PDF}")
    if ERRORS:
        finish()
    reader = PdfReader(PDF)
    require(len(reader.pages) >= 8, "Bericht hat zu wenige Seiten")
    metadata = reader.metadata or {}
    require(not metadata.get("/Author"), "PDF-Autorenmetadaten gefährden Anonymität")
    page_texts = [page.extract_text() or "" for page in reader.pages]
    full_text = "\n".join(page_texts)
    require("TEST-K31pro-max" in page_texts[0], "Team-ID fehlt auf dem Deckblatt")
    require("PlaNeT SimTech" in page_texts[0], "Wettbewerbsname fehlt")
    require("07.11.2026" in page_texts[0], "Datum fehlt")
    for section in ["Zusammenfassung", "Einführung", "Methode", "Diskussion", "Schlussfolgerung", "Literaturverzeichnis"]:
        require(section in full_text, f"Pflichtabschnitt fehlt: {section}")
    for forbidden in ["TODO", "TBD", "PLATZHALTER", "???", "ChatGPT", "GA16-24", "MacBook", "Kimi Code CLI"]:
        require(forbidden not in full_text, f"Unerwünschter Text im Bericht: {forbidden}")
    require("—" not in full_text, "Em dash im Bericht")
    require("Kimi K3.1 Pro" in full_text, "KI-Offenlegung fehlt")
    require("Vulkan" in full_text or "vulkan" in full_text, "Szenarioprämisse fehlt")
    require("877" in full_text and "MW" in full_text, "Zentrale Modellgröße fehlt")
    summary_text = re.sub(r"\s+", " ", page_texts[1].split("1. Einführung", 1)[0].replace("-\n", "").replace("\n", " "))
    require("Für stärkeren Wasserfluss wird die Anlage größer ausgelegt" in summary_text, "Zusammenfassung ist unvollständig")
    require("p90" not in summary_text and "Barwert" not in summary_text and "H1" not in summary_text, "Zusammenfassung verwendet unerklärte Fachkürzel")
    require("1053,3" in full_text, "Bezugsgröße der alten Mittelwertkapazität fehlt")
    source = (ROOT / "report" / "main.tex").read_text(encoding="utf-8")
    source_without_urls = re.sub(r"\\(?:url|href)\{[^{}]*\}", "", source)
    require(not re.search(r"(?<!\\)%", source_without_urls), "Unmaskiertes Prozentzeichen im LaTeX-Quelltext")
    figure_numbers = [int(number) for number in re.findall(r"\\caption\{Abbildung\s+(\d+)", source)]
    table_numbers = [int(number) for number in re.findall(r"\\caption\{Tabelle\s+(\d+)", source)]
    require(not figure_numbers, f"Manuell doppelte Abbildungslabels gefunden: {figure_numbers}")
    require(not table_numbers, f"Manuell doppelte Tabellenlabels gefunden: {table_numbers}")
    labels = set(re.findall(r"\\label\{((?:fig|tab):[^}]+)\}", source))
    references = set(re.findall(r"\\ref\{((?:fig|tab):[^}]+)\}", source))
    missing_references = sorted(labels - references)
    require(not missing_references, f"Marken ohne Textverweis: {missing_references}")

    bibliography_pages = [index for index, text in enumerate(page_texts) if "Literaturverzeichnis" in text]
    require(bool(bibliography_pages), "Beginn des Literaturverzeichnisses nicht bestimmbar")
    if bibliography_pages:
        bibliography_start = bibliography_pages[0]
        main_pages = bibliography_start - 1
        back_pages = len(page_texts) - bibliography_start
        require(main_pages <= 10, f"Haupttext hat {main_pages} statt höchstens 10 Seiten")
        require(back_pages <= 5, f"Literatur und Anhang haben {back_pages} statt höchstens 5 Seiten")
        require("Zusammenfassung" in page_texts[1], "Zusammenfassung beginnt nicht nach dem Deckblatt")

    with pdfplumber.open(PDF) as pdf:
        sizes = []
        figure_sizes = []
        margin_pt = 25.0 / 25.4 * 72.0
        for index, page in enumerate(pdf.pages):
            require(abs(page.width - 595.276) < 1.0 and abs(page.height - 841.89) < 1.0, f"Seite {index + 1} ist nicht A4")
            body_chars = [char for char in page.chars if char["text"].strip()]
            if body_chars:
                min_x = min(char["x0"] for char in body_chars)
                max_x = max(char["x1"] for char in body_chars)
                min_top = min(char["top"] for char in body_chars)
                max_bottom = max(char["bottom"] for char in body_chars)
                require(min_x >= margin_pt, f"Seite {index + 1}: Inhalt links unter 25 mm")
                require(max_x <= page.width - margin_pt, f"Seite {index + 1}: Inhalt rechts über 25 mm")
                require(min_top >= margin_pt, f"Seite {index + 1}: Inhalt oben unter 25 mm")
                require(max_bottom <= page.height - margin_pt, f"Seite {index + 1}: Inhalt unten über 25 mm")
                footer_chars = [char for char in body_chars if index > 0 and char["text"] in str(index) and char["bottom"] > page.height - 40.0 / 25.4 * 72.0 and abs((char["x0"] + char["x1"]) / 2.0 - page.width / 2.0) < 5.0]
                footer_ids = {id(char) for char in footer_chars}
                for footer in footer_chars:
                    for other in body_chars:
                        if id(other) in footer_ids:
                            continue
                        overlap_x = min(footer["x1"], other["x1"]) - max(footer["x0"], other["x0"])
                        overlap_y = min(footer["bottom"], other["bottom"]) - max(footer["top"], other["top"])
                        require(overlap_x <= 0.5 or overlap_y <= 0.5, f"Seite {index + 1}: Seitenzahl überdeckt Text bei {other['text']}")
            sizes.extend(float(char["size"]) for char in body_chars if char["text"].isalpha())
            figure_sizes.extend(float(max(char["height"], char["width"])) for char in body_chars if "DejaVuSans" in char["fontname"] and char["text"].isalpha())
        if sizes:
            sizes.sort()
            median = sizes[len(sizes) // 2]
            require(11.85 <= median <= 12.15, f"Median-Schriftgröße ist {median:.2f} statt 12 pt")
        if figure_sizes:
            require(min(figure_sizes) >= 11.90, f"Diagrammschrift ist {min(figure_sizes):.2f} statt mindestens 12 pt")

    RENDER.mkdir(parents=True, exist_ok=True)
    for old_image in RENDER.glob("page-*.png"):
        old_image.unlink()
    subprocess.run(["pdftoppm", "-png", "-r", "110", str(PDF), str(RENDER / "page")], check=True, stdout=subprocess.DEVNULL)
    images = sorted(RENDER.glob("page-*.png"))
    require(len(images) == len(reader.pages), "Anzahl gerenderter Seiten weicht vom PDF ab")
    for index, path in enumerate(images):
        with Image.open(path).convert("L") as image:
            stat = ImageStat.Stat(image)
            require(stat.stddev[0] > 5.0, f"Seite {index + 1} wirkt leer oder fehlerhaft")
            require(image.width > 800 and image.height > 1100, f"Seite {index + 1} hat falsche Rendergeometrie")

    results = json.loads((ROOT / "output" / "model" / "results.json").read_text(encoding="utf-8"))
    require(results["validation"]["all_checks_passed"], "Modellvalidierung ist nicht bestanden")
    require(abs(results["baseline"]["final_cooling_mw"] - 877.781145245) < 1e-6, "Modellwert weicht vom geprüften Referenzwert ab")
    finish()


def finish() -> None:
    if ERRORS:
        for error in ERRORS:
            print(f"FEHLER: {error}")
        sys.exit(1)
    print("Berichtsprüfung bestanden: PDF, Seitenbudget, Geometrie, Inhalt, Anonymität und Renderbilder")


if __name__ == "__main__":
    main()
