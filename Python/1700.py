n, k = map(int, input().split())
arr = list(map(int, input().split()))
plug = []
res = 0
for i in range(k):
    if arr[i] in plug:
        continue
    if len(plug) < n:
        plug.append(arr[i])
        continue
    idx = []
    check = True
    for j in plug:
        if j in arr[i:]:
            tmp = arr[i:].index(j)
        else:
            tmp = 101
            check = False
        idx.append(tmp)
        if not check:
            break
    out = idx.index(max(idx))
    del plug[out]
    plug.append(arr[i])
    res += 1
print(res)