#User function Template for python3
class Solution:
    def helper(s,start,end):
		
            if(start>=end):
                return 1
            if(s[start]!=s[end]):
                return 0
            return Solution.helper(s,start+1,end-1)

    def isPalindrome(self, S):
          n = len(S)-1
          return Solution.helper(S,0,n)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends