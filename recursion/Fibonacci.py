#User function Template for python3

class Solution:
    def nthFibonacci(self, n):
        # code here 
        F = [1,1]
        for i in range(2,n):
            k = F[i-1]+F[i-2]
            F.append(k)
        return F[n-1]%1000000007
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthFibonacci(n))
# } Driver Code Ends