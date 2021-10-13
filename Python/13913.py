from collections import deque
MAX = 100001
n, k = map(int, input().split())
visited = [0] * MAX
move = [0] * MAX
ans = []
def bfs(p, g):
    q = deque()
    q.append(p)
    while q:
        x = q.popleft()
        if x == g:
            cnt = visited[x]
            while x != n:
                ans.append(x)
                x = move[x]
            ans.append(n)
            return cnt
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < MAX and not visited[nx]:
                visited[nx] = visited[x] + 1
                move[nx] = x
                q.append(nx)
res = bfs(n,k)
print(res)
for i in range(len(ans)-1, -1, -1):
    print(ans[i], end=' ')