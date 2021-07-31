import sys

input = sys.stdin.readline
k, n = map(int,input().split())
num = []
for i in range(k):
    num.append(int(input()))
start, end = 1, max(num)

while start <= end:
    mid = (start + end)//2
    l = 0
    for i in num:
        l += i//mid
    if l >= n:
        result = mid
        start = mid +1
    else:
        end = mid-1
print(result)