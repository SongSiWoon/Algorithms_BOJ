x,y,w,h = map(int,input().split())

num = [x, y, w-x, h-y]
print(min(num))

