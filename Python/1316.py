import sys

n = int(input())
cnt = n
for i in range(n):
    s = sys.stdin.readline()
    for j in range(len(s)-1):
        if s[j] == s[j+1]:
            pass
        else:
            if s[j] in s[j+1:]:
                cnt -=1
                break
print(cnt)

