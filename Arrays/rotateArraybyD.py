#User function Template for python3

class Solution:
    def reverse(A,start,end):
        while start<end:
            temp=A[start]
            A[start]=A[end]
            A[end]=temp
            start+=1
            end-=1
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        D=D%N
        Solution.reverse(A,0,D-1)
        Solution.reverse(A,D,N-1)
        Solution.reverse(A,0,N-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends