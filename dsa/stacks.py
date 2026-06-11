# stack = []

# # Push
# stack.append("A")
# stack.append("B")
# stack.append("C")
# print("Stack:", stack)

# # Pop
# element = stack.pop()
# print("Pop:", element)

# # Peek
# topElement = stack[-1]
# print("Peek:", topElement)

# # isEmpty
# isEmpty = not bool(stack)
# print("isEmpty:", isEmpty)

# # Size
# print("Size: ", len(stack))

# # Stack using Array
# class Stack:
#     def __init__(self):
#         self.stack = []
    
#     def push(self, element):
#         self.stack.append(element)
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is Empty"
#         return self.stack.pop()
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is Empty"
#         return self.stack[-1]
#     def isEmpty(self):
#         return len(self.stack) == 0
#     def size(self):
#         return len(self.stack)
# mystack = Stack()
# mystack.push("D")
# mystack.push("E")
# mystack.push("F")
# print("Stack:", mystack.stack)

# print("Pop:", mystack.pop())
# print("Peek:", mystack.peek())
# print("isEmpty:", mystack.isEmpty())
# print("Size:", mystack.size())

# Stack with Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, value):
        newNode = Node(value)
        if self.head:
            newNode.next = self.head
        self.head = newNode
        self.size += 1
    def traverseStack(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" - > ")
            currentNode = currentNode.next
        print("none")
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        poopedNode = self.head
        self.head = self.head.next
        self.size -= 1
        return poopedNode.value
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    def isEmpty(self):
        return self.size == 0
    def stackSize(self):
        return self.size

mystack = Stack()
mystack.push("G")
mystack.push("H")
mystack.push("I")

print(mystack.traverseStack())
print("Pop:", mystack.pop())
print("Peek:", mystack.peek())
print("isEmpty:", mystack.isEmpty())
print("Size:", mystack.stackSize()) 
