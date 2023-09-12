#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def swap(self,nums,i,j):
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
        
    def quickSort(self,arr,low,high):
        # code here
        if low<high:
            part=self.partition(arr,low,high)
            self.quickSort(arr,low,part-1)
            self.quickSort(arr,part+1,high)
    
    def partition(self,arr,low,high):
        # code here
        pivot=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<pivot:
                i+=1
                self.swap(arr,i,j)
        self.swap(arr,i+1,high)
        return i+1
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends