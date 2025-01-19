import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + ' '
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f'chars: {chars}')
# print(f'key: {key}')

# Encryption
plain_text = input('Enter the text to encrypt: ')
cipher_text = ''

for char in plain_text:
    cipher_text += key[chars.index(char)]

print(f'Encrypted text: {cipher_text}')


# Decryption
decrypted_text = ''
for char in cipher_text:
    decrypted_text += chars[key.index(char)]

print(f'Decrypted text: {decrypted_text}')