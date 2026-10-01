import base64, math, zlib, re
from math import gcd, isqrt
def isprime(n):
    if n<2: return False
    if n<4: return True
    if n%2==0 or n%3==0: return False
    k=5
    while k*k<=n:
        if n%k==0 or n%(k+2)==0: return False
        k+=6
    return True
print("A1",[ (n,isprime(n)) for n in (91,421,1449)])
print("A2",gcd(88,46),gcd(105,35))
for s in ("Hello","hello","HELLO"):
    print("A3",s,base64.b64encode(s.encode()).decode(),s.encode().hex())
print("A4 b64",base64.b64decode("bGxveWRz"),"hex",bytes.fromhex("6E6170696572"),
      "bin",''.join(chr(int(b,2)) for b in "01000001 01101110 01101011 01101100 01100101 00110001 00110010 00110011".split()))
print("A5",53431%453, 53431%4532)
print("A6",0x43|0x21,0x43&0x21,0x43^0x21, bin(0x43),bin(0x21))
v=93;print("A7",v,bin(v),hex(v),oct(v),chr(v))
print("A9",base64.b64encode(b"crypto"),"A10",base64.b64encode(b"crypto1"))
print("A11",41<<1,41<<2,41>>1,41>>2)
def factors(n): return [i for i in range(1,n+1) if n%i==0]
print("A12",factors(432))
p=2;f=[];n=432
while n>1:
    while n%p==0:f.append(p);n//=p
    p+=1
print("A12 prime factors",f)
for s in ("eJzzyc9Lyc8DAAgpAms=","eJxzSi3KycwDAAfXAl0=","eJzzSy1XiMwvygYADKUC8A=="):
    print("A13",zlib.decompress(base64.b64decode(s)))
import random,string
for k in (1,2,4,8,16):
    s=("abc"*k).encode(); r=''.join(random.choice(string.ascii_lowercase) for _ in range(3*k)).encode()
    print("A13 obs",len(s),len(zlib.compress(s)),len(zlib.compress(r)))
print("B1",gcd(4105,10),gcd(4539,6))
print("B2",gcd(5435,634)==1,gcd(5432,634)==1,gcd(5435,634),gcd(5432,634))
print("C1",pow(8,13,271),pow(12,23,973))
print("C2",pow(8,5,269))
print("C3",pow(5,5,53),pow(4,11,79),pow(101,7,293))
print("D1",[2,3]+[x for k in range(1,17) for x in (6*k-1,6*k+1) if x<=100 and isprime(x)])
pr=[i for i in range(2,1001) if isprime(i)];print("D2",pr[-1],len(pr))
for lim in (100,1000,5000,10000): print("D3",lim,max(i for i in range(2,lim+1) if isprime(i)))
print("D4",[(n,isprime(n)) for n in (5,7919,858599509,982451653,982451652)])
def lcg(a,x,c,m,n=5):
    o=[]
    for _ in range(n):
        x=(a*x+c)%m;o.append(x)
    return o
print("E1",lcg(21,35,31,100,6))
print("E2",lcg(22,35,31,100,4))
print("E3",lcg(954365343,436241,55119927,1000000,4))
print("E4",lcg(2175143,3553,10653,1000000,4))
