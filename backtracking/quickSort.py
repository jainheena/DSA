class Solution:
    @staticmethod
    def swap(a, b, arr):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

    def quickSort(self, arr, low, high):
        if low < high:
            part = self.partition(arr, low, high)
            self.quickSort(arr, low, part - 1)
            self.quickSort(arr, part + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i=low+1
        j = high

        for j in range(high,pivot+1,-1):
            if arr[j]<pivot:
                i+=1
                Solution.swap(i, j, arr)

        Solution.swap(low, j, arr)
        return j


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        Solution().quickSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
