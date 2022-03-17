n=int(input())
a=list(map(int,input().split()))
tmax=0
ma=0
for i in range(n):
    tmax+=a[i]
    if tmax<0:
        tmax=0
    if ma<tmax:
        ma=tmax
print(ma)