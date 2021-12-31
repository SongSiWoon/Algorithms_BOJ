from collections import deque

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
w, b = 0, 0


def bfs(r, c, color, graph):
    q = deque()
    q.append((r, c))
    graph[r][c] = 0
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[ny][nx] == color:
                    q.append((ny, nx))
                    graph[ny][nx] = 0
                    cnt += 1
    return cnt


for r in range(m):
    for c in range(n):
        if graph[r][c] != 0:
            if graph[r][c] == 'W':
                w += bfs(r, c, 'W', graph)**2
            else:
                b += bfs(r, c, 'B', graph)**2

print(w, b)
