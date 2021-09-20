import sys
input = sys.stdin.readline

n = int(input())
str = []
for i in range(n):
    str.append(input().rstrip())
dic = {}
for s in str:
    l = len(s)-1
    for i in s:
        if i in dic:
            dic[i] += (10 ** l)
        else:
            dic[i] = (10 ** l)
        l -= 1

num = []
for i in dic.values():
    num.append(i)
num.sort(reverse=True)
result =0
scale = 9
for i in range(len(num)):
    result += num[i]*scale
    scale -= 1
print(result)