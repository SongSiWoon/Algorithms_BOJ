import sys

result = [0] * 10000
n = int(input())

for i in range(n):
    num = int(sys.stdin.readline())
    result[num-1] +=1

for i in range(10000):
    if result[i] != 0:
        for j in range(result[i]):
            print(i+1)