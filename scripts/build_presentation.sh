#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
.venv/bin/python model/run_all.py
cd presentation
tectonic main.tex --outdir ../output/presentation
cd ..
mv output/presentation/main.pdf output/presentation/Blautopf_Finale.pdf
mkdir -p tmp/presentation_pages
pdftoppm -png -r 150 output/presentation/Blautopf_Finale.pdf tmp/presentation_pages/slide >/dev/null 2>&1
.venv/bin/python scripts/build_video.py "$@"
.venv/bin/python scripts/record_playback.py
.venv/bin/python scripts/verify_presentation.py
