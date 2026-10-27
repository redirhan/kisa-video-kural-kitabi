# Kısa Video Kural Kitabı (ücretsiz Claude Code skill paketi)

Reels, Shorts ve TikTok kurgusu için **ölçülmüş** kurallar. "Bence böyle güzel olur" değil: 52 viral
kısa videonun ölçümünden ve 12 kurgu eğitiminin ortak noktalarından çıkan sayılar. Claude Code'a
yüklediğinde, kısa video planlarken, kurarken ya da incelerken bu kurallarla çalışır.

Redirhan Studio tarafından hazırlandı. Ücretsiz, MIT lisanslı.

## İçinde ne var

| Klasör | Ne işe yarar |
|---|---|
| `skills/kisa-video-kurallari/` | Kurgu kural kitabı: çekim seçimi, kelimeye oturan kesim, altyazı boyu ve yüksekliği, vurgu, zoom, ses efekti ve müzik seviyeleri, ilk 3 saniye, bitişler, yasaklar, 4 stil kiti |
| `skills/referanstan-konsepte/` | "Bunun gibisini yap" protokolü: referans videoyu indir, ölç, plan plan 5 açıdan ayrıştır, 2–3 konsept öner, önce 10–15 sn örnek yap, "slayt gösterisi riski" kontrolü |
| `bonus/tts-okunus-sozlugu/` | 181 terimlik Türkçe seslendirme okunuş sözlüğü (DNA → de ne a, Watson → vatsın, 5 mg → 5 miligram) + `respell.py` |

Birkaç örnek sayı:
- Türkçe konuşan kafa videolarında altyazı karenin ~0,67 yüksekliğinde (İngilizcede 0,56).
- Türkçe videolarda ilk kesimin medyanı 3,6 sn: hook'u kesim değil başlık kutusu taşıyor.
- İyi konuşan kafa videolarının yarısında müzik yok; olanlarda müzik sesin ~16 LU altında.
- 14 iyi konuşan kafanın 8'i hiçbir kesime ses efekti koymuyor.

## Kurulum

```bash
mkdir -p ~/.claude/skills
cp -R skills/kisa-video-kurallari skills/referanstan-konsepte ~/.claude/skills/
cp -R bonus/tts-okunus-sozlugu ~/.claude/skills/        # isteğe bağlı
```

Claude Code'u yeniden başlat. Sonra örneğin: *"Bu konuşma videosundan 45 saniyelik bir reels planla"*,
*"Şu reels'e bak, bunun gibisini kafem için yapalım: <link>"* ya da *"Bu seslendirme metnini düzelt"*.
Skill'ler kendiliğinden yüklenir.

Gerekenler: kural kitabı sadece metindir. Referans protokolündeki ölçümler için `yt-dlp`, `ffmpeg` ve
isteğe bağlı olarak whisper (ör. whisper.cpp) önerilir. Sözlük yardımcısı sadece Python 3 ister.

## Daha fazlası: Panel TR

Kurgunu yayınlamadan önce Türk izleyicinin gözünden test etmek istersen: **Panel TR**, yaşa, şehre ve
Instagram kullanımına göre ayrılmış, kanıta dayalı Türk personalardan oluşan bir sentetik odak grubu.
"Kaçı durur, kaçı geçer, kaçı DM atar?" sorusunu sayılarla cevaplar. → ücretsiz Lite sürümü: https://github.com/redirhan/panel-tr-lite

## Lisans

MIT, bkz. `LICENSE`. Referans protokolünün fikri OpenMontage'dan (AGPL-3.0) ilham alır; o projeden kod
alınmadı.
