def Factorial(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result

n = int(input())
cnt = 0
for i in reversed(str(Factorial(n))) :
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)