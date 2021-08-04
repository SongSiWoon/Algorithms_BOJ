import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sstr = set()
lstr = set()
result = []
for i in range(n):
    lstr.add(input().strip())
for j in range(m):
    sstr.add(input().strip())
result = list(sstr & lstr)

print(len(result))
for k in sorted(result):
    print(k)