n, price = map(int, input().split())
coin = list(int(input()) for _ in range(n))


def sol(price):
    res = 0
    tmp = price

    for c in reversed(coin):
        res += tmp//c
        tmp %= c

    return res


print(sol(price))
