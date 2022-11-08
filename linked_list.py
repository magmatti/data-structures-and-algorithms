class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class SLinkedList:
   def __init__(self):
      self.head = None

   def listprint(self):
      printval = self.head
      while printval is not None:
         print (printval.data)
         printval = printval.next


names = SLinkedList()
names.head = Node("David")
e2 = Node("John")
e3 = Node("Matthew")
e4 = Node("Ann")
e5 = Node("Derek")

names.head.next = e2

e2.next = e3
e3.next = e4
e4.next = e5

names.listprint()