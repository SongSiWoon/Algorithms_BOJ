n = int(input())
num = list(map(int, input().split()))
cnt = 1
res = 1

for i in range(1, n):
    if num[i] >= num[i-1]:
        cnt += 1
    else:
        cnt = 1
    res = max(res, cnt)

cnt = 1
for i in range(1, n):
    if num[i] <= num[i-1]:
        cnt += 1
    else:
        cnt = 1
    res = max(res, cnt)
print(res)