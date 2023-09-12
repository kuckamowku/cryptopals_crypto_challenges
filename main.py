# Первый SET включает в себя 8 заданий, большая часть из которых являются простенькими, но полезными в будующем преобразованиями.
# Из-за их простоты первые 5 задания будут находится в одном файле

import base64
import binascii
from pwn import xor

#2 Имеем две строки, необходимо из заксорить:)
string1 = binascii.unhexlify("1c0111001f010100061a024b53535009181c")
string2 = binascii.unhexlify("686974207468652062756c6c277320657965")
print(binascii.hexlify(xor(s, x)))
#b'746865206b696420646f6e277420706c6179'

#3 Имеем зашифрованный текст XORом с ключом длинной равной 1, перебрать все знаечния ключа, расшифровать текст
def find_key(text: str) -> None:
    s = binascii.unhexlify(text)
    for i in range(256):
        if '\\' not in str(xor(s, i)):
            print(xor(s, i), i)
find_key('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
#b"Cooking MC's like a pound of bacon"

#4 Дано 300+ строк, одна из строк зашифрована XORом с ключом длинной равной 1, необходимо определить какая именно и расшифровать ее
s = """""" # 300+ строк 
for i in s:
    find_key(i)
# b'Now that the party is jumping\n' 53

#5 Необходимо зашифровать текст с помощью repeating-key XOR
s = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = 'ICE'
ans = b''
for i in range(len(s)):
    ans += binascii.hexlify(xor(s[i], key[i % 3]))
print(ans)
#b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
