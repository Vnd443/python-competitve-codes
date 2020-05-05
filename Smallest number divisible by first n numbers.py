# https://www.youtube.com/watch?v=PP75FwAX9DI for explaination

import fractions
    
def getSmallestDivNum(n):
    ans = 1
    for i in range(1, n+1):
        print(ans,i,ans*i,fractions.gcd(ans,i))

        ans=(ans*i)//fractions.gcd(ans,i)
       

    return int(ans)
a=int(input("enter Smallest number divisible by first n numbers"))
print(getSmallestDivNum(a))
