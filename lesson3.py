"""
Asimmetrik kalitli shifrlash:

Asimmetrik kalitli shifrlashda biz ikkita kalitdan foydalanamiz:
ochiq kalit va shaxsiy kalit. Ochiq kalit ma'lumotlarni shifrlash
uchun, shaxsiy kalit esa ma'lumotlarni shifrlash uchun ishlatiladi.
Nomiga ko'ra, ochiq kalit ochiq bo'lishi mumkin (ma'lumotlarni
yuborishi kerak bo'lgan har bir kishiga yuborilishi mumkin). 
Hech kim sizning shaxsiy kalitingizga ega emas, shuning uchun o'rtadagi
hech kim ma'lumotlaringizni o'qiy olmaydi.

""" # noqa

import rsa
 # noqa
# bilan umumiy va shaxsiy kalitlarni yarating # noqa
# rsa.newkeys usuli, bu usul qabul qilinadi # noqa
# kalit uzunligi uning parametri sifatida # noqa
# kalit uzunligi kamida 16 boʻlishi kerak # noqa

publicKey, privateKey = rsa.newkeys(512)

# bu biz shifrlaydigan satr # noqa
message = "hello geeks"

# rsa.encrypt usuli shifrlash uchun ishlatiladi # noqa
# umumiy kalit qatori bo'lishi kerak # noqa
# shifrlashdan oldin bayt qatoriga kodlash # noqa
# kodlash usuli bilan # noqa
encMessage = rsa.encrypt(message.encode(),publicKey)

print("original string: ", message)
print("encrypted string: ", encMessage)

# shifrlangan xabarni shifrlash mumkin # noqa
# ras.decrypt usuli va shaxsiy kalit bilan # noqa
# shifrni ochish usuli kodlangan bayt qatorini qaytaradi, # noqa
# uni satrga aylantirish uchun dekodlash usulidan foydalaning # noqa
# ochiq kalitdan shifrni ochish uchun foydalanish mumkin emas   # noqa
decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("decrypted string: ", decMessage)
