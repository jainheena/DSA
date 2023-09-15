from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or head is None:
            return head
        
        current = head
        prev = None
        
        # Check if there are at least k nodes left in the list
        count = 0
        temp = head
        while count < k and temp:
            temp = temp.next
            count += 1
        
        if count < k:
            return head  # Not enough nodes left to reverse
        
        count = 0
        while count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1
        for i in range(k):
            if current is not None:
                prev=current
                current=current.next
        head.next = self.reverseKGroup(current, k)
        return prev.val

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
        print(ob.reverseKGroup(LL.head,3))
        