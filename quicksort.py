def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high],  array[i+1]
    return i+1
def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1) 
        quicksort(array, pivot_index+1, high)
        
mylist = [64, 87, 1, 3, 50, 1000, 34, 55, 23, 11, 0]
quicksort(mylist)
print(mylist)
        
