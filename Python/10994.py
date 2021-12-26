n = int(input())
size = 4*n-3
stars = [[' ']*size for _ in range(size)]


def sol(x, y, n):
    length = 4*n-3
    for i in range(4*n-3):
        stars[x][y+i] = '*'                  # 위
        stars[x+i][y] = '*'                  # 왼쪽
        stars[x + i][y + length - 1] = '*'   # 오른쪽
        stars[x + length - 1][y+i] = '*'     # 아래
    if n == 1:
        return
    sol(x+2, y+2, n-1)


sol(0, 0, n)
for star in stars:
    for s in star:
        print(s, end='')
    print()
