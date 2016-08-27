import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 7763))

def xgcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = xgcd(b % a, a)
        return (g, x - (b // a) * y, y)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def solve(s):
    nrand = len(s)
    t = []
    for x in range(nrand-1):
        t.append(s[x+1]-s[x])
    u = []
    for x in range(nrand-3):
        u.append(abs(t[x+2]*t[x]-t[x+1]**2))
    m = reduce(gcd, u)
    r4 = s[-4]
    r3 = s[-3]
    r2 = s[-2]
    r1 = s[-1]
    x = r2-r4
    b = r1-r3
    if x<0:
        x*=-1
        b*=-1
    if b<0:
        b=b%m
    g,x2,y2 = xgcd(x, m)
    if g==1:
        xi = x2%m
        a=(b*xi)%m
        c=(r1-r2*a)%m
        return [m,a,c]
    else:
        return None


def recvline(sock):
        buf = ""
        while not buf.endswith("\n"):
            buf += sock.recv(1)
        return buf.strip()

recvline(sock)
recvline(sock)
recvline(sock)
recvline(sock)

money = 20

while money<=10**6:
    s = []
    for x in range(8):
        recvline(sock)
        recvline(sock)
        sock.sendall("1\n")
        money-=1
        recvline(sock)
        sock.sendall("0\n")
        recvline(sock)
        ln = recvline(sock)
        num = int(ln.split("You should have guessed ")[1].split(". ")[0])
        print num
        s.append(num)
        recvline(sock)
        sock.sendall("Y\n")
    print "Solving.."
    m,a,c = solve(s)
    nextNum = (a*s[-1]+c)%m
    print recvline(sock)
    print recvline(sock)
    sock.sendall(str(money)+"\n")
    print recvline(sock)
    sock.sendall(str(nextNum)+"\n")
    print recvline(sock)
    print recvline(sock)
    print recvline(sock)
    print recvline(sock)
    sock.sendall("Y\n")
    money*=2
print recvline(sock)
sock.close()
