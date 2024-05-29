# It is CaesarPlus
# Caesar used a few spaces
# but Caesar Plus used shuffles and additional values ​​instead of spaces.
# It use ex ) CaesarCode( ~~~ )


from time import time #시저 플러스 암호화 만드는데 걸리는 시간 세는거
from sys import setrecursionlimit
from random import shuffle, randrange
from string import digits, punctuation, ascii_letters
start = time()
setrecursionlimit(10**6)

def Return(count):
    global point_key
    if count == 0: return 0
    point_key += chars[randrange(0, len(chars)-1)]
    
    Return(count-1)
    
chars = digits + punctuation + ascii_letters
chars = list(chars)
Key = chars.copy()

shuffle(Key)

CaesarCode = {}

for char, key in zip(chars, Key):
    point_key = key

    Return(10000)
    CaesarCode[char] = point_key
end = time()
print(f"crypt : {CaesarCode} ---- time : {end-start:.5f}sec")


#encrypt

