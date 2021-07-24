import sys
n = int(input())

for i in range(n):
    str = sys.stdin.readline().strip()
    sum = 0
    if len(str)%2 !=0:
        print("NO")
        continue
    for s in str:
        if s == '(':
            sum+=1
        elif s == ')':
            sum-=1
        if sum<0:
            print("NO")
            break
    if sum ==0:
        print("YES")
    elif sum>0:
        print("NO")