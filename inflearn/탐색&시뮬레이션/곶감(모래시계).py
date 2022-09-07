n=int(input())
list = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())
    if t==0:
        for _ in range(k):
            list[h-1].append(list[h-1].pop(0))
    else:
        for _ in range(k):
            list[h-1].insert(0, list[h-1].pop())

s=0
e=n-1
res=0
for i in range(n):
    for j in range(s, e+1):
        res+=list[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)