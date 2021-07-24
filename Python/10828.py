import sys

n = int(input())

result = []

for i in range(n):
    str = sys.stdin.readline().strip().split()
    if str[0] == 'push':
        result.append(str[1])
    elif str[0] == 'pop':
        if len(result) ==0:
            print(-1)
        else:
            print(result.pop())
    elif str[0] == 'size':
        print(len(result))
    elif str[0] == 'empty':
        if len(result) ==0:
            print(1)
        else:
            print(0)
    elif str[0] == 'top':
        if len(result) ==0:
            print(-1)
        else:
            print(result[-1])