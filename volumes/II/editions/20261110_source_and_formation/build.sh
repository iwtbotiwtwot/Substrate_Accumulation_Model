#!/usr/bin/env bash
set -euo pipefail
edition_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
build_dir="$edition_dir/tmp/pdfs/build"
mkdir -p "$build_dir" "$edition_dir/pdf" "$edition_dir/qa"
cd "$edition_dir/src"
for pass in 1 2 3; do
  xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" main.tex > "$edition_dir/qa/xelatex-pass-$pass.txt" 2>&1
done
cp "$build_dir/main.pdf" "$edition_dir/pdf/SAM_Volume_II_Revised_Edition_20261110.pdf"
cp "$build_dir/main.log" "$edition_dir/qa/latex-final.log"
cp "$build_dir/main.toc" "$edition_dir/qa/contents.tex"
printf 'Built %s\n' "$edition_dir/pdf/SAM_Volume_II_Revised_Edition_20261110.pdf"
