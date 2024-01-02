# Encryption
Welcome 2024 GitHub 

Shifrlash nima?
Shifrlash ma'lumotlarni o'g'irlash, o'zgartirish yoki buzishdan himoya qilish uchun ishlatiladi va ma'lumotlarni faqat noyob raqamli kalit bilan ochish mumkin bo'lgan maxfiy kodga aylantirish orqali ishlaydi.

Shifrlangan ma'lumotlar kompyuterlarda ishlayotganda yoki ular o'rtasida o'tish paytida yoki qayta ishlanayotganda, bu kompyuterlar mahalliy yoki masofaviy bulutli serverlar bo'lishidan qat'i nazar himoyalanishi mumkin.

![what-is-encryption](https://github.com/themusharraf/Encryption/assets/122869450/aafe97e4-d1bb-49bd-b88d-56c47ec95fdf)

Eng asosiy darajada shifrlash ma'lumot yoki ma'lumotni matematik modellar yordamida himoyalash jarayoni bo'lib, uni ochish uchun kalitga ega bo'lgan tomonlargina unga kirishi mumkin bo'ladi. Bu jarayon juda oddiydan juda
murakkabgacha bo'lishi mumkin va matematiklar va kompyuter olimlari iste'molchilar va korxonalar har kuni tayanadigan ma'lumotlar va ma'lumotlarni himoya qilish uchun ishlatiladigan shifrlashning o'ziga xos shakllarini ixtiro qildilar.

![difference-between-encryption-and-signing](https://github.com/themusharraf/Encryption/assets/122869450/7c873e4f-e99f-4625-abfb-68e6b773736b)
# Shifrlash qanday ishlaydi

![how-encryption-works](https://github.com/themusharraf/Encryption/assets/122869450/d3fcba0b-63f7-4672-aea4-a47cc2abe4c8)

Shifrlash "to'g'ri matn" ni "shifrlangan matn" ga kodlash orqali ishlaydi, odatda algoritmlar deb nomlanuvchi kriptografik matematik modellardan foydalanish orqali. Ma'lumotni ochiq matnga qaytarish uchun shifrni ochish kaliti, raqamlar qatori yoki algoritm tomonidan yaratilgan paroldan foydalanish talab etiladi. Xavfsiz shifrlash usullari shunchalik ko'p kriptografik kalitlarga egaki, ruxsatsiz shaxs na qaysi biri to'g'ri ekanligini taxmin qila olmaydi, na har bir potentsial kombinatsiyani (qo'pol kuch hujumi sifatida tanilgan) sinab ko'rish orqali to'g'ri belgilar qatorini hisoblash uchun kompyuterdan foydalana olmaydi.

Oddiy shifrlashning dastlabki namunalaridan biri Rim imperatori Yuliy Tsezar nomi bilan atalgan "Tsezar shifridir", chunki u shaxsiy yozishmalarida undan foydalangan. Usul almashtirish shifrining bir turi bo'lib, unda bir harf boshqa harf bilan almashtiriladi, alifbo bo'ylab ma'lum miqdordagi pozitsiyalar. Kodlangan matnning shifrini ochish uchun qabul qiluvchi alifboni to'rtta joyga pastga va chapga siljitish kabi shifr kalitini bilishi kerak ("chapga to'rt siljish"). Shunday qilib, har bir "E" "Y" ga aylanadi va hokazo.

Zamonaviy kriptografiya ancha takomillashgan boʻlib, shifrni ochish kalitlari sifatida kompyuterda yaratilgan yuzlab (hatto minglab, baʼzi hollarda) belgilar qatorlaridan foydalanadi.

# Shifrlash turlari

![Asymmetric-vs-Symmetric](https://github.com/themusharraf/Encryption/assets/122869450/a5531df7-2d6a-45c0-a8a1-8445de030c96)


Shifrlash algoritmlarining eng keng tarqalgan ikkita turi nosimmetrik va assimetrikdir.
Umumiy kalit yoki shaxsiy kalit algoritmi sifatida ham tanilgan simmetrik shifrlash shifrlash va shifrni ochish uchun bir xil kalitdan foydalanadi. Simmetrik kalit shifrlarini ishlab chiqarish arzonroq hisoblanadi va shifrlash va shifrni ochish uchun unchalik ko'p hisoblash quvvatini talab qilmaydi, ya'ni ma'lumotlarni dekodlashda kechikish kamroq bo'ladi.

Kamchilik shundaki, agar ruxsatsiz shaxs kalitga qo'l tegsa, ular tomonlar o'rtasida yuborilgan har qanday xabar va ma'lumotlarning shifrini ochishi mumkin bo'ladi. Shunday qilib, umumiy kalitni uzatish boshqa kriptografik kalit bilan shifrlanishi kerak, bu esa qaramlik davriga olib keladi.

Ochiq kalitli kriptografiya sifatida ham tanilgan assimetrik shifrlash ma'lumotlarni shifrlash va shifrini ochish uchun ikkita alohida kalitdan foydalanadi. Ulardan biri shifrlash uchun barcha tomonlar o'rtasida taqsimlangan ochiq kalitdir. Ochiq kalitga ega bo'lgan har bir kishi shifrlangan xabarni yuborishi mumkin, lekin faqat ikkinchi, shaxsiy kalit egalari xabarning shifrini ochishi mumkin.

Asimmetrik shifrlash ishlab chiqarish qimmatroq hisoblanadi va shifrni ochish uchun ko'proq hisoblash quvvati talab qilinadi, chunki ommaviy shifrlash kaliti odatda katta, 1024 dan 2048 bitgacha. Shunday qilib, assimetrik shifrlash ko'pincha katta ma'lumotlar paketlari uchun mos kelmaydi.

# Umumiy shifrlash algoritmlari

![1671128975482](https://github.com/themusharraf/Encryption/assets/122869450/a8c96672-0ec3-4e9e-8d61-e40865ef0642)


Simmetrik shifrlashning eng keng tarqalgan usullariga quyidagilar kiradi:

Ma'lumotlarni shifrlash standarti (DES): 1970-yillarning boshida ishlab chiqilgan shifrlash standarti bo'lib, DES 1977 yilda AQSh hukumati tomonidan qabul qilingan. DES kaliti hajmi atigi 56 bit bo'lib, uni bugungi texnologiya ekotizimida eskirgan. Aytish joizki, bu zamonaviy kriptografiyaning rivojlanishiga ta'sir ko'rsatdi, chunki kriptograflar uning nazariyalarini takomillashtirish va ilg'or shifrlash tizimlarini yaratish ustida ishladilar.

Triple DES (3DES): DESning navbatdagi evolyutsiyasi DES shifrlash blokini oldi va uni shifrlash, shifrini ochish va keyin yana shifrlash orqali shifrlangan har bir ma'lumot blokiga uch marta qo'lladi. Usul kalit hajmini oshirdi, bu qo'pol kuch hujumi bilan shifrni ochishni ancha qiyinlashtirdi. Biroq, 3DES hanuzgacha xavfli hisoblanadi va 2023 yildan boshlab barcha dasturiy ilovalar uchun AQSh Milliy Standartlar Instituti (NIST) tomonidan eskirgan.

Kengaytirilgan shifrlash standarti (AES): Bugungi kunda eng ko'p qo'llaniladigan shifrlash usuli, AES 2001 yilda AQSh hukumati tomonidan qabul qilingan. U 128 bit blokli shifr bo'lgan va kalitlarga ega bo'lishi mumkin bo'lgan "almashtirish-o'zgartirish tarmog'i" deb nomlangan printsip asosida ishlab chiqilgan. 128, 192 yoki 256 bit uzunlikda.

Twofish: Uskuna va dasturiy ta'minotda qo'llaniladigan Twofish eng tezkor simmetrik shifrlash usuli hisoblanadi. Twofish-dan foydalanish bepul bo'lsa-da, u patentlangan yoki ochiq manba emas. Shunga qaramay, u PGP (Pretty Good Privacy) kabi mashhur shifrlash ilovalarida qo'llaniladi. U 256 bitgacha kalit o'lchamlariga ega bo'lishi mumkin.

Asimmetrik shifrlashning eng keng tarqalgan usullari quyidagilardan iborat:

RSA: Rivest-Shamir-Adelmanning stendlari, MIT tadqiqotchilari triosi 1977 yilda birinchi marta tasvirlangan. RSA assimetrik shifrlashning asl shakllaridan biridir. Ochiq kalit ikkita tub son va yordamchi qiymatni faktoring qilish orqali yaratiladi. RSA ochiq kalitidan har kim ma'lumotlarni shifrlash uchun foydalanishi mumkin, lekin faqat asosiy raqamlarni biladigan odam ma'lumotlarni shifrini ochishi mumkin. RSA kalitlari juda katta bo'lishi mumkin (2,048 yoki 4,096 bit odatiy o'lchamlar) va shuning uchun qimmat va sekin hisoblanadi. RSA kalitlari ko'pincha simmetrik shifrlashning umumiy kalitlarini shifrlash uchun ishlatiladi.

Elliptik egri kriptografiya (ECC): cheklangan maydonlar ustidagi elliptik egri chiziqlarga asoslangan assimetrik shifrlashning ilg'or shakli. Usul katta shifrlash kalitlarining mustahkam xavfsizligini ta'minlaydi, ammo kichikroq va samaraliroq iz bilan. Masalan, "256-bitli elliptik egri ochiq kalit 3072-bitli RSA ochiq kaliti bilan taqqoslanadigan xavfsizlikni ta'minlashi kerak." Ko'pincha raqamli imzolar uchun va simmetrik shifrlashda umumiy kalitlarni shifrlash uchun ishlatiladi.

# Ma'lumotlarni shifrlashning ahamiyati

![5-benefits-using-encryption-technology](https://github.com/themusharraf/Encryption/assets/122869450/43562a7b-ade9-4b03-9099-b753083c0038)


Odamlar shifrlash bilan har kuni duch kelishadi, buni bilishadimi yoki yo'qmi. Shifrlash smartfonlar va shaxsiy kompyuterlar kabi qurilmalarni himoyalash, bank depozitini kiritish va onlayn sotuvchidan mahsulot sotib olish kabi moliyaviy operatsiyalarni himoya qilish va elektron pochta va matnlar kabi xabarlar shaxsiy ekanligiga ishonch hosil qilish uchun ishlatiladi.

Agar veb-sayt manzili “https://” (“s” “xavfsiz” degan ma’noni anglatadi) bilan boshlanishini payqagan bo‘lsangiz, bu veb-sayt transport shifrlashdan foydalanayotganligini anglatadi. Virtual xususiy tarmoqlar (VPNlar) qurilmadan maʼlumotlar kelishi va oʻtishini begona koʻzlardan yashirish uchun shifrlashdan foydalanadi.

Ma'lumotlarni shifrlash muhim, chunki u odamlarning maxfiyligini himoya qilishga yordam beradi va ma'lumotlarni tajovuzkorlar va boshqa kiberxavfsizlik tahdidlaridan himoya qiladi. Shifrlash ko'pincha sog'liqni saqlash, ta'lim, moliya va bank ishi va chakana savdo kabi tashkilotlar uchun tartibga soluvchi nuqtai nazardan majburiydir.

Shifrlash to'rtta muhim funktsiyani bajaradi:

Maxfiylik: ma'lumotlar mazmunini sir saqlaydi
Butunlik: xabar yoki ma'lumotlarning kelib chiqishini tasdiqlaydi
Autentifikatsiya: xabar yoki ma'lumotlarning mazmuni yuborilganidan beri o'zgartirilmaganligini tasdiqlaydi
Rad etmaslik: jo'natuvchiga ma'lumotlar yoki xabarning kelib chiqishini rad etishiga yo'l qo'ymaydi

