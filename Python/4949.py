import sys

while True:
    str = sys.stdin.readline().rstrip()
    cnt = []
    if str == ".":
        break
    for s in str:
        if s == '(' or s == '[':
            cnt.append(s)
        elif s == ')':
            if len(cnt) != 0 and cnt[-1] == '(':
                cnt.pop()
            else:
                cnt.append(s)
                break
        elif s == ']':
            if len(cnt) != 0 and cnt[-1] == '[':
                cnt.pop()
            else:
                cnt.append(s)
                break
    if len(cnt) == 0:
        print('yes')
    else:
        print('no')