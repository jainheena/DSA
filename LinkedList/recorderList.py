from pyparsing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None or head.next==None:
            return
        mid=self.findMid(head)
        hs=self.reverseList(mid)
        hf=head
        while hs is not None and hf is not None:
            temp=hf.next
            hf.next=hs
            hf=temp

            temp=hs.next
            hs.next=hf
            hs=temp
        
        if hf is not None:
            hf.next=None
    
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
    
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