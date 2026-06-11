# # Implement AVL Tree
# class TreeNode:
#   def __init__(self, data):
#     self.data = data
#     self.left = None
#     self.right = None
#     self.height = 1
# def getHeight(node):
#   if not node:
#     return 0
#   return node.height
# def getBalance(node):
#   if not node:
#     return 0
#   return getHeight(node.right) - getHeight(node.left)
# def rightRotate(y):
#   print("Rotate right on node", y.data)
#   x = y.left
#   T2 = x.right
#   x.right = y
#   y.left = T2
#   y.height = 1 + max(getHeight(y.left), getHeight(y.right))
#   x.height = 1 + max(getHeight(x.left), getHeight(x.right))
#   return x
# def leftRotate(x):
#   print("Rotate right on node", x.data)
#   y = x.right
#   T2 = y.left
#   y.left = x
#   x.right = T2
#   y.height = 1 + max(getHeight(y.left), getHeight(y.right))
#   x.height = 1 + max(getHeight(x.left), getHeight(x.right))
#   return y
# def insert(node, data):
#   if not node:
#     return TreeNode(data)
#   if data < node.data:
#     node.left = insert(node.left, data)
#   elif data > node.data:
#     node.right = insert(node.right, data)
#   # Update the balance factor and balance the tree
#   node.height = 1 + max(getHeight(node.left), getHeight(node.right))
#   balance = getBalance(node)
#   # Balance the tree
#   # Left Left
#   if balance < -1 and getBalance(node.left) <= 0:
#     return rightRotate(node)
#   # Left Right
#   if balance < -1 and getBalance(node.left) > 0:
#    node.left = leftRotate(node.left)
#    return rightRotate(node) 
#   # Right Right
#   if balance > 1 and getBalance(node.right) >= 0:
#     return leftRotate(node)
#   # Right Left
#   if balance > 1 and getBalance(node.right) < 0:
#     node.right = rightRotate(node.right)
#     return leftRotate(node)
#   return node
# def inOrderTraverse(node):
#   if node is None:
#     return
#   inOrderTraverse(node.left)
#   print(node.data, end=" - > ")
#   inOrderTraverse(node.right)
# def minValuNode(node):
#   current = node
#   while current.left is not None:
#     current = current.left
#   return current
# def delete(node, data):
#   if not node:
#     return node
#   if data < node.data:
#     node.left = delete(node.left, data)
#   elif data > node.data:
#     node.right = delete(node.right, data)
#   else:
#     if node.left is None:
#       temp = node.right
#       node = None
#       return temp
#     elif node.right is None:
#       temp = node.left
#       node = None
#       return temp
    
#     temp = minValuNode(node.right)
#     node.data = temp.data
#     node.right = delete(node.right, temp.data)
#   if node is None:
#     return node
#   # Update the balance factor and balance the tree
#   node.height = 1 + max(getHeight(node.left), getHeight(node.right))
#   balance = getBalance(node)
#   # Balance the tree
#   # Left Left
#   if balance < -1 and getBalance(node.left) <= 0:
#     return rightRotate(node)
#   # Left Right
#   if balance < -1 and getBalance(node.left) > 0:
#    node.left = leftRotate(node.left)
#    return rightRotate(node) 
#   # Right Right
#   if balance > 1 and getBalance(node.right) >= 0:
#     return leftRotate(node)
#   # Right Left
#   if balance > 1 and getBalance(node.right) < 0:
#     node.right = rightRotate(node.right)
#     return leftRotate(node)
#   return node
# # Insert Nodes
# root = None
# letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
# for letter in letters:
#   root = insert(root, letter)
# inOrderTraverse(root)
# print("\nDeleting A")
# root = delete(root, 'A')
# inOrderTraverse(root)

# import matplotlib.pyplot as plt
# import seaborn as sns
# from numpy import random

