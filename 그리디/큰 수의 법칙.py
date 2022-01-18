n, m, k = list(map(int,input().split()))
num = list(map(int, input().split()))

num.sort(reverse=True)
count = 0
ans = 0

for _ in range(m):
    if count == k:
        ans += num[1]
        count = 0
    else:
        ans += num[0]
        count += 1

print(ans)