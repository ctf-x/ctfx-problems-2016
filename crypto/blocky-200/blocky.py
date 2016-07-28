from secrets import IV
g = lambda a, b, q: (a << b%q) & (2**q-1) | ((a & (2**q-1)) >> (q-(b%q)))
h = lambda a, b, q: ((a & (2**q-1)) >> b%q) | (a << (q-(b%q)) & (2**q-1))

def c(x):
    ret = h(x ^ 0x666c616721, (x ^ 0x666c616721) & 0xf, 40)
    ret = g(ret + 0x4e4f504521, (ret + 0x4e4f504521) & 0xf, 40)
    ret *= 0x6861686121
    ret &= 2**40-1
    return ret

def p(text):
    val = 5-(len(text) % 5)
    for _ in xrange(val):
        text += chr(val)
    return text

def encrypt(x):
    blahh = [x[i:i+5] for i in range(0, len(x), 5)]
    iv = IV
    ctxt = ""
    for i in range(len(blahh)):
        v = c(ord(blahh[i][4])+256*ord(blahh[i][3])+65536*ord(blahh[i][2])+16777216*ord(blahh[i][1])+4294967296*ord(blahh[i][0]))
        t = '%x'%h(v^iv, 7, 40)
        ctxt += t if len(t)%2==0 else "0"+t
        iv = v
    return ctxt

print encrypt(p(raw_input()))
