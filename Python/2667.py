n = int(input())
graph =[]
for i in range(n):
    graph.append(list(map(int,input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
res = []

def dfs(x,y):
    graph[x][y] = 0
    global cnt
    cnt += 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if graph[nx][ny] == 1:
            dfs(nx,ny)
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            res.append(dfs(i,j))
            cnt = 0

print(len(res))
for i in sorted(res):
    print(i)