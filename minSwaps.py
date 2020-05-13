def minSwaps(a,n):
    arrPos=[]

    for i in range(n):
        arrPos.append([a[i],i])
    arrPos.sort()

    vis=[0 for i in range(n)]

    ans=0

    for i in range(n):
        if(vis[i] or arrPos[i][1]==i):
            continue

        cycle_size=0
        j=i

        while(not vis[j]):
            vis[j]=1
            j=arrPos[j][1]
            cycle_size+=1
        ans+=cycle_size-1
    return ans
a=list(map(int,input().split()))
n=len(a)
print(minSwaps(a,n))

'''
ex- 4,3,2,1
o/p- 2
there 2 swaps occurs 
'''