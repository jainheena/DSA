class Node:
    def __init__(self,value):
        self.value=value
        self.next=None  
        self.prev=None

class DLL:
     
    def __init__(self):
        self.head=None
        self.size=0

    def elementAt(self,index):
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp
    
    def find(self,value):
        node=self.head
        index=0
        while node!=None:
            index+=1
            if node.value==value:
                print("The value",value,"is present at index",index)
                return node
            node=node.next
        print("Not present")

    def insertFirst(self,value):
        node=Node(value)
        node.value=value
        node.next=self.head
        node.prev=None
        if self.head!=None:
            self.head.prev=node
        self.head=node
        self.size+=1

    def insertLast(self,value):
        node=Node(value)
        node.value=value
        last=self.head
        while last.next!=None:
            last=last.next
        node.next=None
        last.next=node
        node.prev=last
        self.size+=1

    def insertAt(self,value,index):
        if index==0:
            self.insertFirst(value)
            return
        if index==self.size:
            self.insertLast(value)
            return
        node=Node(value)
        temp=self.head
        for i in range(index):
            temp=self.head.next
        node.next=temp.next
        if node.next!=None:
            temp.next.prev=node
        temp.next=node
        node.prev=temp
        self.size+=1

    def inserAfter(self,after,value):
        p=self.find(after)
        if p==None:
            print("doesn't exist")
            return
        node=Node(value)
        node.next=p.next
        p.next=node
        node.prev=p
        if node.next!=None:
            node.next.prev=node

    
    def deleteFirst(self):
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.head.prev=None
        self.size-=1
        del temp
    
    def deleteLast(self):
        if self.size<=1:
            return self.deleteFirst()
        secondLast=self.elementAt(self.size-2)
        last=self.elementAt(self.size)
        val=last.value
        print("deleted value:",val)
        secondLast.next=None
        del last
        self.size-=1

    def deleteAt(self,index):
        if index==0:
            self.deleteFirst()
            return
        if index==self.size:
            self.deleteLast()
            return
        temp=self.elementAt(index-2)
        node=temp.next
        temp.next=temp.next.next
        temp.next.prev=temp
        del node
        self.size-=1

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.value,"->",end=" ")
            temp=temp.next
        print("End")

    def displayRev(self):
        temp=self.head
        last=None
        while temp!=None:
            last=temp
            temp=temp.next
        print("Printing in reverse::")
        while last!=None:
            print(last.value,"->",end=" ")
            last=last.prev
        print("Start")

if __name__ == "__main__":
    ob=DLL()  
    ob.insertFirst(23)
    ob.insertFirst(45)
    ob.insertLast(1)
    ob.insertFirst(67)
    ob.insertLast(55)
    ob.insertAt(19,3)
    ob.inserAfter(45,33)
    ob.display()
    ob.deleteAt(3)
    ob.display() 