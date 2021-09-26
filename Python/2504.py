stack = []
res = 0
li = list(input())
for i in li:
    if i == ')':
        tmp = 0
        while stack:
            ret = stack.pop()
            if ret == '(':
                if tmp == 0:
                    stack.append(2)
                else:
                    stack.append(2*tmp)
                break
            elif ret == '[':
                print(0)
                exit()
            else:
                if tmp == 0:
                    tmp = int(ret)
                else:
                    tmp += int(ret)
    elif i == ']':
        tmp = 0
        while stack:
            ret = stack.pop()
            if ret == '[':
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3*tmp)
                break
            elif ret == '(':
                print(0)
                exit()
            else:
                if tmp == 0:
                    tmp = int(ret)
                else:
                    tmp += int(ret)
    else:
        stack.append(i)

for i in stack:
    if i == '(' or i == '[':
        print(0)
        exit()
    else:
        res += i
print(res)