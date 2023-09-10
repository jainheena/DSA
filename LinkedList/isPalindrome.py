#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        mid=self.findMid(head)
        headSecond=self.reverseList(mid)
        reReverseHead=headSecond

        while head!=None and headSecond!=None:
            if head.data!=headSecond.data:
                break
            head=head.next
            headSecond=headSecond.next
        
        self.reverseList(reReverseHead)
        
        return head==None or headSecond==None    
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


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

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
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if Solution().isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends