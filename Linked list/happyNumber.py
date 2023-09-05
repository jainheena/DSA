class Solution:
    def isHappy(self, n):
        slow=n
        fast=n
        slow=self.numSquare(slow)
        fast=self.numSquare(self.numSquare(fast))
        while slow!=fast:
            slow=self.numSquare(slow)
            fast=self.numSquare(self.numSquare(fast))

        if slow==1:
            return True
        else:
            return False

    def numSquare(self,num):
        ans=0
        while num>0:
            rem=num%10
            ans+=rem*rem
            num=num//10
        return ans
        

if __name__ == "__main__":
    ob=Solution()
    n=int(input())
    print(ob.isHappy(n))