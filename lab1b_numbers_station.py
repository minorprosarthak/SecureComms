ct="66475 19274 92028 78494 24146 68542 17507 39398 32348 59378 70636".replace(' ','')
key="66153 77185 10800 54937 48159 83271 12892 07132 34987 53954 23074".replace(' ','')
pt=''.join(str((int(c)+int(k))%10) for c,k in zip(ct,key))
print(len(ct),len(key)); print(' '.join(pt[i:i+5] for i in range(0,len(pt),5)))
# AT-ONE-SIR board
row0={'0':'A','1':'T','3':'O','4':'N','5':'E','7':'S','8':'I','9':'R'}
row2=dict(zip('0123456789','BCDFGHJKLM'))
row6=dict(zip('0123456789',['P','Q','U','V','W','X','Y','Z','.','/']))
out=[];i=0
while i<len(pt):
    d=pt[i]
    if d=='2': out.append(row2[pt[i+1]]) if i+1<len(pt) else out.append('?'); i+=2
    elif d=='6': out.append(row6[pt[i+1]]) if i+1<len(pt) else out.append('?'); i+=2
    else: out.append(row0[d]); i+=1
print(''.join(out))
# check alternative: subtraction
alt=''.join(str((int(c)-int(k))%10) for c,k in zip(ct,key)); print(alt)
