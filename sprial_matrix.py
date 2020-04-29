def sprialmatx(l,n):
    a=b=n
    c=0
    d=0
    v=1 #values

    ''' c - starting row index 
        a - ending row index 
        d - starting column index 
        b - ending column index 
        i - iterator '''
    while c<a and d<b:

        # Print the first row from
        # the remaining rows
        for i in range(d,b):
            l[c][i]=v
            v+=1
        c+=1

        # Print the last column from
        # the remaining columns
        for i in range(c,a):
            l[i][b-1]=v
            v+=1
        b-=1

        # Print the last row from
        # the remaining rows
        if c<a:
            for i in range(b-1,d-1,-1):
                l[a-1][i]=v
                v+=1
            a-=1
        # Print the first column from
        # the remaining columns
        if d<b:
            for i in range(a-1,c-1,-1):
                l[i][d]=v
                v+=1
            d+=1

    return l


n=int(input("Enter the size of martix:"))
l = [[0] * n for p in range(n)]

aa=sprialmatx(l,n)
for i in l:
    print(i)
