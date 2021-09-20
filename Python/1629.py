a, b, c = map(int, input().split())
def pow(n, m):
    if m == 1:
        return n % c
    else:
        ret = pow(n, m // 2)
        if m % 2 == 0:
            return ret * ret % c
        else:
            return ret * ret * n % c
print(pow(a,b))