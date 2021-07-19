n = int(input())
cnt = 0

while True:
    if(n%5==0):
        cnt += n//5
        print(cnt)
        break
    else:
        if(n//3!=0):
            n -= 3
            cnt += 1
            if(n==0):
                print(cnt)
                break
        else:
            print(-1)
            break