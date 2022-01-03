from encode import encode
from decode import decode
import numpy as np
def randomPermAlphabet(msg):
    encoded = encode(msg)
    encoded = np.random.permutation(encoded)
    decoded = decode(encoded, "UPPER")
    return decoded
print(randomPermAlphabet("hi my name is bob"))