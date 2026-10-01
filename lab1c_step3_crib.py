import json
cts={int(k):bytes.fromhex(v) for k,v in json.load(open('cts.json')).items()}
# crib: recognised quote for message 13 (punctuation stripped in this exercise)
guess13="The Web as I envisaged it we have not seen it yet The future is still so much bigger than the past Tim Berners-Lee"
assert len(guess13)==len(cts[13])
key=bytes(c^ord(p) for c,p in zip(cts[13],guess13))   # K = C xor P
def dec(c): return ''.join(chr(c[i]^key[i]) for i in range(min(len(c),len(key))))
for n in sorted(cts): print(n,dec(cts[n]))
