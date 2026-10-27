---
name: kisa-video-kurallari
description: Kısa Video Kural Kitabı — Reels / Shorts / TikTok kurgusu için ölçülmüş kurallar (önce konuşan kafa videoları). Hangi çekimin seçileceği, kelimeye oturan kesim, akan altyazı, vurgu, zoom, konuşanın arkasına yazı, ses efektleri, müzik seviyesi, ilk 3 saniye ve bitişler; 52 viral kısa video ve 12 kurgu eğitimi videosundan çıkan sayılarla. Kısa video kurgusu planlarken, kurarken ya da incelerken yükle. Tetikleyiciler - "reels kurgula", "short yap", "altyazı ekle", "kurguma bak", "edit this reel", "short-form edit", "caption style".
---

# Kısa Video Kural Kitabı

Bu dosya kararları bir kez, gerekçesiyle verir. Her videoda kuralları baştan düşünmek yerine bunu
oku, kullanıcı yorumlarıyla güncelle. Sayılar, son 12 ayda yayınlanmış 52 viral kısa videonun
ölçümünden (Türkçe ve İngilizce, konuşan kafa ağırlıklı) ve 12 kurgu eğitimi videosundan gelir.
"Ölçüldü" yazan kural ölçümdür; "eğitimlerden" yazan kural en az 3 eğitmenin ortak iddiasıdır.

**Yaratıcı yönetmen kullanıcıdır.** İlk kurguyu kurmadan önce stratejiyi sade bir dille öner
(hangi çekimler, hook, vurgular, stil) ve onay bekle. Kendi verdiğin puan "bitti" demek değildir;
kullanıcının puanını sor.

## İş akışı (konuşan kafa)

1. **Malzemeyi oku:** kelime zamanlı transkript çıkar (ör. whisper.cpp `-ojf` ya da WhisperX).
   Cümleleri ve duraklamaları gösteren sıkıştırılmış bir metin görünümü hazırla.
2. **Sadece karar zor olan yere bak:** tekrar çekimler, uzun bir duraklama, kesim noktası.
   Videoyu baştan sona izlemek yerine o aralığın birkaç karesini ve kelime zamanlarını incele.
3. **Brief yaz:** hangi çekimler, hangi satır vurucu, hangi kelimeler vurgu. Gerisi mekanik iştir.
4. **Kur:** kendi aracınla (NLE, ffmpeg, Remotion, HyperFrames, CapCut…). Kaynak dosyalara asla yazma;
   çıktıları ayrı bir klasöre koy.
5. **Ölç ve düzelt:** render'ı aynı türden referanslarla karşılaştır (kesim sıklığı, altyazı
   yüksekliği, ses seviyesi). En pahalı farkı önce düzelt, en fazla 3 tur; sonra kalanı açıkça söyle.

## Çekim seçimi (yönetmenin işi; kod sadece kesinleştirir)

- Transkriptten seç, videoyu ileri geri sararak değil. Her cümlenin en iyi çekimi = akıcı olan,
  çoğu zaman sonraki deneme. "Eee", yarım başlangıçlar ve tekrarlanan kelimeler çıkar.
- Kesimler kelimeye oturur: ilk kelimeden ~0,12 sn önce, son kelimeden ~0,25 sn sonra; komşu bir
  kelimenin içine asla girme. Aynı akıştan kesilen iki parça boşluğun ortasında buluşur.
- Asıl noktayı söyleyen satırı **vurucu** olarak işaretle (en sıkı kadraj, varsa ses vuruşu).
- Uzunluğu malzeme belirler: konuşan kafa referansları 20–150 sn, medyan 67 sn (ölçüldü).

## Hook (ilk 3 saniye)

- Konuşma ve altyazı ilk kareden başlar; sessiz açılış planı yok. İlk kesim ~1–3 sn.
- Röportaj kesitlerinde ilk saniyelerde sabit bir soru/başlık kutusu iyi çalışır. Yerine başka bir
  şey gelmeden önce kaybolsun.
- Ölçüldü: en yaygın hook aracı bu başlık. 14 konuşan kafanın 6'sında var (6–12 sn boyunca beyaz büyük
  harfli kırmızı kutu ya da cümle düzeninde metin, beyaz hap şekli, ya da video boyu başlık).
- Ölçüldü: Türkçe videolarda ilk kesimin medyanı 3,6 sn, hook içinde kesim yok. Türkçe hook'u
  kesim değil, başlık taşıyor.
- Eğitimlerden: ilk 3 saniyede izleyici aynı anda hareket (bir itme, yerine oturan bir öğe, fiziksel
  bir eylem), ses ve ekranda hook cümlesini alır. Hook cümlesi izleyiciye seslenir ya da somut bir
  iddia/sayı verir ve sonucu ima eder. Hook'tan sonra tempo eşit kalsın; kurgunun birden seyreldiği
  bir bölüm olmasın.

