import sys

a = int(input())
n = 0
for i in range(a):
    score = list(map(int, sys.stdin.readline().split()))
    average = sum(score[1:])/score[0]
    for j in score[1:]:
        if average < j:
            n += 1
    print("%.3f%%"%((n/score[0])*100))
    n = 0
