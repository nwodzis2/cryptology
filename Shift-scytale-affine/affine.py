from encode import encode
from decode import decode
from sympy import *

def encrypt(msg, key):
    msg = encode(msg)
    msg = [(((n*key[0]) + key[1])%26) for n in msg]
    msg = decode(msg, "LOWER")
    return msg
def decrypt(msg, key):
    msg = encode(msg)
    msg = [((1/key[0])*(n - key[1]))%26 for n in msg]
    msg = decode(msg, "UPPER")
    return msg
def affine(msg, key, mode):
    a = key[0]
    b = key[1]
    if(gcd(a, b) == 1):
        return "No Multiplicative inverse"
    elif(mode == "ENC"):
        return encrypt(msg, key)
    elif(mode == "DEC"):
        return decrypt(msg, key)