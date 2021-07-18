import sys

n, m = map(int,input().split())
num = list(map(int,sys.stdin.readline().split()))
num = sorted(num, reverse=True)
sum = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if(num[i]+num[j]+num[k]>m):
                continue
            else:
                if(sum<num[i]+num[j]+num[k]):
                    sum = num[i]+num[j]+num[k]
                    
print(sum)

    
