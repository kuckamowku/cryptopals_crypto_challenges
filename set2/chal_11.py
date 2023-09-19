import os
from random import randint
from Crypto.Cipher import AES
from pwn import xor


# Поиск повторяющихся блоков
def find_repeat_block(text: bytes, len_block=16):
    n_block = len(text) // len_block
    text = list(dict.fromkeys([text[i * len_block: (i + 1) * len_block] for i in range(len(text) // len_block)]))
    if n_block == len(text):
        return False
    else:
        return True


def pad_pkcs7(text: bytes, block_size: int = 16):
    ans = block_size - (len(text) % block_size)
    text += ans * bytes([ans])
    return text


# Шифрование текста алгоритмом AES_ECB
def aes_ebc_enc(text: bytes, key: bytes = os.urandom(16)) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    cipher = cipher.encrypt(pad_pkcs7(text))
    return cipher


# Шифрование текста алгоритмом AES_CBC
def aes_cbc_enc(text: bytes, key: bytes = os.urandom(16), IV: bytes = os.urandom(16)) -> bytes:
    text = pad_pkcs7(text)
    text = [text[i * 16: (i + 1) * 16] for i in range(len(text) // 16)]
    answer = b''
    cipher = AES.new(key, AES.MODE_ECB)
    for i in text:
        i = xor(i, IV)
        ciph = cipher.encrypt(i)
        IV = ciph
        answer += ciph
    return answer


plaintext = os.urandom(randint(5, 11)) + b"ABA" * 50 + os.urandom(randint(5, 11))
choise = randint(0, 1)

# Случайным образом выбираем каким из алгоритмов шифровать текст
if choise:
    cipher = aes_ebc_enc(plaintext)
else:
    cipher = aes_cbc_enc(plaintext)

# Проверям наличие повторяющихся блоков в шифртексте
# Если используем AES_EBC - выведется True
# Если используем AES_CBC - выведется False

if find_repeat_block(cipher):
    print('Для шифрования использовался алгоритм AES_ECB')
else:
    print('Для шифрования использовался алгоритм AES_CBC')

