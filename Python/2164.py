from collections import deque
n = int(input())

num = [i+1 for i in range(n)]
num = deque(num)
if n==1:
    print(1)
elif n<=5:
    print(2)
else:
    for i in range(n-2):
        num.popleft()
        num.append(num[0])
        num.popleft()
    print(num[1])