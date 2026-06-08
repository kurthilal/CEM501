#!/usr/bin/env bash
# CEM501 kılavuz .txt dosyalarından PDF üretir.
# Gereksinim: pandoc + LaTeX (macOS: brew install pandoc basictex)
#
# Kullanım (project/ klasöründen):
#   ./scripts/build_kilavuz_pdf.sh
#   ./scripts/build_kilavuz_pdf.sh --calistirma
#   ./scripts/build_kilavuz_pdf.sh --web
#   ./scripts/build_kilavuz_pdf.sh --combined

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="${ROOT}/docs"
CALISTIRMA="${ROOT}/CALISTIRMA_KILAVUZU.txt"
WEB="${ROOT}/WEB_KULLANIM_KITAPCIGI.txt"

BUILD_CALISTIRMA=0
BUILD_WEB=0
BUILD_COMBINED=0

usage() {
  cat <<'EOF'
CEM501 kılavuz PDF oluşturucu

Kullanım:
  ./scripts/build_kilavuz_pdf.sh              Tüm PDF'leri üret (varsayılan)
  ./scripts/build_kilavuz_pdf.sh --calistirma Sadece CALISTIRMA_KILAVUZU.pdf
  ./scripts/build_kilavuz_pdf.sh --web        Sadece WEB_KULLANIM_KITAPCIGI.pdf
  ./scripts/build_kilavuz_pdf.sh --combined   Sadece birleşik CEM501_KILAVUZ_TAM.pdf
  ./scripts/build_kilavuz_pdf.sh --help

Çıktı klasörü: project/docs/

Gereksinimler (macOS):
  brew install pandoc basictex

İlk kurulumdan sonra terminali yeniden açın veya:
  eval "$(/usr/libexec/path_helper)"

EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --calistirma) BUILD_CALISTIRMA=1 ;;
    --web) BUILD_WEB=1 ;;
    --combined) BUILD_COMBINED=1 ;;
    --help|-h) usage; exit 0 ;;
    *)
      echo "Bilinmeyen seçenek: $1" >&2
      usage
      exit 1
      ;;
  esac
  shift
done

if [[ "$BUILD_CALISTIRMA" -eq 0 && "$BUILD_WEB" -eq 0 && "$BUILD_COMBINED" -eq 0 ]]; then
  BUILD_CALISTIRMA=1
  BUILD_WEB=1
  BUILD_COMBINED=1
fi

require_file() {
  if [[ ! -f "$1" ]]; then
    echo "Dosya bulunamadı: $1" >&2
    exit 1
  fi
}

require_file "$CALISTIRMA"
require_file "$WEB"

if ! command -v pandoc >/dev/null 2>&1; then
  cat >&2 <<'EOF'
Hata: pandoc yüklü değil.

macOS:
  brew install pandoc basictex

Kurulumdan sonra terminali yeniden açın ve scripti tekrar çalıştırın.
EOF
  exit 1
fi

pick_pdf_engine() {
  if command -v xelatex >/dev/null 2>&1; then
    echo "xelatex"
  elif command -v pdflatex >/dev/null 2>&1; then
    echo "pdflatex"
  elif command -v lualatex >/dev/null 2>&1; then
    echo "lualatex"
  else
    cat >&2 <<'EOF'
Hata: LaTeX PDF motoru bulunamadı (xelatex / pdflatex / lualatex).

macOS:
  brew install basictex

Kurulumdan sonra terminali yeniden açın.
EOF
    exit 1
  fi
}

PDF_ENGINE="$(pick_pdf_engine)"
mkdir -p "$OUT_DIR"

build_one() {
  local src="$1"
  local dest="$2"
  echo "→ $(basename "$dest")"
  pandoc "$src" \
    -o "$dest" \
    --pdf-engine="$PDF_ENGINE" \
    -V lang=tr \
    -V geometry:margin=2.5cm \
    -V fontsize=11pt \
    -V documentclass=article \
    -V colorlinks=true \
    -V linkcolor=NavyBlue
}

build_combined() {
  local dest="${OUT_DIR}/CEM501_KILAVUZ_TAM.pdf"
  echo "→ $(basename "$dest")"
  pandoc "$CALISTIRMA" "$WEB" \
    -o "$dest" \
    --pdf-engine="$PDF_ENGINE" \
    -V lang=tr \
    -V geometry:margin=2.5cm \
    -V fontsize=11pt \
    -V documentclass=article \
    -V colorlinks=true \
    -V linkcolor=NavyBlue
}

echo "PDF motoru: $PDF_ENGINE"
echo "Çıktı: $OUT_DIR"
echo

if [[ "$BUILD_CALISTIRMA" -eq 1 ]]; then
  build_one "$CALISTIRMA" "${OUT_DIR}/CALISTIRMA_KILAVUZU.pdf"
fi

if [[ "$BUILD_WEB" -eq 1 ]]; then
  build_one "$WEB" "${OUT_DIR}/WEB_KULLANIM_KITAPCIGI.pdf"
fi

if [[ "$BUILD_COMBINED" -eq 1 ]]; then
  build_combined
fi

echo
echo "Tamamlandı."
ls -lh "$OUT_DIR"/*.pdf 2>/dev/null || true
