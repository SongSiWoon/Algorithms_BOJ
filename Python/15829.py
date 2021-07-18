L = int(input())
num = list(map(ord,input()))
H = 0
for i in range(L):
    H += ((num[i]-96)*(31**i))
print(H%1234567891)