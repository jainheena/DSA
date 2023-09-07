class Node:
    def __init__(self,value):
        self.value=value
        self.next=None  
    
class CLL:

    def __init__(self):
        self.head=None
        self.tail=None
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
            node=node.next
        return None

    def insertFirst(self,value):
        node=Node(value)
        if self.head==None:
            self.tail=node
            self.head=node
            self.size+=1
            return
        self.tail.next=node
        node.next=self.head
        self.head=node
        self.size+=1

    def insertLast(self,value):
        node=Node(value)
        if self.head==None:
            self.tail=node
            self.head=node
            self.size+=1
            return
        self.tail.next=node
        node.next=self.head
        self.tail=node
        self.size+=1

    def insertAt(self,index,value):
        if index==0:
                self.insertFirst(value)
                return
        if index==self.size:
            self.insertLast(value)
        for i in range(index):
                temp=self.head.next
        node=Node(value)
        node.next=temp.next
        temp.next=node
        self.size+=1

    def deleteFirst(self):
        if self.head==None:
            return None
        self.head=self.head.next
        self.tail.next=self.head
        self.size-=1

    def deleteLast(self):
        if self.head==None:
            return None
        for i in range(self.size-2):
            temp=self.head.next
        self.tail=temp
        self.tail.next=self.head
        self.size-=1

    def deleteAt(self,index):
        if index==0:
            return self.deleteFirst
        if index==self.size:
            return self.deleteLast
        node = self.elementAt(index-2)
        val = node.next.value
        node.next = node.next.next
        self.size -= 1
        print(val)

    def deleteVal(self,value):
        node=self.head
        if node==None:
            return
        if node.value==value:
            self.head=self.head.next
            self.tail.next=self.head
            self.size-=1
            return
        n=node.next
        if n.value==value:
            node.next=n.next
            self.size-=1
            return
        while(node!=self.head):
            if n.value==value:
                node.next=n.next
                self.size-=1
                return
            node=node.next


    def display(self):
        node=self.head
        if self.head!=None:
            print(node.value,"->",end=" ")
            node=node.next
            while node!=self.head:
                print(node.value,"->",end=" ")
                node=node.next
        print("Head")

if __name__ == "__main__":
    ob=CLL()
    ob.insertFirst(54)
    ob.insertFirst(74)
    ob.insertFirst(51)
    ob.insertLast(4)
    ob.insertFirst(3)
    ob.display()
    ob.deleteVal(51)
    ob.display()
