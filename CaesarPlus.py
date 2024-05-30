# It is CaesarPlus
# Caesar used a few spaces
# but Caesar Plus used shuffles and additional values ​​instead of spaces.
# It use ex ) CaesarCode( ~~~ )


from time import time #counting time
from sys import setrecursionlimit
from random import shuffle, randrange
from string import digits, punctuation, ascii_letters
start = time()
setrecursionlimit(10**6)

def CaesarCode(count):
    global CaesarKey
    if count == 0: return 0
    CaesarKey += chars[randrange(0, len(chars)-1)]
    
    CaesarCode(count-1)
    return 0
    
def cryption(txt):
    global point_crypKey
    if len(txt) == 0: return 0
    
    point_crypKey += CaesarCodeKey[CaesarCodeChars.index(txt[0])]
    cryption(txt[1:])
    return 0

def encryption(txt):
    global point_encrypKey
    if len(txt) == 0: return 0
    
    for idx, k in zip(CaesarCodeKey, CaesarCodeChars):
        if idx == "".join(txt[:10001]):
            point_encrypKey += k
            break
    encryption(txt[10001:])
    return 0
    
chars = digits + punctuation + ascii_letters
chars = list(chars)
Key = chars.copy()

shuffle(Key)

CaesarCodeChars = []
CaesarCodeKey = []

for char, key in zip(chars, Key):
    CaesarKey = key

    CaesarCode(10000)
    CaesarCodeChars.append(char)
    CaesarCodeKey.append(CaesarKey)
end = time()
#print(f"crypt : {CaesarCode} ---- time : {end-start:.5f}sec")


#crypt
text = input()
point_crypKey = ''
cryption(list(text))
print(f"crypKey : {point_crypKey}")
#encrypt
point_encrypKey = ''
encryption(list(point_crypKey))
print(f"encrypKey : {point_encrypKey}")
