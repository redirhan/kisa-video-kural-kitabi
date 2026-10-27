# Türkçe TTS okunuş sözlüğü: kısa kullanım notu

Türkçe seslendirme motorları (TTS) kısaltmaları, yabancı özel adları ve birimleri çoğu zaman yanlış
okur: "DNA" İngilizce harflenir, "Watson" yazıldığı gibi okunur, "5 mg" "5 mg" diye geçer. Bu sözlük
181 terimin doğru Türkçe okunuşunu verir: biyoloji, sağlık, kimya, fizik, matematik, mühendislik,
ekonomi ve psikoloji.

**Altın kural: ekranda yazılış kalır, TTS'e sadece okunuş gider.** Altyazıda "DNA" yazar, ses
"de ne a" der.

## Sütunlar (TAB ile ayrılmış)

| Sütun | Örnek | Not |
|---|---|---|
| yazılış | `CRISPR-Cas9` | metinde aranan biçim |
| okunuş | `krispır kas dokuz` | TTS'e giden metin |
| tür | `abbr` / `name` / `term` / `unit` / `translate` | abbr ve unit büyük/küçük harfe duyarlıdır; unit sadece sayıdan sonra |
| alan | `bio`, `health`, `chem`, `phys`, `math`, `eng`, `econ`, `psy`, `sci` | filtrelemek için |
| alternatif okunuşlar | `krisper kas dokuz` | motor ilkini beceremezse dene |
| whisper'da kabul edilenler | `crispr cas9\|krispır kas dokuz` | sesi geri yazıya döküp kontrol ederken doğru sayılacak biçimler |

## Kullanım

```bash
python3 respell.py "DNA'nın yapısını Watson ve Crick buldu; 5 mg yeterli."
# -> de ne a'nın yapısını vatsın ve krik buldu; 5 miligram yeterli.
python3 respell.py --check     # sözlük biçimini ve tekrar eden terimleri kontrol eder
```

Kendi kodunda: `from respell import respell` ve TTS'e göndermeden önce metni `respell(metin)`'den geçir.
Claude Code'da: "seslendirme metnini bonus/tts-okunus-sozlugu/glossary_tr.tsv ile düzelt" demen yeterli.

**Kontrol döngüsü (önerilir):** seslendir → whisper ile geri yazıya dök → son sütundaki kabul edilen
biçimlerden biri çıktı mı bak. Çıkmadıysa alternatif okunuşu dene.

Yeni terim eklemek: bir satır ekle, `--check` çalıştır, bir cümlede dene. Okunuşlar kulakla
hazırlandı; motorlar farklı olduğu için kendi motorunda dinleyip gerekirse düzelt.
