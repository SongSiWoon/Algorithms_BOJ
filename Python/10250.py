import sys
T = int(input())

for i in range(T):
    a = list(map(int,sys.stdin.readline().split()))
    if(a[2]%a[0]!=0):
        room = (a[2]%a[0])*100+(a[2]//a[0]+1)
    else:
        room = a[0]*100 + a[2]//a[0]
    print(room)
