n = int(input())
num = list(map(int, input().split()))
num.sort()
res = 1
for j in num:
    if res < j:
        break
    res += j
print(res)