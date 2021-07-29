import sys

n = int(input())
result = []
for i in range(n):
    result.append(list(map(int,sys.stdin.readline().split())))
result.sort(key= lambda x : (x[1], x[0]))
for i in range(n):
    print(result[i][0], result[i][1])
