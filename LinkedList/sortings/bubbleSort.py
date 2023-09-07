class Node:
    def __init__(self,value):
        self.value=value
        self.next=None  
    
class LL:

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def elementAt(self,index):
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp
    
    def insertFirst(self,value):
        node=Node(value)
        node.value=value
        node.next=self.head
        self.head=node
        if self.tail==None:
            self.tail=self.head
        self.size+=1

    def bubbleSort(self,row,col):
        if row==0:
            return
        
        if col<row:
            first=self.elementAt(col)
            second=self.elementAt(col+1)
            if first.value>second.value:
                #swap
                if first==self.head:
                    self.head=second
                    first.next=second.next
                    second.next=first
                elif second==self.tail:
                    prev=self.elementAt(col-1)
                    prev.next=second
                    self.tail=first
                    first.next=None
                    second.next=self.tail
                else:
                    prev=self.elementAt(col-1)
                    prev.next=second
                    first.next=second.next
                    second.next=first
            self.bubbleSort(row,col+1)
        else:
            self.bubbleSort(row-1,0)

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.value,"->",end=" ")
            temp=temp.next
        print("END")


if __name__ == "__main__":
    ob=LL()
    ob.insertFirst(6)
    ob.insertFirst(7)
    ob.insertFirst(8)
    ob.insertFirst(9)
    ob.insertFirst(10)
    ob.display()
    ob.bubbleSort(ob.size-1,0)
    ob.display()