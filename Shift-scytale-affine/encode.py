def encode(msg):
    msg = msg.upper()
    msg = "".join(c for c in msg if c.isalpha())
    msg2 = [ord(c)-65 for c in msg]
    return msg2
