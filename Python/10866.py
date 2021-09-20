import sys
from collections import deque

deq = deque()

n = int(input())

for i in range(n):
    str = sys.stdin.readline().strip().split()

    if str[0] == 'push_front':
        deq.appendleft(str[1])
    elif str[0] == 'push_back':
        deq.append(str[1])
    elif str[0] == 'pop_front':
        if len(deq)==0:
            print(-1)
        else:
            print(deq.popleft())
    elif str[0] == 'pop_back':
        if len(deq)==0:
            print(-1)
        else:
            print(deq.pop())
    elif str[0] == 'size':
        print(len(deq))
    elif str[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif str[0] == 'front':
        if len(deq)==0:
            print(-1)
        else:
            print(deq[0])
    elif str[0] == 'back':
        if len(deq)==0:
            print(-1)
        else:
            print(deq[-1])         