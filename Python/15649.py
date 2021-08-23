n, m = map(int, input().split())
visted = [False] * (n+1)
res = []
def dfs():
    if len(res) == m:
        for i in res:
            print(i, end =' ')
        print()
        return

    for j in range(1, n+1):
        if not visted[j]:
            visted[j] = True
            res.append(j)
            dfs()
            res.pop()
            visted[j] = False
dfs()