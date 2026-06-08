# Scripts

## `build_kilavuz_pdf.sh`

`CALISTIRMA_KILAVUZU.txt` ve `WEB_KULLANIM_KITAPCIGI.txt` dosyalarından PDF üretir.

### Kurulum (macOS, bir kez)

```bash
brew install pandoc basictex
```

Kurulumdan sonra terminali yeniden açın.

### Kullanım

```bash
cd project
chmod +x scripts/build_kilavuz_pdf.sh   # ilk seferde
./scripts/build_kilavuz_pdf.sh
```

Çıktılar: `project/docs/`

| Dosya | Kaynak |
|-------|--------|
| `CALISTIRMA_KILAVUZU.pdf` | Kurulum ve çalıştırma |
| `WEB_KULLANIM_KITAPCIGI.pdf` | Web arayüzü kullanımı |
| `CEM501_KILAVUZ_TAM.pdf` | İki kılavuz birleşik |

Seçenekler: `--calistirma`, `--web`, `--combined`, `--help`
