String = input()
bomb = input()


def sol(String, bomb):
    ret = String
    while bomb in ret:
        tmp = ret.split(bomb)
        val = ''
        for s in tmp:
            val += s
        ret = val
    return ret if ret != '' else 'FRULA'


print(sol(String, bomb))
