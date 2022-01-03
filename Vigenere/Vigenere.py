from encode import encode
from decode import decode
from sympy import *

def encrypt(msg, key):
    msg = encode(msg)
    key = encode(key)
    iterations = 0
    iterations2 = 0
    for i in msg:
        msg[iterations2] = (i + key[iterations]) % 26
        if(iterations != 0 and iterations%(len(key)-1) == 0):
            iterations = 0
        else:
            iterations += 1
        iterations2 += 1
    msg = decode(msg, "UPPER")
    return msg
def decrypt(msg, key):
    msg = encode(msg)
    key = encode(key)
    iterations = 0
    iterations2 = 0
    for i in msg:
        msg[iterations2] = (i - key[iterations]) % 26
        if(iterations != 0 and iterations%(len(key)-1) == 0):
            iterations = 0
        else:
            iterations += 1
        iterations2 += 1
    msg = decode(msg, "LOWER")
    return msg
def Vigenere(msg, key, mode):
    if(mode == "ENC"):
        return encrypt(msg, key)
    elif(mode == "DEC"):
        return decrypt(msg, key)



print(str(Vigenere("hello my name is bob the builer", "hello", "ENC")))
print(str(Vigenere(str(Vigenere("hello my name is bob the builer", "hello", "ENC")), "hello", "DEC")))