num = int(input())
cnt = 1

while True:
    s=[]
    for i in str(cnt):
        s.append(i)
    dp = sum(map(int,s))+cnt

    if(num == dp):
        print(cnt)
        break
    if(cnt == num):
        print(0)
        break
    cnt +=1