n = int(input())
num = list(map(int, input().split()))
cnt = 0
arrow = [0]*(max(num)+1)
for i in num:
    if arrow[i] == 0:
        arrow[i-1] += 1
        cnt += 1
    else:
        arrow[i] -= 1
        arrow[i-1] += 1
print(cnt)