from encode import encode
from decode import decode
def encrypt(msg, key):
    msg = encode(msg)
    msg = [(n+key%26) for n in msg]
    msg = decode(msg, "UPPER")
    return msg
def decrypt(msg, key):
    msg = encode(msg)
    msg = [(n-key%26) for n in msg]
    msg = decode(msg, "LOWER")
    return msg
def shift(msg, key, mode):
    if(mode == "ENC"):
        return encrypt(msg, key)
    elif(mode == "DEC"):
        return decrypt(msg, key)