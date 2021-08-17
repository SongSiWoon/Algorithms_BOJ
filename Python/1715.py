from queue import PriorityQueue

n = int(input())
num = PriorityQueue()
for i in range(n):
    num.put(int(input()))
result = 0
while (num.qsize())>1:
    x = num.get()
    y = num.get()
    result += (x+y)
    num.put(x+y)
print(result)