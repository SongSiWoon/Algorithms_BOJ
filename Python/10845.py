import sys
n= int(sys.stdin.readline())

queue = []

for i in range(n):
    str = sys.stdin.readline().split()
    if str[0] == 'push':
        queue.append(int(str[1]))
    elif str[0] == 'pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop(0))
    elif str[0] == 'size':
        print(len(queue))
    elif str[0] == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif str[0] == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif str[0] == 'back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])


