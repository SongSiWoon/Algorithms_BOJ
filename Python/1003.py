import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    cnt0 = [1, 0]
    cnt1 = [0, 1]
    n = int(input())
    if n == 0:
        print("1 0")
    elif n == 1:
        print("0 1")
    else:
        for j in range(2, n+1):
            cnt0.append(cnt0[j-1] + cnt0[j - 2])
            cnt1.append(cnt1[j-1] + cnt1[j - 2])
        print(cnt0[-1], end=" ")
        print(cnt1[-1])