

"""
UTF-8:

Kodlash: text.encode('utf-8')
Dekodlash: encoded_data.decode('utf-8')
Misol:


"""


text = "Hello, World!"
encoded_data = text.encode('utf-8')
decoded_data = encoded_data.decode('utf-8')

print(f"Original Text: {text}")
print(f"Encoded Text: {encoded_data}")
print(f"Decoded Text: {decoded_data}")
