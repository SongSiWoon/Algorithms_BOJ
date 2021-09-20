import sys
from collections import Counter
input = sys.stdin.readline

n, m, b = map(int, input().split())
grand = []
for i in range(n):
    grand.extend(list(map(int, input().split())))
gc = Counter(grand)
result=[]

for j in range(max(gc.keys()), -1, -1):
    

