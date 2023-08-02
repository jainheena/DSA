#User function Template for python3

class Solution:
    def allPairs(self, A, B, N, M, X):
        # Your code goes here 
        A.sort()
        B.sort()
        i=0
        j=M-1
        k=0 
        ans=[]
        while i<N and j>=0:
            k=A[i]+B[j]
            if k==X:
                ans.append([A[i],B[j]])
                i+=1
                j-=1
            elif k>X:
                j-=1
            else:
                i+=1
            
        return ans
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        N, M, X = sz[0], sz[1], sz[2]
        A = [int(x) for x in input().strip().split()]
        B = [int(x) for x in input().strip().split()]
        ob=Solution()
        answer = ob.allPairs(A, B, N, M, X)
        sz = len(answer)

        if sz==0:
            print(-1)
        else:
            for i in range(sz):
                if i==sz-1:
                    print(*answer[i])
                else:
                    print(*answer[i],end=',')

        T-=1


if __name__ == "__main__":
    main()




# } Driver Code Ends