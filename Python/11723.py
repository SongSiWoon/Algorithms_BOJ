import sys
input = sys.stdin.readline

n = int(input())
result = set()
for i in range(n):
    str = list(input().split())

    if str[0] == 'add':
        result.add(int(str[1]))
    elif str[0] == 'remove':
        result.discard(int(str[1]))
    elif str[0] == 'check':
        if int(str[1]) in result:
            print(1)
        else:
            print(0)
    elif str[0] == 'toggle':
        if int(str[1]) in result:
            result.discard(int(str[1]))
        else:
            result.add(int(str[1]))
    elif str[0] == 'all':
        result = set([i for i in range(1,21)])
    else:
        result = set()
