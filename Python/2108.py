import sys
from collections import Counter

def average(list):
    return round(sum(list)/len(list))
def mid(list):
    return list[len(list)//2]
def mode(list):
    cnt = Counter(list).most_common()
    if len(list) == 1:
        return list[0]
    else:
        if cnt[0][1] == cnt[1][1]:
            return cnt[1][0]
        else:
            return cnt[0][0]
def ran(list):
    return list[-1] - list[0]


n= int(input())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
print(average(num))
print(mid(num))
print(mode(num))
print(ran(num))