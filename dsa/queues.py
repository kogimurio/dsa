queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')

print(queue) 

# Dequeue
element = queue.pop(0)
print("Dequeue: ", element)

# Peek
frontElement = queue[0]

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("size: ", len(queue))

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, element):
        self.queue.append(element)
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    def isEmpty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
myQueue = Queue()

myQueue.enqueue("D")
myQueue.enqueue("E")
myQueue.enqueue("F")
print("Queue: ", myQueue.queue)

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())


# Implementing Queue using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    def enqueue(self, element):
        newNode = Node(element)
        if self.rear is None:
            self.front = self.rear = newNode
            self.length += 1
            return
        self.rear.next = newNode
        self.rear = newNode
        self.length += 1
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    def isEmpty(self):
        return self.length == 0
    def size(self):
        return self.length
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" - > ")
            temp = temp.next
        print("none")
# Create a queue
myQueue = Queue()

myQueue.enqueue("G")
myQueue.enqueue("H")
myQueue.enqueue("I")
print("Queue: ", end="")
myQueue.printQueue()

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("size: ", myQueue.size())





