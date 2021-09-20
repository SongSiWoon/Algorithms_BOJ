import sys
n, m = map(int,input().split())
bd = [list(sys.stdin.readline().rstrip()) for i in range(n)]

result = []
for i in range(n-7):
    for j in range(m-7):
        cw = 0
        cb = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2 ==0:
                    if bd[a][b] != 'W':
                            cw += 1
                    if bd[a][b] != 'B':
                            cb += 1
                else:
                    if bd[a][b] != 'B':
                            cw += 1
                    if bd[a][b] != 'W':
                            cb += 1

        result.append(min(cw,cb))

print(min(result))