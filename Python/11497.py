T = int(input())
for _ in range(T):
    res = 0
    n = int(input())
    num = list(map(int,input().split()))
    num.sort()
    res = max(num[1]-num[0], num[-1] - num[-2])
    for i in range(2, n):
        res = max(res, abs(num[i] - num[i-2]))
    print(res)