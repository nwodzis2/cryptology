import math
def encrypt(columns, msg):
    length = len(msg)
    rows = math.ceil(length / columns)
    ##padded with z
    encoded = ['z'] * length
    for i in range(length):
        row = i // columns
        col = i % columns
        encoded[col * rows + row] = msg[i]
    return "".join(encoded)

def decrypt(columns, msg):
    ##reverse the encrypt
    return encrypt(len(msg) // columns, msg)
def scytale(msg, key, mode):
    if(mode == "ENC"):
        return encrypt(key, msg).lower()
    elif(mode == "DEC"):
        return decrypt(key, msg).upper()