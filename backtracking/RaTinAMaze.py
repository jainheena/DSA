#User function Template for python3

class Solution:
    def isSafe(m,visited,srcx,srcy,n):
        if srcx>=0 and srcy>=0 and srcx<n and srcy<n and m[srcx][srcy]==1 and not visited[srcx][srcy]:
            return True
        return False
    def helper(m,visited,n,srcx,srcy,temp,ans):
        if srcx==n-1 & srcy==n-1:
            ans.append(temp)
            return
        
        visited[srcx][srcy]=1
        if Solution.isSafe(m,visited,srcx+1,srcy,n):
            Solution.helper(m,visited,n,srcx+1,srcy,temp+"D",ans)
        
        if Solution.isSafe(m,visited,srcx,srcy-1,n):
            Solution.helper(m,visited,n,srcx,srcy-1,temp+"L",ans)
        
        if Solution.isSafe(m,visited,srcx,srcy+1,n):
            Solution.helper(m,visited,n,srcx,srcy+1,temp+"R",ans)
        
        if Solution.isSafe(m,visited,srcx-1,srcy,n):
            Solution.helper(m,visited,n,srcx-1,srcy,temp+"U",ans)

        visited[srcx][srcy]=0
        
        
    def findPath(self, m, n):
        # code here
        ans=[]
        if m[0][0]==0:
            return ans
        visited=[[0]*n for _ in range(n)]
        Solution.helper(m,visited,n,0,0,"",ans)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends