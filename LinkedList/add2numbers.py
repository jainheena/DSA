#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def reverseList(self, head):
        # Code here
        if head is None:
            return head
            
        cur = head
        Next = head.next
        cur.next = None
        
        while Next is not None:
            temp = Next
            Next = Next.next
            temp.next = cur
            cur = temp
        
        return cur
    
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        first=self.reverseList(first)
        second=self.reverseList(second)
        dummy=Node()
        temp=dummy
        carry=0
        while(first or second or carry==1):
            sum=0
            if first is not None:
                sum+=first.data
                first=first.next
            
            if second is not None:
                sum+=second.data
                first=second.next
            sum+=carry #add sum and carry
            carry=sum/10 #carry is calculated by dividing sum by 10
            node=Node(sum%10) #create a new node with mode of sum by 10 and
            temp.next=node #point temp's next to new node created and then
            temp=temp.next #move temp one step ahead

        head=self.reverseList(dummy.next)
        return head            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends