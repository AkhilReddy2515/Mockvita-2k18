x1=input()
a1=x1.split(',')
M=int(a1[0])
N=int(a1[1])
x=[]
p=[c for c in range(0,M)]
for i in range(0,M):
    x.append(input().split(','))
for j in x:
    for y in range(0,len(j)):
        j[y]=int(j[y])

z=[]
ans=[]
for u in range(0,M*N):
    for (t,t1) in zip(x,p):
        if len(t)!=0:
            z.append(t[-1])
    a1=max(z)
    ans.append(a1)
    ind=z.index(a1)
    x[ind].pop()
    if len(x[ind]) == 0: del x[ind]
    z.clear()
for e in ans:
    print(e,end='')
    