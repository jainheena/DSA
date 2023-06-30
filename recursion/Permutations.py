from ast import List


class Solution:
    def permute(self, nums):
        ans=[]

        def helper(nums,i):
            #base case
            if i==len(nums):
                adc = nums.copy()
                ans.append(adc)
                return
        
            for j in range(i,len(nums)):
                #swapping
                nums[i],nums[j]=nums[j],nums[i]
                #recursion
                helper(nums,i+1)
                #backtrack
                nums[i],nums[j]=nums[j],nums[i]
        helper(nums,0)
        return ans