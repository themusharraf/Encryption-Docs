
"""
Simmetrik kalitli shifrlash:
Simmetrik kalitli shifrlashda ma'lumotlar bir xil kalit bilan kodlanadi va dekodlanadi.
 Bu shifrlashning eng oson yo'li, ammo xavfsizroq. Qabul qiluvchiga shifrni ochish uchun
kalit kerak, shuning uchun kalitlarni uzatishning xavfsiz usuli kerak. Kalitga ega bo'lgan
 har bir kishi o'rtadagi ma'lumotlarni o'qiy oladi.
""" # noqa

from cryptography.fernet import Fernet

# biz quyidagi qatorni shifrlaymiz. # noqa
message = "hello geeks"

"""
shifrlash va shifrni ochish uchun kalit yaratish
Yaratish uchun fernetdan foydalanishingiz mumkin
kalit yoki tasodifiy kalit generatoridan foydalaning
bu yerda men kalit yaratish uchun fernetdan foydalanmoqdaman
""" # noqa

key = Fernet.generate_key()

# Kalit bilan Fernet sinfiga misol keltiring # noqa
fernet = Fernet(key)

"""
keyin Fernet sinf misolidan foydalaning
qatorni shifrlash kerak
shifrlashdan oldin bayt qatoriga kodlangan bo'lishi kerak
""" # noqa
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

"""
bilan shifrlangan satr shifrini hal qilish Kalitning 
Fernet namunasi,
bu satrni shifrlash uchun ishlatilgan
kodlangan bayt satri shifrni ochish usuli bilan qaytariladi,
shuning uchun uni dekodlash usullari bilan satrga dekodlang
"""  # noqa
decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)
