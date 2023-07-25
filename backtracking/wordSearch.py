import pdb
class Solution:
    def helper(board,word,i,j,n,m,k):
        if k>=len(word):return True
        if i<0 or i>=n or j<0 or j>=m or board[i][j]=="." or word[k]!=board[i][j]:return False
        if len(word)==1 and word[k]==board[i][j]:return True
        board[i][j]="."
        temp = False
        x = [0,0,-1,1]
        y = [-1,1,0,0]
        for index in range(4):
            temp = temp or Solution.helper(board,word,i+x[index],j+y[index],n,m,k+1)
        
        board[i][j]=word[k]
        return temp
    
    def exist(self, board: list[list[str]], word: str) -> bool:
        n = len(board)
        if n==0:return False
        m=len(board[0])
        if len(word)==0:return False
        for i in range(n):
            for j in range(m):
                if word[0]==board[i][j]:
                    if Solution.helper(board,word,i,j,n,m,0):
                        return True
        return False
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        rows=int(input())
        board=[]
        for _ in range(rows):
            rd = input().split()
            board.append(rd)
        word = str(input())
        
        ans = Solution().exist(board,word)
        print(ans)
        