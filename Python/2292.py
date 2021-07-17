n = int(input())
f = 2
cnt=1

while True:
    if(n == 1):
        print(1)
        break
    cnt += 1
    f = f+((cnt-2)*6)
    e = f+((cnt-1)*6)-1
    if(n>=f and n<=e):
        print(cnt)
        break