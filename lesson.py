import urllib.parse

# Example String
original_string = "admin@1234"

# Encode for URL
encoded_string = urllib.parse.quote(original_string)
print("Encoded URL String:", encoded_string)

# Decode from URL
decoded_string = urllib.parse.unquote(encoded_string)
print("Decoded URL String:", decoded_string)
