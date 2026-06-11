# myArray = [170, 45, 75, 90, 802, 24, 2, 66]

# print("Original array:", myArray)
# radixArray = [ [], [], [], [], [], [], [], [], [], []]
# max_val = max(myArray)
# exp = 1

# while max_val // exp > 0:
#     while len(myArray) > 0:
#         val = myArray.pop()
#         radixIndex = (val // exp) % 10
#         radixArray[radixIndex].append(val)
#     for bucket in radixArray:
#         while len(bucket) > 0:
#             val = bucket.pop()
#             myArray.append(val)
#     exp *= 10
# print("Sorted array:", myArray)

# Counting for radix
def countingsort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] +=1
        
    arr[:] = []
    
    for num, freq in enumerate(count):
        arr.extend([num] * freq)
    
    return arr

# Insertion sort for radix
def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        current_value = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value

# Merge sort for radix
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    
    return merge(sortedLeft, sortedRight)

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


# Bubble sort for radix
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def radixSortWithBubble(arr):
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        radixArray = [ [], [], [], [], [], [], [], [], [], []]
        # Put number into the buckets
        for num in arr:
            radixIndex = (num // exp) % 10
            radixArray[radixIndex].append(num)
        # Bubble sort each bucket
        for bucket in radixArray:
            mergeSort(bucket)
        # Put numbers back into array
        i = 0
        for bucket in radixArray:
            for num in bucket:
                arr[i] = num
                i+=1
        exp *= 10
myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixSortWithBubble(myArray)
print("Sorted array:", myArray)