def pad_PKCS7(text: bytes, block_size: int=16):
    ans = block_size - len(text)
    text += ans * bytes([ans])
    return text

text = b"YELLOW SUBMARIN"
print(pad_PKCS7(text))
