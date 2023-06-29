#User function Template for python3

class Solution:
    def helper(s,tempAns,index):
        if index==len(s):
            print(tempAns)
            return
        #take
        Solution.helper(s,tempAns+s[index],index+1)
        #notTake
        Solution.helper(s,tempAns,index+1)
    def AllPossibleStrings(self, s):
		# Code ans
        self.ans=[]
        Solution.helper(s,"",0)
        return sorted(self.ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends