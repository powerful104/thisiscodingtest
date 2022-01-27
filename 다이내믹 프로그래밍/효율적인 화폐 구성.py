n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(int(input()))

dp = [0] * (m + 1)

for i in range(1, m+1):
    tmp_arr = []
    for j in array:
        if i - j >= 0 and dp[i-j] != -1:
                tmp_arr.append(dp[i-j])
    
    print(i, tmp_arr)
    if len(tmp_arr) == 0:
        dp[i] = -1
    else:
        dp[i] = min(tmp_arr) + 1

print(dp[m])