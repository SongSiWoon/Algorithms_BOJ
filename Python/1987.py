r, c = map(int, input().split())
matrix = list(input() for i in range(r))
visited = [False] * 26
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0
visited[ord(matrix[0][0]) - 65] = True
def DFS(x, y, cnt):
    global res
    res = max(res, cnt)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<r and 0<=ny<c and visited[ord(matrix[nx][ny]) - 65] == False:
            visited[ord(matrix[nx][ny]) - 65] = True
            DFS(nx,ny,cnt+1)
            visited[ord(matrix[nx][ny]) - 65] = False
DFS(0,0,1)
print(res)