n, m = list(map(int,input().split()))

ans = 0

for _ in range(n):
    li = list(map(int,input().split()))
    li.sort()
    if li[0]>ans:
        ans = li[0]
print(ans)    