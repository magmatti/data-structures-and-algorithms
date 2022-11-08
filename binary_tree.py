class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def add(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.add(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.add(value)
        else:
            self.value = value

    def printBinaryTree(self):
        if self.left:
            self.left.printBinaryTree()
        print(self.value)

        if self.right:
            self.right.printBinaryTree()


root = Node(10)

root.add(9)
root.add(11)
root.add(1)
root.add(3)
root.add(5)
root.add(7)
root.add(8)

root.printBinaryTree()