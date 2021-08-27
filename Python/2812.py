n, k = map(int, input().split())
s = input()
num = []
cnt=k
num.append(int(s[0]))
for i in range(1, n):
    if k==0:
        num.append(int(s[i:]))
        break
    while num and num[-1]<int(s[i]) and cnt>0:
        num.pop()
        cnt -= 1
    num.append(int(s[i]))
for i in range(n-k):
    print(num[i], end="")