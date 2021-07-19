import sys
n = int(input())
p = []
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    p.append((int(age), name))

p.sort(key = lambda x : (x[0], x.index(x[0])))
for i in p:
    print(i[0], end=" ")
    print(i[1])

