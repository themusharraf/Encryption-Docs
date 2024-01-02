

"""
UTF-8:

Kodlash: text.encode('utf-8')
Dekodlash: encoded_data.decode('utf-8')
Misol:


"""


password = "@admin1234"
encoded_data = password.encode('utf-8').hex()
# decoded_data = encoded_data.decode('utf-8')

print(f"Original Text: {password}")
print(f"Encoded Text: {encoded_data}")
# print(f"Decoded Text: {decoded_data}")
