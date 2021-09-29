T = int(input())
command = [input() for _ in range(T)]
for com in command:
    dir = 500
    x, y = 0, 0
    nx, ny = 0, 0
    mx, rx = 0, 0
    my, ry = 0, 0
    for c in com:
        d = dir % 4
        if c == 'F':
            if d == 0:
                ny = y + 1
            elif d == 1:
                nx = x + 1
            elif d == 2:
                ny = y - 1
            else:
                nx = x - 1
        elif c == 'B':
            if d == 0:
                ny = y - 1
            elif d == 1:
                nx = x - 1
            elif d == 2:
                ny = y + 1
            else:
                nx = x + 1
        elif c == 'L':
            dir -= 1
        else:
            dir += 1
        mx = max(mx, nx)
        rx = min(rx, nx)
        my = max(my, ny)
        ry = min(ry, ny)
        x = nx
        y = ny
    if rx<0:
        rx = mx -rx
    else:
        rx = mx
    if ry<0:
        ry = my - ry
    else:
        ry = my
    print(rx*ry)

