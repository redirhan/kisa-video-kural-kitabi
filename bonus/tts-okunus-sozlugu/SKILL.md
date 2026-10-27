---
name: tts-okunus-sozlugu
description: Türkçe seslendirme (TTS) metnini göndermeden önce kısaltma, yabancı özel ad ve birimleri doğru Türkçe okunuşa çevirir (DNA → de ne a, Watson → vatsın, 5 mg → 5 miligram); 181 terimlik sözlük + respell.py. Türkçe seslendirme, anlatım videosu, sesli özet ya da TTS metni hazırlarken yükle. Tetikleyiciler - "seslendir", "TTS", "okunuşu düzelt", "Turkish voiceover pronunciation".
---

# Türkçe TTS okunuş sözlüğü

1. Ekranda / altyazıda gösterilecek metni olduğu gibi bırak.
2. Sadece TTS'e gidecek kopyayı düzelt:
   `python3 ~/.claude/skills/tts-okunus-sozlugu/respell.py "metin"` (ya da `-` ile stdin).
3. Seslendirmeden sonra mümkünse whisper ile geri yazıya dök; terim, `glossary_tr.tsv`'nin son
   sütunundaki kabul edilen biçimlerden biri olarak çıkmalı. Çıkmadıysa 5. sütundaki alternatif
   okunuşu dene.
4. Sözlükte olmayan bir terimle karşılaşırsan aynı biçimde yeni satır öner; kullanıcıya hangi
   okunuşu seçtiğini söyle.

Ayrıntılar: `KULLANIM.md`. Sütunlar ve türler sözlük dosyasının başında yazılı.
