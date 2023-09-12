import base64
import binascii
from pwn import xor
#2
# s = binascii.unhexlify("1c0111001f010100061a024b53535009181c")
# x = binascii.unhexlify("686974207468652062756c6c277320657965")
# print(binascii.hexlify(xor(s, x)))

#3
def find_key(text: str) -> None:
    s = binascii.unhexlify(text)
    for i in range(256):
        if '\\' not in str(xor(s, i)):
            print(xor(s, i), i)
find_key('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

#b"Cooking MC's like a pound of bacon"


#4
#
# for i in s:
#     find_key(i)
# b'Now that the party is jumping\n' 53

#5
# s = """Burning 'em, if you ain't quick and nimble
# I go crazy when I hear a cymbal"""
# key = 'ICE'
# ans = b''
# for i in range(len(s)):
#     ans += binascii.hexlify(xor(s[i], key[i % 3]))
# print(ans)

#6