## Altyazı ve vurgu

- Hücre başına 1–3 kelime. Noktalama ve ≥ 0,3 sn duraklamalarda böl; bir kesimin üstünden asla geçme.
  0,35 sn'den kısa hücre olmasın (sonraki kelimeyi içine alır). ≤ 0,25 sn boşluklarda yazı ekranda
  kalsın (yanıp sönme olmasın).
- Altyazı transkripttir: söylenmeyeni asla yazma. Sadece tanıma hatalarını düzelt.
- Vurgu ANLAMA göre seçilir (sayı, kazanç, isim), bir ritme göre değil. Tek kelime değil, bütün ifade.
  Tavan: 6–8 saniyede yaklaşık 1 vurgu.
- Ölçüldü: iyi creator'lar anahtar kelimeyi akan altyazının İÇİNDE, aynı boyutta yeniden
  renklendirir (sarı / yeşil). Sadece para rakamları büyür, yaklaşık 1,2–1,4 kat. Ayrı ve 1,5 kat büyük
  bir vurgu hücresi bütün referanslardan büyük kalır: nadir kullan, sayılara sakla.
- Görünüm: kalın, sade bir sans-serif; beyaz yazı, siyah kontur + yumuşak gölge, sert kesim.
  Vurgu: daha kalın, sıcak sarı, tek bir geri-yaylanan "pop". Renkli parlama (glow) yok.
  Açık lisanslı (OFL) fontlar seç: Montserrat, Inter, Poppins, Figtree gibi.
- Yükseklik (karenin üstünden, 0 = üst, 1 = alt): yüz merkezi + 0,26, 0,45–0,70 arasına sıkıştır.
  Ölçüldü: Hormozi 0,50; Türk creator'lar ~0,67, İngilizce konuşan kafalar 0,56, B-roll anlatım
  videoları 0,72–0,78.
- Altyazı stili video stiline uyar. Sakin uzmanlar: cümle düzeni, 4–6 kelimelik 2 satır, yumuşak gölge
  ya da beyaz hap. Yüksek enerji: 1–4 kalın kelime. Anlatım videoları: daha küçük, dar fontlu, karede
  daha aşağıda. Referanslarda satır yüksekliği karenin 0,023–0,04'ü.
- Eğitimlerden: en fazla 3 kelime, karenin alt-orta kısmı (gözler üst üçte birde), her altyazıya ses
  yok, dolgu kelime yok. Anahtar kelimeleri anlama göre renklendir (birçok editör: yeşil = olumlu,
  kırmızı = olumsuz, sarı = diğer).

## Kadraj

- Kesimde yeniden kadrajlama bir STİL seçimidir, kural değil. Ölçüldü: 8 Türkçe konuşan kafanın
  hiçbirinde ve tek kameralı sakin uzman videolarında kesimlerin %0'ı yeniden kadrajlanıyor;
  İngilizce / yüksek enerjili kurgularda %71–75 (Hormozi 0,90).
- Yüksek enerji kiti: her kesim görünür bir kadraj değişimiyle gelir: geniş 1,0 / sıkı 1,28 dönüşümlü,
  vurucu satır 1,38. 1,1'lik değişim fark edilmez. Zoom merkezi = yüz.
  En uzun 4–5 planda yavaş itme (×1,08).
- Sakin uzman kiti: sabit kadraj, yeniden kadrajsız jump cut (ya da iki kameralı geniş/sıkı kesim),
  uzun planlarda en fazla yavaş bir itme (×1,03–1,05).
- Konuşanın arkasına yazı (kişi maskesi / segmentasyon ile): videoda 1–2 kez, sadece duvardaki boş
  alana giren büyük bir vurgu kelimesi için. Maske pencerelerini kısa tut (≤ 12 sn).
- Eğitimlerden: hiçbir şey birden belirmez. Her öğe hareketle girer: hızlı giriş / yavaş çıkış, küçük
  bir yükselme + belirme + bulanıktan nete. Fotoğraf ya da ekran görüntüsü kadrajına yerleşir.
  Sabit planlara %3–10 yavaş itme.
- Eğitimlerden (göz takibi): kesim boyunca odak noktası (yüz, en yeni kart, anahtar kelime) eski yerinin
  ~%10 yakınında kalsın, özellikle hook'ta. Sadece bilerek boz.

## Ses

- Önce ses (konuşma). Efektler sadece görünen bir şeye bağlıdır (bir kesim, yerine oturan bir vurgu).
- Kesimde efekt stile bağlıdır. Ölçüldü (stem ayrıştırmasıyla): 14 iyi konuşan kafanın 8'i HİÇBİR
  kesime efekt koymuyor (Hormozi: %12, şans seviyesi %21). B-roll ve yüzsüz anlatım videoları görsel
  değişimlerin %20–80'ine whoosh / vuruş koyuyor (şansın çok üstünde). Yüksek enerjili creator'lar sesi
  kesime değil grafik olaylara bağlıyor (sayaç, sıralamaya yerleşen öğe).
  Not: karışık sesteki ani yükselmeler konuşmada zaten saniyede ~4 kez olur; efekt saymak için
  karışık sesi değil, ayrıştırılmış stem'i ölç.
