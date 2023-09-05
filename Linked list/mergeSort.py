from pyparsing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        mid=self.findMid(head)
        left=self.sortList(head)
        right=self.sortList(mid)
        return self.sortedMerge(left,right)

    def sortedMerge(self,head1, head2):
    # code here
        dummy=ListNode()
        tail=dummy
        
        while head1!=None and head2!=None:
            if head1.val<head2.val:
                tail.next=head1
                head1=head1.next
                tail=tail.next
            else:
                tail.next=head2
                head2=head2.next
                tail=tail.next
        if head1!=None:
            tail.next=head1
        else:
            tail.next=head2

        return dummy.next
    
    def findMid(self,head):
        midPrev=None
        while head!=None and head.next!=None:
            if midPrev==None:
                midPrev=head
            else:
                midPrev=midPrev.next
            head=head.next.next
        mid=midPrev.next
        midPrev.next=None
        return mid