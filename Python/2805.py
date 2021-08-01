import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)
result = 0
while start<=end:
    mid = (end+start)//2
    target = 0
    target = sum(i-mid if i>=mid else 0 for i in tree)
    """for i in tree:
        if i>=mid:
            target += i - mid"""
    if target < m:
        end = mid-1
    else:
        result = mid
        start = mid+1
print(result)