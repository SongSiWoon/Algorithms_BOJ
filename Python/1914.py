N = int(input())


def sol(n, start, end, mid):
    if n == 1:
        print(start, end)
        return
    sol(n-1, start, mid, end)
    print(start, end)
    sol(n-1, mid, end, start)


print(2**N - 1)
if N <= 20:
    sol(N, 1, 3, 2)
