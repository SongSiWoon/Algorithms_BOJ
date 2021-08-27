from collections import deque
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
#day = [[0]*m]*n
dx = [0,0,-1,1]
dy = [-1,1,0,0]
cnt = 0
q = deque()
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.append([i,j])
            #day[i][j] = 1
def bfs():
    global cnt
    while q:
        cnt+=1
        for l in range(len(q)):
            qx, qy = q.popleft()
            for i in range(4):
                nx = qx+dx[i]
                ny = qy+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if matrix[nx][ny] == 0:
                        matrix[nx][ny] = 1
                        #day[nx][ny] = day[qx][qy] +1
                        q.append([nx,ny])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                return -1
    return cnt-1
    #return max(max(day))
print(bfs())