import sys

a=[]
result = []
n = int(input())
for i in range(n):
    a.append(sys.stdin.readline().strip())
    
a.sort()
a.sort(key = len)
for i in a:
    if i not in result:
        result.append(i)

for i in result:
    print(i)