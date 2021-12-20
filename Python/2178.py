from collections import deque
n, m = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
maze = [list(map(int, input().strip())) for _ in range(n)]


def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return maze[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1:
                    q.append((nx, ny))
                    maze[nx][ny] = maze[x][y] + 1


if __name__ == "__main__":
    print(bfs())
