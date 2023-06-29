#User function Template for python3

class Solution:
    def helper(self,A,ans,temp,index):
        if index == len(A):
            ans.append(temp.copy())
            return
        temp.append(A[index])
        self.helper(A,ans,temp,index+1)
        temp.pop()
        self.helper(A,ans,temp,index+1)
        return ans
    
    def subsets(self, A):
        #code here
        ans = []
        temp = []
        index = 0
        
        ans = self.helper(A,ans,temp,index)
        return sorted(ans)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends