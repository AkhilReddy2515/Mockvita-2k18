import itertools
x1=input()
a1=x1.split(',')
N=int(a1[0])
P=int(a1[1])
Q=int(a1[2])
x=input()
a=x.split(',')
S=[]
for u in a:
    S.append(int(u))
c=0
y=[]
def findsubsets(S,m):
      y.extend(list(itertools.combinations(S,m)))
for i in range(2,N+1):
    findsubsets(S,i)
res=[]
for a in y:
    p=1
    for x in a:
        p=p*x
    if p%35==0:
       c=c+1
print(c%1009)
    