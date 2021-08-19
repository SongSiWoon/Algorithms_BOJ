import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    cnt = 1
    rank=[]
    for i in range(n):
        rank.append(list(map(int, input().split())))
    rank.sort()
    max = rank[0][1]

    for j in range(1,n):
        if max > rank[j][1]:
            cnt += 1
            max = rank[j][1]
    print(cnt)