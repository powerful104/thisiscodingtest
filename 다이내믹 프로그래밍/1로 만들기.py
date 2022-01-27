n = int(input())

dp = [0] * (n + 1)

def make_one(n):
    array = []
    if n == 1:
        return 0
    if dp[n] != 0:
        return dp[n]
    
    if n % 5 == 0:
        array.append(make_one(n//5))
    if n % 3 == 0:
        array.append(make_one(n//3))
    if n % 2 == 0:
        array.append(make_one(n//2))
    array.append(make_one(n - 1))
    
    dp[n] = min(array) + 1
    
    return dp[n]

print(make_one(n))