# # data = {
# #   "normal": random.normal(loc=50, scale=5, size=1000),
# #   "binormial": random.binomial(n=100, p=0.5, size=1000)
# # }
# # sns.displot(data, kind="kde")
# # plt.show()
# # data = {
# #   # "normal": random.normal(loc=50, scale=7, size=1000),
# #   "binomial": random.binomial(n=1000, p=0.01, size=1000),
# #   "poisson": random.poisson(lam=10, size=1000)
# # }
# # sns.displot(data, kind='kde')
# # plt.show()
# print()
# # sns.displot(random.uniform(size=1000), kind='kde')
# # plt.show()
# # data = {
# #   "normal": random.normal(scale=2, size=1000),
# #   "logistic": random.logistic(size=1000)
# # }
# # sns.displot(data, kind='kde')
# # plt.show()
# # sns.displot(random.exponential(size=1000), kind='kde')
# # plt.show()
# # sns.displot(random.chisquare(df=1, size=1000), kind='kde')
# # plt.show
# # 
# # sns.displot(random.pareto(a=4, size=1000))
# # plt.show()
# # x = random.zipf(a=2, size=1000)
# # sns.displot(x[x<10])
# # plt.show()

# import numpy as np
# def myadd(x, y):
#   return x**y
# myadd = np.frompyfunc(myadd, 2, 1)

# print(type(myadd))
# print(myadd([2, 3], [3, 2]))

# x = np.array([[2, 3]])
# y = np.around([-3.1666, 3.6667])
# newarray = np.absolute(y)
# print(y)

# arr = np.arange(1, 10)
# print(np.log2(arr))
# print(np.log10(arr))
# print(np.log(arr))

# from math import log

# nplog = np.frompyfunc(log, 2, 1)
# print(nplog(100, 15))

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 6, 8])

# newArr = np.diff(arr2, n=2)
# print(newArr)

# arr = np.arange(1, 11)
# x = np.lcm.reduce(arr)
# print(x)

# num1 = 6
# num2 = 9

# x = np.gcd.reduce(arr2)
# print(x)

# arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5, np.pi/6,])
# x = np.sin(arr)
# print(x)

# arr = np.array([90, 180, 270, 360])
# x = np.deg2rad(arr)
# print(x)

# arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
# x = np.rad2deg(arr)
# print(x)

# arr = np.array([1, -1, 0.1])
# x = np.arcsin(arr)
# print(x)

# base = 3
# perp = 4

# x = np.hypot(base, perp)
# print(x)

# x = np.sinh(np.pi/2)
# print(x)

# arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5, np.pi/6,])
# x = np.cosh(arr)
# print(x)

# x = np.arcsin(1.0)
# print(x)
# y = np.rad2deg(x)
# print(y)

# arr = np.array([0.1, 0.2, 0.5])
# x = np.arctanh(arr)
# print(x)

# arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

# x = np.unique(arr)
# print(x)

# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([3, 4, 5, 6, 7, 8])
# x = np.union1d(arr1, arr2)
# print(x)
# y = np.intersect1d(arr1, arr2, assume_unique=True)
# print(y)
# z = np.setdiff1d(arr1, arr2)
# print(z)
# d = np.setxor1d(arr1, arr2)
# print(d)
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 999

a = [1, 7, 9, 4]
myval = pd.Series(a, index = [5, 7, 2, 9])
print(myval[9])

calories = {"day1": 420, "day2": 380, "day3": 390}
myval = pd.Series(calories, index = ['day2', 'day3'])
print(myval)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myval = pd.DataFrame(data, index=['day4', 'day5', 'day6'])
try:
 print(myval.loc[['day1', 'day3']])
except:
  print(myval.loc['day4'])

df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset=['Date'], inplace= True)
x = df['Calories'].mean()
df.fillna({'Calories': x}, inplace=True)
for x in df.index:
  if df.loc[x, 'Duration'] > 50:
    df.drop(x, inplace=True)
print(df.drop_duplicates(inplace=True))
print(df.to_string())
df['Duration'].plot(kind='hist')
plt.show()



# df = pd.read_json('data.json')
# x = df["Calories"].mode()[0]
# df.fillna({"Calories": x}, inplace= True)
# print(df)

# 4 nodes: A, B, C, D
matrix = [
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 1],  # C
    [0, 1, 1, 0]   # D
]

# Check if A is connected to C
print(matrix[0][2])  # 1 → yes