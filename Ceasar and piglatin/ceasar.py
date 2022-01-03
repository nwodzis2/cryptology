ENC = 0
DEC = 1

def makeDisk():		
    enc_disk = { }
    dec_disk = { }
    #go through first 12
    for i in range(12):
        if((i+1)%4 == 0):
            enc_disk[chr(i+65)] = chr(i+65-3)
        else:
            enc_disk[chr(i+65)] = chr(i+65+1)
    #go through m and n because they just go to one another
    enc_disk[chr(77)] = chr(78)
    enc_disk[chr(78)] = chr(77)
    #go through last 12, same algorithm but only incremented to O
    for i in range(12):
        if((i+1)%4 == 0):
            enc_disk[chr(i+65+14)] = chr(i+65+14-3)
        else:
            enc_disk[chr(i+65+14)] = chr(i+65+14+1)
    #decryption disk is the encyption disk dictionary flipped
    dec_disk = {v: k for k, v in enc_disk.items()}
    return enc_disk, dec_disk


def caesar(msg, mode):
	ret = ''	
	
	msg = msg.upper()
	enc_disk, dec_disk = makeDisk()
	
	if enc_disk is None:
		return ret
	
	if mode == ENC:
		disk = enc_disk
	if mode is DEC:
		disk = dec_disk
		
	for c in msg:
		if c in disk: 
			ret += disk[c]
		else:
			ret += c
			
	return ret


def main():
	plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #get rid of key
	print('Original:\t%s' %plaintext.upper())	 
	ciphertext = caesar(plaintext, ENC)
	print('Caesar Cipher:\t%s' %ciphertext)	
	deciphertext = caesar(ciphertext, DEC)
	print('Deciphered:\t%s' %deciphertext)

if __name__ == '__main__':
	main()
