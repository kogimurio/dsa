# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     leftHalf = arr[:mid]
#     rightHalf = arr[mid:]
    
#     sortedLeft = mergeSort(leftHalf)
#     sortedRight = mergeSort(rightHalf)
    
#     return merge(sortedLeft, sortedRight)
# def merge(left, right):
#     result = []
#     i = j = 0
    
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result
# mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
# mysortedList = mergeSort(mylist)
# print(mysortedList)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergeSort(arr):
    step = 1
    length = len(arr)
    
    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i+ step:i + 2 * step]
            
            merged = merge(left, right)
            
            for j, val in enumerate(merged):
                arr[i + j] = val
        step *= 2
    return arr

mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedList = mergeSort(mylist)
print(mysortedList)
