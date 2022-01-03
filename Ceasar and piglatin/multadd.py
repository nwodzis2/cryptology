import math
#multiadd function (part 1)
def multiadd(a,b,c):
    return(a*b+c)
#(part b) makes calulations using the imported math
print("sin(pi/4) + cos(pi/4)/2 is:")
print(multiadd(1/2, math.cos(math.pi/4),math.sin(math.pi/4)))
print("ceiling(276/19) + 2 log_7(12) is:")
print(multiadd(2, math.log(12,7), math.ceil(276/19)))