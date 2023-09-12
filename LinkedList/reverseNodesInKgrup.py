from pyparsing import Optional


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
        
        head.next = self.reverseKGroup(current, k)
        
        return prev
