from z3 import *
import binascii, string, itertools
g = lambda a, b, q: (a << b%q) & (2**q-1) | ((a & (2**q-1)) >> (q-(b%q)))
h = lambda a, b, q: ((a & (2**q-1)) >> b%q) | (a << (q-(b%q)) & (2**q-1))

bits = 40
mask = 2**bits - 1
allowed_chars = string.printable

def int2ascii(x):
    txt = chr(x//4294967296)
    x-=(x//4294967296)*4294967296
    txt+= chr(x//16777216)
    x-=(x//16777216)*16777216
    txt+= chr(x//65536)
    x-=(x//65536)*65536
    txt+= chr(x//256)
    x-=(x//256)*256
    txt+= chr(x)
    return txt
def ascii2int(blah):
    return ord(blah[4])+256*ord(blah[3])+65536*ord(blah[2])+16777216*ord(blah[1])+4294967296*ord(blah[0])

def rot(val, steps):
   return (val << (bits-steps)) | LShR(val, steps)

def symencrypt(input):
   eax = rot(input ^ 0x666c616721, (input ^ 0x666c616721) & 0xf)
   eax = rot(eax + 0x4e4f504521, bits - (eax + 0x4e4f504521 & 0xf))
   eax = eax * 0x6861686121
   return eax & mask

def encrypt(x):
    ret = h(x ^ 0x666c616721, (x ^ 0x666c616721) & 0xf, 40)
    ret = g(ret + 0x4e4f504521, (ret + 0x4e4f504521) & 0xf, 40)
    ret *= 0x6861686121
    ret &= 2**40-1
    return ret


known = '6915c70109fa3398321127cfcd44342115d6d75feb56706087'
data = list(map(''.join, zip(*[iter(known)]*10)))
print data
vs = [int(x, 16) for x in data]
vs = [g(x,7,40) for x in vs]


poss_ivs = []
for x in allowed_chars:
    enc = encrypt(ascii2int('ctf('+x))
    poss_ivs.append(enc^vs[0])
print poss_ivs
#vs[0]^=0xde4dbe3f49
#for i in range(1,len(vs)):
#    vs[i]^=vs[i-1]
#print "vs:",vs


def undoBlockEncrypt(x):
    s = Solver()
    first = BitVec('bitvec', bits)
    s.add(symencrypt(first)==x)
    while s.check() == sat:
        sol = s.model()
        vec = sol[first].as_long()
        s.add(first != vec)
        text = int2ascii(vec)
        print text
        #allASCII = True
        #for c in text:
        #    if c not in allowed_chars:
        #        allASCII= False
        #if allASCII:
        #    print "text:", text

#for x in poss_ivs:
#    print x
#    undoBlockEncrypt(x^vs[1]^vs[0])
vs[0]^=0xde4dbe3f49
undoBlockEncrypt(vs[0])
for i in range(1,len(vs)):
    vs[i]^=vs[i-1]
    undoBlockEncrypt(vs[i])
