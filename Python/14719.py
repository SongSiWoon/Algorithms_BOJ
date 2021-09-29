h, w = map(int, input().split())
num = list(map(int, input().split()))
left = 0
right = w - 1
max_left = num[left]
max_right = num[right]
res = 0
while left < right:
    max_left = max(max_left, num[left])
    max_right = max(max_right, num[right])
    if max_right >= max_left:
        res += max_left-num[left]
        left += 1
    else:
        res += max_right - num[right]
        right -= 1
print(res)