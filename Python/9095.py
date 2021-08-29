dp = [0] * 100
def sol(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = sol(n-1) + sol(n-2) + sol(n-3)
    return dp[n]
T = int(input())
for _ in range(T):
    n = int(input())
    print(sol(n))