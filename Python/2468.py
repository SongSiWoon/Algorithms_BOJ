from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix_min = min(map(min,matrix))
matrix_max = max(map(max,matrix))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(x,y,h):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if matrix[nx][ny] > h and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx,ny])

res = 0
for h in range(matrix_max+1):
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > h and visited[i][j] == 0:
                bfs(i,j,h)
                cnt+=1
    res = max(cnt,res)
print(res)