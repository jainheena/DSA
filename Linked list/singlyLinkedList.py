
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

    def insertLast(self,value):
        if self.tail==None:
            self.insertFirst(value)
            return
        node=Node(value)
        node.value=value
        self.tail.next=node
        self.tail=node
        self.size+=1

    def insertAt(self,value,index):
            if index==0:
                self.insertFirst(value)
                return
            if index==self.size:
                self.insertLast(value)
            temp=self.head
            for i in range(index):
                temp=self.head.next
            node=Node(value)
            node.value=value
            node.next=temp.next
            temp.next=node
            self.size+=1

    def deleteFirst(self):
        temp=self.head
        self.head=self.head.next
        del temp
        self.size-=1
    
    def deleteLast(self):
        if self.size<=1:
            return self.deleteFirst()
        sL=self.size-2
        secondLast=self.elementAt(sL)
        val=self.tail.value
        self.tail=secondLast
        self.tail.next=None
        self.size-=1
        print(val)

    def deleteAt(self,index):
        if index==0:
            self.deleteFirst()
            return
        if index==self.size:
            self.deleteLast()
            return
        prev = self.elementAt(index - 1)
        val = prev.next.value
        prev.next = prev.next.next
        self.size -= 1
        self.size-=1
        print(val)

    def find(self,value):
        node=self.head
        index=0
        while node!=None:
            index+=1
            if node.value==value:
                print("The value",value,"is present at index",index)
            node=node.next
        return None

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.value,"->",end=" ")
            temp=temp.next
        print("END")


if __name__ == "__main__":
    ob=LL()
    