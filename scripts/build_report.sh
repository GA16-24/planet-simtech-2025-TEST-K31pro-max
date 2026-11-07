#!/usr/bin/env bash
set -euo pipefail
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-1794009600}"
cd "$(dirname "$0")/.."
.venv/bin/python model/run_all.py
cd report
tectonic main.tex --outdir ../output/pdf
cd ..
mv output/pdf/main.pdf output/pdf/TEST-K31pro-max.pdf
.venv/bin/python scripts/verify_report.py
