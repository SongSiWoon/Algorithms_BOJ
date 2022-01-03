expression = input()


def sol(ex):
    addex = ex.split('-')

    for i in range(len(addex)):
        tmp = addex[i].split('+')
        addex[i] = sum(list(map(int, tmp)))

    addex[1:] = map(lambda x: -1 * x, addex[1:])
    res = sum(addex)
    return res


print(sol(expression))
