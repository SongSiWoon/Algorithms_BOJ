from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
res = []
def bfs(x,y):
    q = deque()
    q.append([x,y])
    matrix[x][y] = 0
    while q:
        qx, qy = q.popleft()
        for i in range(8):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0<=nx<h and 0<=ny<w and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                q.append([nx,ny])
while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    matrix = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)