brakcets = list(input().strip())


def check(brakcets):
    stack = []
    for b in brakcets:
        if b in ('(', '['):
            stack.append(b)
        elif b in (')', ']'):
            if len(stack) == 0:
                return False
            tmp = stack.pop()
            if b == ')':
                if tmp != '(':
                    return False
            elif b == ']':
                if tmp != '[':
                    return False
    return False if stack else True


def sol(brakcets):
    stack = []
    for b in brakcets:
        if b in ('(', '['):
            stack.append(b)
        elif b == ')':
            tmp = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    if tmp == 0:
                        stack.append(2)
                    else:
                        stack.append(2*tmp)
                    break
                else:
                    if tmp == 0:
                        tmp = int(top)
                    else:
                        tmp += int(top)
        elif b == ']':
            tmp = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    if tmp == 0:
                        stack.append(3)
                    else:
                        stack.append(3*tmp)
                    break
                else:
                    if tmp == 0:
                        tmp = int(top)
                    else:
                        tmp += int(top)
    return sum(stack)


if __name__ == "__main__":
    if check(brakcets):
        print(sol(brakcets))
    else:
        print(0)
