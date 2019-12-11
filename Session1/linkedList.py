class Element:
    def __init__(self , name):
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None
        self.length = 0

    def addBegin(self , newElement):
        if self.root == None:
            self.root = newElement
        else:
            newElement.next = self.root
            self.root = newElement
        self.length += 1

    def addEnd(self , newElement):
        temp = self.root
        while(temp.next):
            temp = temp.next
        temp.next = newElement   
        self.length += 1 

    def addBet(self , oldElement , newElement):
        oldNextElement = oldElement.next #just define
        oldElement.next = newElement
        newElement.next = oldNextElement


    def remElement(self , element):
        if element == self.root:
            self.root.next = self.root
        else:    
            temp = self.root
            while(temp.next):
                if temp.next == element:
                    parent = temp
                    parent.next = element.next
                    self.length -= 1
                    break
                temp = temp.next


    def printLinkedList(self):
        if self.root == None:
            print("Empty")
        else:
            temp = self.root
            print(temp.name)
            while(temp.next):
                temp = temp.next
                print(temp.name) 

l = LinkedList()
elm1 = Element('Negar')
elm2 = Element('Nasim')
elm3 = Element('Narges')
elm4 = Element('Navid')  
elm5 = Element('Nima')  

l.addBegin(elm2)
l.addBegin(elm1)
l.addBet(elm1 , elm3)
l.addEnd(elm4)
l.addBet(elm3 , elm5)
l.printLinkedList()

print("**")

l.remElement(elm5)
l.printLinkedList()