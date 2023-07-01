class Solution:

    def helper(candidates,target,i,curSum,temp,ans):

        if curSum > target:
            return

        if i==len(candidates):
            if curSum == target:
                ans.append(temp.copy())
            return
        
        #inclusion
        curSum+=int(candidates[i])
        temp.append(candidates[i])
        Solution.helper(candidates,target,i,curSum,temp,ans)
        curSum-=int(candidates[i])
        temp.pop()
        #exclusion
        Solution.helper(candidates,target,i+1,curSum,temp,ans)

        if curSum > target:
            return


    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        temp=[]
        ans=[]
        Solution.helper(candidates,target,0,0,temp,ans)
        return ans

#driver code runs  
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        candidates = input().strip().split(",")
        target = int(input())
        ob=Solution()
        print(ob.combinationSum(candidates,target))