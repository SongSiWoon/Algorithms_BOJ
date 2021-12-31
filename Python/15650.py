n, m = map(int, input().split())
lst = []


def sol(k):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    for i in range(k, n+1):
        if i not in lst:
            lst.append(i)
            sol(i+1)
            lst.pop()


sol(1)
