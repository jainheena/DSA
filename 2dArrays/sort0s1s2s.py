#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        low=0
        mid=0
        high=n-1
        #dutch flag algorithm
        while mid<=high:
            if arr[mid]==0:
                arr[mid],arr[low]=arr[low],arr[mid] # if mid value is 0 swap it with low value
                mid+=1
                low+=1
            elif arr[mid]==1:
                mid+=1 # if mid value is 1 then no change and increase mid by 1
            else:
                arr[mid],arr[high]=arr[high],arr[mid] # if mid is 2 swap it with high value and decrease high by 1
                high-=1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends