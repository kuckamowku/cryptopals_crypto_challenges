def pad_PKCS7(text: bytes, block_size: int=16):
    ans = block_size - len(text)
    text += ans * bytes([ans])
    return text

text = b"YELLOW SUBMA"
print(pad_PKCS7(text))
#b'YELLOW SUBMA\x04\x04\x04\x04'

text = b"YELLOW SUBMARI"
print(pad_PKCS7(text))
#b'YELLOW SUBMARI\x02\x02'
