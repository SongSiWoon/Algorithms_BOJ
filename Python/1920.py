import sys

def binarysearch(arr, target, start, end):
    if start>end:
        return None
    mid = (start + end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarysearch(arr,target,start,mid-1)
    else:
        return binarysearch(arr,target,mid+1,end)

n = int(input())
a=[int(x) for x in sys.stdin.readline().strip().split()]
m = int(input())
b=[int(x) for x in sys.stdin.readline().strip().split()]
a.sort()

for i in range(m):
    if(binarysearch(a,b[i],0,n-1)!=None):
        print(1)
    else:
        print(0)




    
