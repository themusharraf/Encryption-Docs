import urllib.parse

# Example String
original_string = "https://chat.openai.com/c/6a22d0d1-fb3c-448e-a09b-2a88ff96aa65"

# Encode for URL
encoded_string = urllib.parse.quote(original_string)
print("Encoded URL String:", encoded_string)

# Decode from URL
decoded_string = urllib.parse.unquote(encoded_string)
print("Decoded URL String:", decoded_string)
