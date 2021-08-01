from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

for i in range(n):
    t, c = map(int,input().split())
    val = deque(input().split())
    key = deque([j for j in range(t)])
    result = []
    check = key[c]
    while len(val)!=0:
        if val[0] != max(val):
            val.append(val.popleft())
            key.append(key.popleft())
        else:
            val.popleft()
            result.append(key.popleft())
    print(result.index(check)+1)