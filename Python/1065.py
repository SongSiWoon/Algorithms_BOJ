n = int(input())
def hansu(n):
    count = 0
    for i in range(1,n+1):
        if i<100:
            count+=1
        else:
            a = [int(j) for j in str(i)]
            if a[0]-a[1] == a[1]-a[2]:
                count+=1
    print(count)
hansu(n)