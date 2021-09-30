from itertools import combinations
n = int(input())
taste = []
com = []
res = 1_000_000_001
for i in range(n):
    taste.append(list(map(int, input().split())))
for i in range(1, n+1):
    com.append(combinations(taste, i))
for c in com:
    for t in c:
        s, b = 1, 0
        for i in t:
            s *= i[0]
            b += i[1]
        res = min(res, abs(s - b))
print(res)
