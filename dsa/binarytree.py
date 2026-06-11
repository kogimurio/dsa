class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def preOderTraversal(node):
    if node is None:
        return
    print(node.data, end=" -> ")
    preOderTraversal(node.left)
    preOderTraversal(node.right)
def inOderTraversal(node):
    if node is None:
        return
    inOderTraversal(node.left)
    print(node.data, end=" -> ")
    inOderTraversal(node.right)
def postOderTraversal(node):
    if node is None:
        return
    postOderTraversal(node.left)
    postOderTraversal(node.right)
    print(node.data, end=" -> ")
def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)
def insert(node, data):
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node
def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
def delete(node, data):
    if not node:
        return None
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # Node with only one child
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp
        # Node with two children, get the in-order succesor
        node.data = minValue(node.right).data
        node.right = delete(node.right, node.data)
    return node
root = TreeNode(13)
nodeA = TreeNode(7)
nodeB = TreeNode(15)
nodeC = TreeNode(3)
nodeD = TreeNode(8)
nodeE = TreeNode(14)
nodeF = TreeNode(19)
nodeG = TreeNode(18)

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Insert new value into BST
# insert(root, 51)
# print("root.right.left.data:", root.right.left.data)
# preOderTraversal(root)
# print()
# inOderTraversal(root)
# print()
# postOderTraversal(root)
# print()
# result = search(root, 51)
# if result:
#     print(f"Found the node with value: {result.data}")
# else:
#     print("Value not found in the BTS.")
# print()
# print("Min value:", minValue(root).data)


binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_index(index):
    return 2 * index + 1
def right_child_index(index):
    return 2 * index + 2
def get_data(index):
    if 0 <= index < len(binary_tree_array):
        return binary_tree_array[index]
    return None
right_child = right_child_index(0)
left_child_of_right_child = left_child_index(right_child)
data = get_data(left_child_of_right_child)

# print("root.right.left.data:", data)



binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_index(index):
    return 2 * index + 1
def right_child_index(index):
    return 2 * index + 2
def pre_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return [binary_tree_array[index]] + pre_order(left_child_index(index)) + pre_order(right_child_index(index))
def in_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return in_order(left_child_index(index)) + [binary_tree_array[index]] + in_order(right_child_index(index))
def post_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return post_order(left_child_index(index)) + post_order(right_child_index(index)) + [binary_tree_array[index]]


# print("Pre-order Traversal:", pre_order(0))
# print("In-order Traversal:", in_order(0))
# print("Post-order Traversal:", post_order(0))

# AVL Tree implementation
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
def getHeight(node):
    if not node:
        return 0
    return node.height
def getBalance(node):
    if not node:
        return 0
    return getHeight(node.right) - getHeight(node.left)
def rightRotate(y):
    print('Rotate right on node', y.data)
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x
def leftRotate(x):
    print('Rotate left on node', x.data)
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y

def insert(node, data):
    if not node:
        return TreeNode(data)
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    # Update the balance factor and balance the tree
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)
    
    # Balance the tree
    # left left
    if balance < -1 and getBalance(node.left) <= 0:
        return rightRotate(node)
    
    # left right
    if balance < -1 and getBalance(node.left) > 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    # right right
    if balance > 1 and getBalance(node.right) >= 0:
        return leftRotate(node)
    
    # right left
    if balance > 1 and getBalance(node.right) < 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    return node
def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, data):
    if not node:
        return node
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        temp = minValue(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)
    if node is None:
        return node
    # Update the balance factor and balance the tree
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)
    
    # Balance the tree
    # left left
    if balance < -1 and getBalance(node.left) <= 0:
        return rightRotate(node)
    
    # left right
    if balance < -1 and getBalance(node.left) > 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    # right right
    if balance > 1 and getBalance(node.right) >= 0:
        return leftRotate(node)
    
    # right left
    if balance > 1 and getBalance(node.right) < 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    return node
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=" - > ")
    inOrderTraversal(node.right)
# Insert nodes
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
    root = insert(root, letter)
    
inOrderTraversal(root)
    
delete(root, 'D')

inOrderTraversal(root)

