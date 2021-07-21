import sys
n = int(input())
num = list(map(int,sys.stdin.readline().split()))
cnt = 0

for i in num:
    if(i==1):
        continue
    if(i==2):
        cnt+=1
        continue
    c = 0
    for j in range(2,i):
        if(i%j==0):
            c+=1
    if(c==0):
        cnt+=1
print(cnt)