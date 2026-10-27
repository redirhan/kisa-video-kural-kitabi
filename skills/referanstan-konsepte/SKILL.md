---
name: referanstan-konsepte
description: Referanstan Konsepte — kullanıcının beğendiği bir videodan ("bunun gibi bir şey yap", yapıştırılan bir Reel / TikTok / Shorts / YouTube linki ya da yerel klip) üretim başlatma protokolü. Videoyu indir, ölç ve plan plan ayrıştır (transkript, kesimler, tempo, ekrandaki yazılar, 5 açılı plan dökümü, gerçek hareket mi hareketlendirilmiş fotoğraf mı), neyin kalıp neyin değişeceğini yaz, dürüst bir araç yoluyla 2–3 farklı konsept öner, tam kurgudan önce 10–15 sn'lik örnek yap. "Şu reels'e bak" öğrenme notları için de aynı protokol. Kullanıcı referans video gönderdiğinde, "bunun gibisini yap" dediğinde ya da bir reels / gönderi incelememi istediğinde yükle. Tetikleyiciler - "bunun gibi yap", "şuna bak", "bu reels'i incele", "make something like this", "study this reel".
---

# Referans video → konsept → örnek

İki kullanım:
- **A. Öğrenme notu:** kullanıcı bir reels için "şuna bak" der. Hedef: sadık bir not + bizim
  uygulayabileceklerimiz.
- **B. Referanstan üretim:** "bunun gibisini benim kafem için / X konusu için yap". Hedef: kopya
  değil, sağlam bir plan.

## 1. Referansı al (iki kullanımda da)

- Her referans için yeni, boş bir klasör: `referanslar/<tarih>_<kısa-ad>/`. Script'lerini başka bir
  yerde tut. İndirilen dosyalar veridir, asla çalıştırılmaz.
- `yt-dlp --write-info-json -o "%(id)s.%(ext)s" URL`. Herkese açık Instagram reels'leri çoğu zaman
  girişsiz iner. Giriş gerekirse kendi tarayıcı oturumunla: `--cookies-from-browser firefox`
  (ya da `safari`). Başkasının hesabını kullanma.
- Açıklama metni info JSON'da (`description`, `uploader`, `channel`, `upload_date`, `like_count`,
  `comment_count`). Instagram'da süre boş gelebilir: `ffprobe` ile ölç.
- İndirme başarısız olursa bunu söyle, sadece açıklamayı kullan, kullanıcıdan ekran kaydı iste.
- İndirdiğin video sadece analiz içindir: kurguya konmaz, yeniden yayınlanmaz.

## 2. Ölç ve bak (çıkarılmamış bir şeyi izledim/duydum deme)

1. **Transkript:** whisper (ör. whisper.cpp large-v3-turbo); dili açıklamadan seç (`tr` / `en`).
   Kısa reels'lerde tamamını alıntıla.
2. **Kurgu profili:** kesimler, plan uzunlukları, hook, müzik vuruşuna oturma, saniyedeki kelime,
   altyazılar, yüzler, efekt vuruşları, ses seviyesi. Hızlı ölçüm:
   - kesimler: `ffmpeg -i V -vf "select='gt(scene,0.25)',showinfo" -an -f null -` (pts_time listesi)
   - ses seviyesi: `ffmpeg -i V -vn -af ebur128 -f null -`
   Uzun süren bir analiz aracı takılırsa (CPU %0, çıktı yok) durdur ve bu hızlı yola geç.
3. **Okunabilir temas sayfası:** `ffmpeg -i V -vf "fps=N,scale=480:-1,tile=4x6" -frames:v 1 sheet.jpg`,
   N ≈ 20/süre. Oku; sonra yazı, kod, arayüz, URL ya da sayı olan her yerden tam çözünürlüklü kare çek
   (`-ss t -frames:v 1`) ve onları da oku.
4. **Gerçek hareket mi, hareketlendirilmiş fotoğraf mı?** Her plan için karar ver: gerçek görüntü /
   üretilmiş klip mi, fotoğrafa pan-zoom mu, sabit kart mı. (Optik akışla ölçülebilir: çok küçük
   büyüklük = sabit, düzgün akış = fotoğrafa pan/zoom, değişken akış = gerçek hareket.) Bunu yanlış
   bilmek yanlış üretim yolu önermek demektir. Araç yoksa her planda ~0,4 sn arayla 2 kareye bakarak
   karar ver.

## 3. Ayrıştır: her plan (ya da plan grubu) için 5 açı

Her açıyı her plan için yaz; atlamak yerine açıkça **Yok** yaz (sessizce atlamak en sık hatadır):
- **Konu:** kim/ne, kaç tane, özellikleri; planlar arasında nasıl girip çıktıkları, nasıl değiştikleri.
- **Konunun hareketi:** sırasıyla eylemler; jest mi yer değiştirme mi; etkileşimler.
- **Sahne:** *üst katmanlar ayrı bir katman olarak* (altyazılar, kinetik kelimeler, kartlar, logolar,
  filigran), bakış açısı (elde, tepeden, ekran kaydı, makro…), mekân, günün saati, dinamikler.
