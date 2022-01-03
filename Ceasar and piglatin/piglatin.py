#translate a scentence to pig latin
def pigLatin():
        #list of two letter constonant sounds
        clist = ['gl', 'pl', 'ch', 'ph', 'sl', 'tr', 'br', 'sh', 'fr', 'bl', 'gr', 'fl' ,'st', 'cl']
        s = input('What would you like translated?')
        s = s.split()
        #list of vowels
        v = ['a', 'e', 'i', 'o', 'u']
        for j in range(len(s)):
                i = s[j]
                #if a vowel
                if i[0].lower() in v:
                        s[j] = i+'ay'
                #if two letter
                elif (i[0]+i[1]).lower() in clist:
                        s[j] = i[2:]+i[:2]+'ay'
                #any other
                else:
                        s[j] = i[1:]+i[0]+'ay'
        return ' '.join(s)
#get the pig latin results and print it
x = pigLatin()
print(x)