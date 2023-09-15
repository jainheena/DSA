from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k<=0 or head==None or head.next==None:
            return head
        
        last=head
        length=1
        while last.next is not None:
            last=last.next
            length+=1
        last.next=head
        rotations=k%length
        skip=length-rotations
        newLast=head
        for i in range(skip-1):
            newLast=newLast.next

        head=newLast.next
        newLast.next=None
        return head

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))
        ob=Solution()
        print(ob.rotateRight(LL.head,3)) 