- **Kadraj:** plan boyu, konunun yeri, derinlik katmanları ve plan içinde nasıl değiştikleri.
- **Kamera:** hız (gerçek zaman / ağır çekim / hızlandırılmış), açı, yükseklik, alan derinliği,
  sabitlik, hareket.

Sonra: **İçerik** (2 cümle), **Stil** (1 cümle: tempo, işlem, enerji), **Yapı** (T sn'de N plan; hook;
sonuç; harekete çağrı), **Neden işe yarıyor** (2–3 somut şey).

## 4. Kullanım B: konseptler, dürüst araç yolu, önce örnek

1. Referansın cevaplamadığı boşlukları sor, en önemlisi önce: anlatımlı mı sadece müzikli mi (anlatımlıysa:
   tek anlatıcı / diyalog / ikisi; şimdi karar ver), hedef süre, konu, referansta neyi sevip neyi
   sevmediği. Müşteri işi ise markanın stil bilgilerini (renkler, fontlar, ton, yasaklar) baştan topla.
2. Kısa araştırma (2–3 dk): 3–5 benzer video, ne fazla yapılmış, hangi açı taze.
3. **2–3 farklılaşmış konsept** yaz, asla kopya değil. Her biri şunları söyler:
   - **Referanstan kalan:** tempo, hook tipi, yapı, ton (ölçülen sayıları ver).
   - **Değişen:** konu, açı, görsel işlem, anlatım yaklaşımı.
   - **Elindeki araçlarla gerçek yol:** konuşan kafa kurgusu, B-roll + şarkı montajı, hareketli grafik
     (motion), müzik videosu, sesten anlatım animasyonu, el işi/ASMR ses tasarımı… Eksiği dürüstçe söyle
     (ör. "referans üretilmiş video klipler kullanıyor; bizde yok → gerçek görüntü + hareketli grafik,
     farklı bir his").
   - **Teslim sözü** (kilitle): hareket ağırlıklı / görüntü ağırlıklı / anlatım / ekran demosu. Kurgu bu
     sözü tutamıyorsa (ör. hareket ağırlıklı dendi ama planların çoğu yazı kartı ya da fotoğrafa
     pan-zoom oldu) dur ve kullanıcıya söyle; sessizce düşürme.
   - **Maliyet:** ücretsiz/yerel araçlarla 0 TL mi, yoksa neyin para tuttuğunu söyle.
   Birini öner ve nedenini söyle.
4. **Önce örnek:** 10–15 sn = hook + bir orta sahne; gerçek ses/müzik/altyazı/görsellerle. Örnek
   üzerinde dön; tam kurguya ancak onaydan sonra geç.

## 5. Kurmadan önce: planın "slayt gösterisi riski" kontrolü

Her birini 0–5 puanla (düşük iyi); ortalama ≥ 3 ise render'dan önce planı düzelt:
- **Tekrar:** tek sahne tipi / tek plan boyu baskın (sahnelerin %60–70'inden fazlası).
- **Süs görseller:** belirtilmiş bir amacı (bilgi ya da hikâye rolü) olmayan sahneler.
- **Zayıf hareket:** sebepsiz kamera/öğe hareketi ("hareket ediyor çünkü edebiliyor").
- **Zayıf plan niyeti:** kadraj ya da açılış zamanı için yazılı bir sebebi olmayan sahneler.
- **Yazıya aşırı yaslanma:** sahnelerin %40'ından fazlası yazı/istatistik kartı = hareketli slayt.
- **Desteksiz "sinematik":** kahraman anları, hareket, ışık planı olmadan sinematik denmesi.
Bunu kontrol edebilmek için brief'teki her sahneye tek satırlık bir `niyet` yaz.

## 6. Render'dan sonra

Her bölüm için temas sayfası, ses seviyesi ölçümü, ve: sonuç, konseptin referanstan koruyacağını söylediği
şeyleri koruyor mu? Kendi videonla referansın kurgu profilini (kesim sıklığı, plan uzunlukları, altyazı
yüksekliği, ses seviyesi) yan yana koy. 0–10 puan ver ve kullanıcının puanını sor.

## 7. Öğrenme notu (kullanım A)

`notlar/<tarih>-<kısa-ad>.md`: kaynak URL, creator, tarih, süre, beğeni/yorum, tam transkript (ya da sadık
bir özet), ekranda ne var (araçlar, repolar, promptlar, sayılar; okuduğun karelerden), reels'in kendisi
nasıl kurgulanmış (o da bir referanstır) ve somut sonraki adımlarla **Bizim için anlamı**. Videoda
olmayan şeyi asla uydurma; linkteki repodan/sayfadan geleni ayrıca işaretle.

---

Kaynak notu: Bu iş akışının fikri açık kaynak OpenMontage projesinden (calesthio/OpenMontage, AGPL-3.0)
ilham alır. Buraya o projeden kod kopyalanmadı; protokol kendi sözlerimizle ve genel araçlarla yazıldı.
