from collections import deque
n, k = map(int, input().split())

def bfs(n, k):
    q = deque([(n, 0)])
    visited = [0] * (10**5 + 1)
    cnt = 0
    res_t = 10**6
    while q:
        num, t = q.popleft()
        if t>res_t:
            break
        if num == k:
            res_t = t
            if not visited[num]:
                visited[num] = t
                cnt += 1
            else:
                if t == visited[num]:
                    cnt += 1

        for i in (num-1,num+1,num*2):
            if 0 <= i < (10**5 + 1):
                if not visited[i] or visited[i] >= t+1:
                    visited[i] = t + 1
                    q.append((i, t+1))
    print(res_t)
    print(cnt)
    print((10**5 + 1))
    print((10**5+1))
    return
bfs(n, k)