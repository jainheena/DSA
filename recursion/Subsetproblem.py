#User function Template for python3

class Solution:
    
    def helper(a,sum,tempSum,i):
        if sum==tempSum:
            return True
        
        if i>=len(a):
            return False
            
        recCall1=Solution.helper(a,sum,tempSum+a[i],i+1)
        recCall2=Solution.helper(a,sum,tempSum,i+1)
        
        return recCall1 or recCall2
    
    def isSubsetSum (self, N, arr, sum):
        # code here
        return Solution.helper(arr,sum,0,0)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends