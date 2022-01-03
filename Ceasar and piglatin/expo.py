#given base and exponent uses forloop to caluclate what the exponent wouldbe
def exp(base, exp):
    calc = 1
    for x in range(exp):
        calc = calc * base
    return calc
#print our results of our exp function
print(exp(3,3))
