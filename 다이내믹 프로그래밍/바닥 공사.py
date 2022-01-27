n = int(input())

dp = [0] * (n + 1)

def fill(n):
    if n == 0 or n == 1:
        return 1
    
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = fill(n - 1) + fill(n - 2)*2
    return dp[n]


print(fill(n)%796796)
print(dp)