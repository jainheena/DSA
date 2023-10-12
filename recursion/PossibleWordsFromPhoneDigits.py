#User function Template for python3
import math

class Solution:

    def helper(a,n,temp,i,ans):
        keys =["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if i==n:
            ans.append(temp)
            return
        
        for j in range(len(keys[a[i]])):
            Solution.helper(a,n,temp+keys[a[i]][j],i+1,ans)

    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        #Your code here
        ans=[]
        Solution.helper(a,N,"",0,ans)
        return ans




#{ 
 # Driver Code Starts
#Initial Template for Python 3




def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split(",")]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends