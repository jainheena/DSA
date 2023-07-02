#User function Template for python3


class Solution:

    def isSafe(board,r,c,n):
        for i in range(r):
            if board[i][c]==1:
                return False
    
        for i,j in zip(range(r-1,-1,-1) , range(c-1,-1,-1)):
            if board[i][j]==1:
                return False
        
        for i,j in zip(range(r-1,-1,-1) , range(c+1,n)):
            if board[i][j]==1:
                return False
            
        return True

    def helper(board,n,r,ans,temp):
        if r==n:
            for i in range(n):
                for j in range(n):
                    if board[i][j]==1:
                        temp.append(j+1)
            ans.append(temp.copy())
            for i in range(n):
                temp.pop()
            return
        
        for i in range(n):
            if Solution.isSafe(board,r,i,n):
                board[r][i]=1
                Solution.helper(board,n,r+1,ans,temp)
                board[r][i]=0
        
    
    def nQueen(self, n):
        # code here
        ans=[]
        temp=[]
        size = n
        board = [[0] * size for _ in range(size)]
        Solution.helper(board,n,0,ans,temp)
        return ans
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends