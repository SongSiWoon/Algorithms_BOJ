import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d):
    global cnt
    if matrix[x][y] == 0:
        matrix[x][y] = 2
        cnt += 1
    for j in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if matrix[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if matrix[nx][ny] == 1:
        return
    clean(nx, ny, d)


n, m = map(int, input().split())
r, c, d = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

cnt = 0
clean(r, c, d)
print(cnt)