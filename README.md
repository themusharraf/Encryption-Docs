# Encryption

#Creator: Musharraf Ibragimov

Shifrlash nima?
Shifrlash ma'lumotlarni o'g'irlash, o'zgartirish yoki buzishdan himoya qilish uchun ishlatiladi va ma'lumotlarni faqat noyob raqamli kalit bilan ochish mumkin bo'lgan maxfiy kodga aylantirish orqali ishlaydi.

Shifrlangan ma'lumotlar kompyuterlarda ishlayotganda yoki ular o'rtasida o'tish paytida yoki qayta ishlanayotganda, bu kompyuterlar mahalliy yoki masofaviy bulutli serverlar bo'lishidan qat'i nazar himoyalanishi mumkin.

![what-is-encryption](https://github.com/themusharraf/Encryption/assets/122869450/aafe97e4-d1bb-49bd-b88d-56c47ec95fdf)

Eng asosiy darajada shifrlash ma'lumot yoki ma'lumotni matematik modellar yordamida himoyalash jarayoni bo'lib, uni ochish uchun kalitga ega bo'lgan tomonlargina unga kirishi mumkin bo'ladi. Bu jarayon juda oddiydan juda
murakkabgacha bo'lishi mumkin va matematiklar va kompyuter olimlari iste'molchilar va korxonalar har kuni tayanadigan ma'lumotlar va ma'lumotlarni himoya qilish uchun ishlatiladigan shifrlashning o'ziga xos shakllarini ixtiro qildilar.

![difference-between-encryption-and-signing](https://github.com/themusharraf/Encryption/assets/122869450/7c873e4f-e99f-4625-abfb-68e6b773736b)


# Shifrlash turlari

![Asymmetric-vs-Symmetric](https://github.com/themusharraf/Encryption/assets/122869450/a5531df7-2d6a-45c0-a8a1-8445de030c96)


Shifrlash algoritmlarining eng keng tarqalgan ikkita turi nosimmetrik va assimetrikdir.
Umumiy kalit yoki shaxsiy kalit algoritmi sifatida ham tanilgan simmetrik shifrlash shifrlash va shifrni ochish uchun bir xil kalitdan foydalanadi. Simmetrik kalit shifrlarini ishlab chiqarish arzonroq hisoblanadi va shifrlash va shifrni ochish uchun unchalik ko'p hisoblash quvvatini talab qilmaydi, ya'ni ma'lumotlarni dekodlashda kechikish kamroq bo'ladi.

Kamchilik shundaki, agar ruxsatsiz shaxs kalitga qo'l tegsa, ular tomonlar o'rtasida yuborilgan har qanday xabar va ma'lumotlarning shifrini ochishi mumkin bo'ladi. Shunday qilib, umumiy kalitni uzatish boshqa kriptografik kalit bilan shifrlanishi kerak, bu esa qaramlik davriga olib keladi.

Ochiq kalitli kriptografiya sifatida ham tanilgan assimetrik shifrlash ma'lumotlarni shifrlash va shifrini ochish uchun ikkita alohida kalitdan foydalanadi. Ulardan biri shifrlash uchun barcha tomonlar o'rtasida taqsimlangan ochiq kalitdir. Ochiq kalitga ega bo'lgan har bir kishi shifrlangan xabarni yuborishi mumkin, lekin faqat ikkinchi, shaxsiy kalit egalari xabarning shifrini ochishi mumkin.

Asimmetrik shifrlash ishlab chiqarish qimmatroq hisoblanadi va shifrni ochish uchun ko'proq hisoblash quvvati talab qilinadi, chunki ommaviy shifrlash kaliti odatda katta, 1024 dan 2048 bitgacha. Shunday qilib, assimetrik shifrlash ko'pincha katta ma'lumotlar paketlari uchun mos kelmaydi.

