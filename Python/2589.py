from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int,input().split())
matrix = [list(map(str,input())) for _ in range(m)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    res_t = 0
    q = deque()
    q.append((x,y,0))
    visited[x][y] = 1
    while q:
        qx,qy,qt = q.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if matrix[nx][ny] == 'L' and visited[nx][ny] ==0:
                    q.append((nx,ny,qt+1))
                    visited[nx][ny] = 1
                    res_t = qt+1
    return res_t
res = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 'L':
            visited = [[0]*n for _ in range(m)]
            res = max(res, bfs(i,j))
print(res)