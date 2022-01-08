N = int(input())
col = [0] * N
cnt = 0


def checkconflict(r, col):
    for i in range(r):
        if col[r] == col[i]:  # 열 체크
            return False
        if abs(col[r] - col[i]) == r - i:  # 대각선 체크
            return False
    return True


def sol(r, col):
    global cnt
    if r == N:
        cnt += 1
        return
    else:
        for c in range(N):
            col[r] = c
            if checkconflict(r, col):
                sol(r+1, col)
    return cnt


print(sol(0, col))
