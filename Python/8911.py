T = int(input())
command = [input() for _ in range(T)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for com in command:
    pos_x = 0
    pos_y = 0
    pos_dir = 0
    pos = [(0,0)]
    for c in com:
        if c == 'F':
            pos_x = pos_x + dx[pos_dir]
            pos_y = pos_y + dy[pos_dir]
        elif c == 'B':
            pos_x = pos_x - dx[pos_dir]
            pos_y = pos_y - dy[pos_dir]
        elif c == 'L':
            if pos_dir == 3:
                pos_dir = 0
            else:
                pos_dir += 1
        else:
            if pos_dir == 0:
                pos_dir = 3
            else:
                pos_dir -= 1
        pos.append((pos_x, pos_y))
    if min(pos, key = lambda x: x[0])[0]<0:
        width = max(pos, key=lambda x: x[0])[0] - min(pos, key=lambda x: x[0])[0]
    else:
        width = max(pos, key=lambda x: x[0])[0]
    if min(pos, key=lambda x: x[1])[1]:
        height = max(pos, key=lambda x: x[1])[1] - min(pos, key=lambda x: x[1])[1]
    else:
        height = max(pos, key=lambda x: x[1])[1]
    print(width * height)

