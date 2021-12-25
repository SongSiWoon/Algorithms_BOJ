import sys
sys.setrecursionlimit(10**6)
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]


def sol(x, y):
    if x == n-1 and y == n-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        if 0 <= x + board[x][y] < n and 0 <= y < n:
            dp[x][y] += sol(x + board[x][y], y)
        if 0 <= x < n and 0 <= y + board[x][y] < n:
            dp[x][y] += sol(x, y + board[x][y])
    return dp[x][y]


print(sol(0, 0))
