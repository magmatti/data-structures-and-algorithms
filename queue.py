class Queue:
    def __init__(self):
        self.queue = list()

    def addToQueue(self, value):
        if value not in self.queue:
            self.queue.insert(0, value)
            return True
        return False

    def size(self):
        return len(self.queue)


myQueue = Queue()

myQueue.addToQueue("value1")
myQueue.addToQueue("value2")
myQueue.addToQueue("value3")
myQueue.addToQueue("value4")
myQueue.addToQueue("value5")
myQueue.addToQueue("value6")
myQueue.addToQueue("value7")
myQueue.addToQueue("value8")

print(f"Number of elements in queue: {myQueue.size()}")