import sys

n = int(input())
nlst = list(map(int, sys.stdin.readline().split()))
m = int(input())
mlst = list(map(int, sys.stdin.readline().split()))
dic ={}
for i in nlst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for j in mlst:
    if j in dic:
        print(dic[j], end=" ")
    else:
        print(0, end=" ")