n = int(input())
points = list(map(int, input().split()))
sum = 0
cnt = 0

for x in points:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt = 0