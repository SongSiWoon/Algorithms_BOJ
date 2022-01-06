n, m = map(int, input().split())
lst = []


def sol(k):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    for i in range(k, n+1):
        lst.append(i)
        sol(i)
        lst.pop()


sol(1)
