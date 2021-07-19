n, m = map(int,input().split())
gcdl = []
for i in range(1,min(n,m)+1):
    if(n%i==0 and m%i==0):
        gcdl.append(i)
gcd = max(gcdl)
lcm = m*n//gcd
print(gcd)
print(lcm)