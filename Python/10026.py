from collections import deque
n = int(input())
matrix = [list(map(str,input())) for _ in range(n)]
color = [[0]*n for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append([x, y])
    color[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if color[nx][ny]==0 and matrix[nx][ny]==matrix[x][y]:
                    color[nx][ny] = 1
                    q.append([nx,ny])
cnt = 0
for i in range(n):
    for j in range(n):
        if color[i][j] == 0:
            bfs(i, j)
            cnt += 1
res1 = cnt
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'
color = [[0]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if color[i][j] == 0:
            bfs(i, j)
            cnt += 1
res2 = cnt
print(res1, res2)