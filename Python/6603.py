def BackTracking(pos, n, visit, li):
    if len(li) == 6:
        for i in li:
            print(i, end=' ')
        print()
        return
    for i in range(pos, len(n)):
        if not visit[i]:
            visit[i] = True
            li.append(n[i])
            BackTracking(i,n,visit,li)
            li.pop()
            visit[i] = False
while True:
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        break
    T = tmp[0]
    num = tmp[1:]
    res = []
    visit = [False]*T
    BackTracking(0, num, visit, res)
    print()