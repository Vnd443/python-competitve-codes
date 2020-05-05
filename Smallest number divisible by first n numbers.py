# Returns the lcm of first n numbers 
import fractions
    
def getSmallestDivNum(n):
    #RETURN ans
    ans = 1
    for i in range(1, n+1):
        print(ans,i,ans*i,fractions.gcd(ans,i))

        ans=(ans*i)//fractions.gcd(ans,i)
        #print(ans,fractions.gcd(ans,i))

    return int(ans)
a=int(input("enter Smallest number divisible by first n numbers"))
print(getSmallestDivNum(a))