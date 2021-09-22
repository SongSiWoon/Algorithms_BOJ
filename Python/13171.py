a = int(input())
x = int(input())
mod = 1000000007
def power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        x = power(a, n // 2)%mod
        return x * x % mod
    return (a * power(a, n-1))%mod
print(power(a,x))