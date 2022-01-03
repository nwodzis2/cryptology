def decode(msg, case):
    if(case == "UPPER"):
        return("".join(chr(int(c)+65) for c in msg))
    elif(case == "LOWER"):
        return("".join(chr(int(c)+97) for c in msg))
    return False