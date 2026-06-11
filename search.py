# Linear Search 
def searchLinear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
myArray = [1, 5, 7, 3, 8, 2, 9]
x = 9
results = searchLinear(myArray, x)
if results != -1:
    print("Found at index:", results)
else:
    print("Not found")

# Binary Search
def binarySearch(arr, target):
    left = 0
    right = len(arr) -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 11]
x = 11

results = binarySearch(mylist, x)
if results != -1:
    print("Found at index:", results)
else:
    print("Not found")
