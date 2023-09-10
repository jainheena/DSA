from pyparsing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current=head
        prev=None
        for i in range(left-1):
            if current is not None:
                prev=current
                current=current.next
        last=prev
        newend=current
        next=current.next
        for i in range(right-left+1):
            if current is not None:
                current.next=prev
                prev = current
                current=next
                if next is not None:
                    next=next.next
        
        if last is not None:
            last.next = prev
        else:
            head=prev

        newend.next =current
        return head