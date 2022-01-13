import heapq
import sys
input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N):
    tmp = int(input())
    if tmp == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, tmp)
