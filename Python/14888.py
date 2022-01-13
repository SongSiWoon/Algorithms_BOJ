import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))

MIN, MAX = 1e9, -1e9


def sol(depth, res, add, sub, mul, div):
    global MIN, MAX
    if depth == N-1:
        MAX = max(MAX, res)
        MIN = min(MIN, res)
        return

    if add > 0:
        sol(depth+1, res + num[depth+1], add-1, sub, mul, div)
    if sub > 0:
        sol(depth+1, res - num[depth+1], add, sub-1, mul, div)
    if mul > 0:
        sol(depth+1, res * num[depth+1], add, sub, mul-1, div)
    if div > 0:
        if res < 0:
            res = -((-res)//num[depth+1])
        else:
            res = res//num[depth+1]
        sol(depth+1, res, add, sub, mul, div-1)


sol(0, num[0], operator[0], operator[1], operator[2], operator[3])
print(MAX)
print(MIN)
