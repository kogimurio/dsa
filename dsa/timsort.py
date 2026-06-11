def insertionsort(arr, left, right):
    # Sort small runs using Insertion sort
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        
        while j >= left and arr[j] > key:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = key
def merge(arr, left, mid, right):
    # Create left and right sub-array
    leftPart = arr[left:mid + 1]
    rightPart = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    # Merge the two sorted parts
    while i < len(leftPart) and j < len(rightPart):
        if leftPart[i] <= rightPart[j]:
            arr[k] = leftPart[i]
            i+=1
        else:
            arr[k] = rightPart[j]
            j+=1
        k+=1
    # Add remaining elements
    while i < len(leftPart):
        arr[k] = leftPart[i]
        i+=1
        k+=1
    while j < len(rightPart):
        arr[k] = rightPart[j]
        j+=1
        k+=1

def timSort(arr):
    n = len(arr)
    
    # Size of small runs
    RUN = 4
    
    # STEP 1: Sort small runs using Insertion sort
    for start in range(0, n, RUN):
        end = min(start + RUN - 1, n - 1)
        
        insertionsort(arr, start, end)
    # STEP 2: Merge sorted runs
    size = RUN
    
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            
            # Merge only if there are two parts
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2
    return arr
unsortedArr = [5, 2, 8, 1, 9, 3, 7, 6]
sortedArr = timSort(unsortedArr)
print("Sorted Arry:", sortedArr)
            