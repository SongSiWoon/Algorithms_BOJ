total, win = map(int, input().split())
wrate = win * 100 // total
res = 0
start = 1
end = 1000000000

if wrate >= 99:
    print(-1)

else:
    while start <= end:
        mid = (start + end) // 2
        tmp = (win + mid) * 100 // (total + mid)
        if wrate >= tmp:
            start = mid + 1
        else:
            res = mid
            end = mid - 1

    print(res)
