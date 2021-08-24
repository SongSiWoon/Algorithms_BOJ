from collections import deque
n, k = map(int, input().split())

def bfs(n, k):

    q = deque([n])
    visited = [0] * (10**5+1)
    while q:
        idx = q.popleft()
        if idx == k:
            print(visited[idx])
            return
        for i in (idx-1,idx+1,idx*2):
            if 0 <= i < (10**5+1) and not visited[i]:
                visited[i] = visited[idx] + 1
                q.append(i)
bfs(n, k)