n, m = map(int, input().split())
lst = []


def sol():
    if len(lst) == m:
        print(" ".join(map(str,lst)))
        return
    for i in range(1, n+1):
        lst.append(i)
        sol()
        lst.pop()


sol()
