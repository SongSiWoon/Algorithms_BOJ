String = input()
bomb = input()


def sol(String, bomb):
    stack = []
    blen = len(bomb)
    for s in String:
        stack.append(s)
        if s == bomb[-1]:
            tmp = ''
            for i in stack[-blen:]:
                tmp += i
            if tmp == bomb:
                for i in range(blen):
                    stack.pop()
    res = ''.join(stack)
    return res if res != '' else 'FRULA'


print(sol(String, bomb))
