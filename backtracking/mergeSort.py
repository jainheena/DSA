class Solution:

    def merge(A,B):
        sizeA = len(A)
        sizeB = len(B)
        i=0
        j=0
        ans=[]
        print(A)
        print(B)
        while i<sizeA and j<sizeB:
            if A[i]<B[j]:
                ans.append(A[i])
                i=i+1
            else:
                ans.append(B[j])
                j=j+1

        while i<sizeA:
            ans.append(A[i])
            i=i+1
        
        while j<sizeB:
            ans.append(B[j])
            j=j+1
        
        return ans
        

    def mergeSort(nums,start,end):
        if start>end:
            return [0]
        if start==end:
            return [nums[start]]
        
        mid =  start + (end-start)//2

        A=Solution.mergeSort(nums,start,mid)
        B=Solution.mergeSort(nums,mid+1,end)
        print(type(A))

        return Solution.merge(A,B)

    def sortArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        return Solution.mergeSort(nums,0,n-1)
    
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        nums = input().strip().split(",")
        ob = Solution()
        ans = ob.sortArray(nums)
        print(ans)