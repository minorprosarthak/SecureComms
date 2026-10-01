import json, string
cts={int(k):bytes.fromhex(v) for k,v in json.load(open('cts.json')).items()}
target=13
L=max(len(c) for c in cts.values())
key=[None]*L
letters=set(string.ascii_letters.encode())
# Space heuristic: c_i ^ c_j is a letter (bit 0x20 set, alpha) when one of them is a space
for pos in range(L):
    votes={}
    for i,ci in cts.items():
        if pos>=len(ci): continue
        cnt=0
        for j,cj in cts.items():
            if i==j or pos>=len(cj): continue
            if (ci[pos]^cj[pos]) in letters: cnt+=1
        n=sum(1 for j,cj in cts.items() if j!=i and pos<len(cj))
        if n>=3 and cnt>=0.8*n:   # i likely has a space here
            votes[i]=ci[pos]^0x20
    if votes:
        vals=list(votes.values())
        key[pos]=max(set(vals),key=vals.count)
def dec(c):
    return ''.join(chr(c[p]^key[p]) if key[p] is not None and 32<=(c[p]^key[p])<127 else '_' for p in range(len(c)))
for n in sorted(cts): print(n,dec(cts[n]))
json.dump(key,open('key.json','w'))
