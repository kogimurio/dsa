# Single linked
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# currentNode = node1

# while currentNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
# print("null")


# Doubly Linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)

# node1.next = node2

# node2.prev = node1
# node2.next = node3

# node3.prev = node2
# node3.next = node4

# node4.prev = node3

# print("\nTraversing forward")
# currentNode = node1
# while currentNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
# print("null")

# print("\nTraversing backword")
# currentNode = node4
# while currentNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.prev
# print("null")
    
# Circular Linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node1

# currentNode = node1
# startNode = node1
# print(currentNode.data, end=" -> ")
# currentNode = currentNode.next

# while currentNode != startNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
# print("...")

# Circular Doubly Linked List
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
        
# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)

# node1.next = node2
# node1.prev = node4

# node2.prev = node1
# node2.next = node3

# node3.prev = node2
# node3.next = node4

# node4.prev = node3
# node4.next = node1

# print("\nTraversing forword")
# currentNode = node1
# startNode = node1
# print(currentNode.data, end=" -> ")
# currentNode = currentNode.next

# while currentNode != startNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
# print("...")


# print("\nTraversing backward")
# currentNode = node4
# startNode = node4
# print(currentNode.data, end=" -> ")
# currentNode = currentNode.prev

# while currentNode != startNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.prev
# print("...")

# Traversal of a singly linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# def traverseAndPrint(head):
#     currentNode = head
#     while currentNode:
#         print(currentNode.data, end=" -> ")
#         currentNode = currentNode.next
#     print("null")
    
# traverseAndPrint(node1)

# # Finding the lowest value in a singly linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def findTheLowestValue(head):
#     minValue = head.data
#     currentNode = head.next
#     while currentNode:
#         if currentNode.data < minValue:
#             minValue = currentNode.data
#         currentNode = currentNode.next
#     return minValue

# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# print("The lowset value in the linked list:", findTheLowestValue(node1))

# Delete a Node in a Linked List
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# def transeAndPrint(head):
#     currentNode = head
#     while currentNode:
#         print(currentNode.data, end=" -> ")
#         currentNode = currentNode.next
#     print("null")

# def deleteSpecficNode(head, nodeToDelete):
    
#     if head == nodeToDelete:
#         return head.next

#     currentNode = head
#     while currentNode and currentNode.next and currentNode.next != nodeToDelete:
#         currentNode = currentNode.next
    
#     if currentNode.next is None:
#         return head
    
#     currentNode.next = currentNode.next.next
    
#     return head

# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# print("Before deletion")
# transeAndPrint(node1)

# # Delete node4

# node1 = deleteSpecficNode(node1, node4)

# print("\nAfter deletion")
# transeAndPrint(node1)


# Inserting a node in a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def selectionSortLinkedList(head):
    currentNode = head
    
    while currentNode:
        minNode = currentNode
        nextNode = currentNode.next
    
        # Find smallest node
        while nextNode:
            if nextNode.data < minNode.data:
                minNode = nextNode
            nextNode = nextNode.next
        
        # Swap value
        currentNode.data, minNode.data = minNode.data, currentNode.data
        
        currentNode = currentNode.next
    return head

def linearSearchLinkedList(head, targetValue):
    currentnode = head
    while currentnode:
        if currentnode.data == targetValue:
            return True
        currentnode = currentnode.next
    return False
            
def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode
    
    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next
        
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

def deleteSpecficNode(head, nodeToDelete):
    
    if head == nodeToDelete:
        return head.next

    currentNode = head
    while currentNode and currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next
    
    if currentNode.next is None:
        return head
    
    currentNode.next = currentNode.next.next
    
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original List")
traverseAndPrint(node1)

# Delete Node
deleteSpecficNode(node1, node4)

# Insert node with value 97 at position 2
newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print("\nAfter insertion")
traverseAndPrint(node1)

# Sort Linked List
selectionSortLinkedList(node1)

print("\nAfter sorting:")
traverseAndPrint(node1)

# Search Linked List
searched_value = linearSearchLinkedList(node1, 1)

if searched_value:
    print("found!")
else:
    print("not found")

# Sorting Algorithm for Linked list
# Linear search Algorithm for Linked list 