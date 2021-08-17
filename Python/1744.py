n = int(input())
pnum = []
nnum = []
sum = 0
for i in range(n):
    x = int(input())
    if x >1:
        pnum.append(x)
    elif x <1:
        nnum.append(x)
    else:
        sum += 1
pnum.sort(reverse=True)
nnum.sort()

if len(pnum) % 2 == 0:
    for i in range(0, len(pnum), 2):
        sum += pnum[i] * pnum[i+1]
else:
    for i in range(0, len(pnum)-1, 2):
        sum += pnum[i] * pnum[i+1]
    sum += pnum[-1]
if len(nnum) % 2 == 0:
    for i in range(0, len(nnum), 2):
        sum += nnum[i] * nnum[i+1]
else:
    for i in range(0, len(nnum)-1, 2):
        sum += nnum[i] * nnum[i+1]
    sum += nnum[-1]
print(sum)