- Vurguya darbe sesi sadece yüksek enerji kitinde.
- Seviyeler, konuşmanın p95 tepesine göre: arayüz/pop −14 dB, whoosh −12 dB, darbe −8 dB, meme sesi −3 dB.
  Kabaran sesler tepesini kesime, vuruşlar başlangıcını kesime denk getirir.
  10 saniyede en fazla 4,5 efekt, aralarında ≥ 0,25 sn.
- Meme sesi asla bir kelimenin üstüne gelmez.
- Teslim: −14 LUFS, true peak ≤ −1 dBTP (ölç, tahmin etme).
- Müzik. Ölçüldü: 14 iyi konuşan kafanın 7'sinde müzik yatağı YOK. Olanlarda müzik konuşmanın yaklaşık
  16 LU altında (medyan, entegre); yüksek enerji yatakları daha sıcak (10–12 LU altında), anlatım
  videoları 16–22 LU altında. Müziksiz sürümü yedek değil, gerçek bir seçenek olarak sun.
- Eğitimlerden: büyük bir harekette (zoom, kayma, whip, sahne değişimi) efektin TEPESİ hareketin
  tepesine oturur. Hafif tık / arayüz sesleri yazı ve ikon pop'larına. Riser sadece gerçekten bir
  açılış geliyorsa (sonuca giriş), anahtar satırdan hemen sonra bir vuruş. Az kullanılırsa anlamını
  korur. Müziğin bir görevi var: konuşmanın 15–25 dB altında durur, dönüm noktasında (sorun → çözüm)
  yükselir, bitişi haber vermek için kısılır.

## Bitişler ve geçişler (saha geri bildirimi)

- Konuşan devam ederken bitirme ("o yüzden", "çünkü", sonraki kelime < 0,7 sn sonra): düşüncenin
  sonuna kadar uzat. Son parça görüntü + sesle 0,6 sn'de kararır.
- Geçiş sesi yumuşak bir whoosh: alçak frekans, sert atak yok, konuşmaya göre −18 dB.
- Uzun planları kelime boşluklarında jump-zoom parçalarına böl (≤ 4,2 sn, hook'ta ≤ 2,6 sn); bir vurgu
  ifadesinin içinde asla bölme. Bu kesimlere whoosh konmaz.
- Eğitimlerden: büyük geçişler sadece büyük anlarda (bölüm ya da mekân değişimi). Diğer her yerde düz
  kesim + J/L ses.

## Yoğunluk

- Kurgu içeriği destekler, yıldız olmaz. Sakin ya da kişisel bir konuşma daha az kesim ve efekt alır;
  kesmek için kesme. İlginç bir plan uzun kalabilir.
- Kesim sıklığı türe özgüdür: yoğun grafikli tek planlık kısa videolar (MrBeast, Zach King) neredeyse
  hiç kesim yapmadan kazanır. Sadece aynı türle karşılaştır.
- Yapay zekâ ajanları az keser ve fazla iddia eder: neyin doğrulanmadığını açıkça söyle.

## Yasaklar

- Kelime içinde kesim; yüzün ya da konunun üstüne binen altyazı; kesimin üstünden geçen altyazı.
- Her kesimde whoosh; konuşmadan yüksek efekt (bilinçli bir meme sesi hariç).
- Şablonda kalmış yer tutucu metin ("Metninizi buraya girin"): her zaman doldur ve geri oku.
- Yazıda renkli parlama; sonraki sahne geldiğinde hâlâ ekranda duran yazı.
- Bir referansın görüntüsünü ya da sesini kurguya koymak (referanslar sadece ölçüm içindir).

## Stil kitleri (özet)

| Kit | Kesimde kadraj | Kesimde efekt | Altyazı | Müzik |
|---|---|---|---|---|
| Sakin uzman | yok (ya da iki kamera) | yok | cümle düzeni, 2 satır, 4–6 kelime | yok ya da ~16 LU altında |
| Yüksek enerji | her kesimde 1,0 / 1,28, vurucu 1,38 | grafik olaylara bağlı, vurguya darbe | 1–4 kalın kelime, sayılar büyür | 10–12 LU altında |
| B-roll anlatım | — | görsel değişimlerin %20–80'i | küçük, dar, aşağıda (0,72–0,78) | 16–22 LU altında |
| Türkçe konuşan kafa | yok | yok | ~0,67 yükseklik, başlık kutusu hook'u | çoğu zaman yok |
