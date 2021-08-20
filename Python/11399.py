import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

num.sort()
print(num)
result = 0
for i in range(len(num)):
    result += (n-i)*num[i]
print(result)