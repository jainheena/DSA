class Solution():
	def reverse(self,arr,n):
		for i,j in zip(range(n),range(n-1,n//2,-1)):
			temp=arr[i]
			arr[i]=arr[j]
			arr[j]=temp
		print(arr,end="")
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		ob.reverse(arr, n) 
# } Driver Code Ends