from collections import deque
n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


def DFS(graph, v, visted):
    visited[v] = True
    print(v, end= ' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)
def BFS(graph, v, visted):
    queue = deque([v])
    visited[v] = False
    while queue:
        val = queue.popleft()
        print(val, end=' ')
        for i in graph[val]:
            if visited[i]:
                queue.append(i)
                visited[i] = False

DFS(graph, v, visited)
print()
BFS(graph, v, visited)