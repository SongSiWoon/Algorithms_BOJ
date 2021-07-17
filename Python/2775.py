import sys
T = int(input())

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    p = [a for a in range(1,n+1)]
    for b in range(k):
        for c in range(1,n):
            p[c] += p[c-1]
            
    print(p[-1])