#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        # code here
        F=[1,2]
        if n==1 or n==2:
            return n
        for i in range(2,n): 
            res=F[i-2]+F[i-1] #base case because for 1 stair res is 1 and for 2 result is 2 nd we can get result for n stairs by adding up the base cases forming it into recursive tree.
            F.append(res)
        result=F[n-1]%1000000007
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends