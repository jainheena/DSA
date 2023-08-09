import math
#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        ele=0
        count=0
        # Moore voting algo{maximium and minimum count will be equal till count reaches 0
        #  i.e. min=max when count =0 at each subarray and 
        # if maximum element is present end count will be greater than 0
        for i in range(N):
            if count==0:
                ele=A[i]
            if ele==A[i]:
                count+=1
            else:
                count-=1
        count=0
        for i in range(N):
            if ele==A[i]:
                count+=1
        if count>N/2:
            return ele
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends