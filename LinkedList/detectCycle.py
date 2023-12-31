#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
            return False
    
    def countNodesinLoop(head):
    #Your code here
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                temp=slow
                temp=temp.next
                length=1
                while temp!=slow:
                    temp=temp.next
                    length+=1
                return length
        return 0
    
    def findFirstNode(self, head):
        #code here
        length=0
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                length=Solution.countNodesinLoop(slow)
                break
        if length==0:
            return -1
        s=head
        f=head
        while length>0:
            s=s.next
            length-=1

        while f!=s:
            s=s.next
            f=f.next
        return s.data


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
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
    
    #connects last node to node at position pos from begining.
    def loopHere(self,pos):
        if pos==0:
            return
        
        walk = self.head
        for i in range(1,pos):
            walk = walk.next
        
        self.tail.next = walk

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))
        
        LL.loopHere(int(input()))
        
        print(Solution().findFirstNode(LL.head))
# } Driver Code Ends