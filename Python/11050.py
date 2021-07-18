n, k = map(int,input().split())

def factorial(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return n*factorial(n-1)

if(k>=0 and k<=n):
    result = factorial(n)/(factorial(k)*factorial(n-k))
elif(k<0):
    result = 0
elif(k>n):
    result = 0

print(int(result))
