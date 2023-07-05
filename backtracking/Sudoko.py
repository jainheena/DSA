#User function Template for python3

class Solution:

    def check(grid,row,col,num):
        #row
        for i in range(9):
            if grid[i][col]==num:
                return False
        #col
        for j in range(9):
            if grid[row][j]==num:
                return False
        #box
        ini = row-row%3
        inj = col-col%3
        for i in range(3):
            for j in range(3):
                if grid[ini+i][inj+j]==num:
                    return False
        return True

    def helper(grid,row,col):
        if row==9:return True
        if col==9:return Solution.helper(grid,row+1,0)
        if grid[row][col]!=0:return Solution.helper(grid,row,col+1)
        for i in range(1,10):
            if Solution.check(grid,row,col,i):
                grid[row][col]=i
                if Solution.helper(grid,row,col+1):
                    return True
            grid[row][col]=0
        return False
    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        return Solution.helper(grid,0,0)
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,grid):
        # Your code here
        self.SolveSudoku(grid)
        for i in range(9):
            for j in range(9):
                print(grid[i][j],end=" ")

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends