#User function Template for python3
import copy
class Solution:
	def MakeZeros(self, matrix):
		n=len(matrix)
		m=len(matrix[0])
		temp=copy.deepcopy(matrix)
		for i in range(n):
			for j in range(m):
				if temp[i][j]==0:
					if i+1<n:
						matrix[i][j]+=temp[i+1][j]
						print(temp[i+1][j])
						matrix[i+1][j]=0
					if i-1>=0:
						matrix[i][j]+=temp[i-1][j]
						matrix[i-1][j]=0
					if j+1<m:
						matrix[i][j]+=temp[i][j+1]
						matrix[i][j+1]=0
					if j-1>=0:
						matrix[i][j]+=temp[i][j-1]
						matrix[i][j-1]=0
		#code here
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m)
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ob.MakeZeros(matrix)
		for i in range(n):
			for j in range(m):
				print(matrix[i][j], end = " ")
			print()
# } Driver Code Ends