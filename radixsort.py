mylist = [170,45,75,90,802,24,2,66]

# print("Original array", mylist)
# radixArray = [[], [], [], [], [], [], [], [], [], [], ]
# maxVal = max(mylist)
# exp = 1

# while maxVal // exp > 0:
#     while len(mylist) > 0:
#         val = mylist.pop()
#         radixIndex = (val // exp) % 10
#         radixArray[radixIndex].append(val)
#     for bucket in radixArray:
#         while len(bucket) > 0:
#             val = bucket.pop()
#             mylist.append(val)
#     exp *= 10
# print(mylist)




# def radix_sort(arr):
#     # Find the biggest number
#     max_val = max(arr) 
#     # Start with ones plce
#     exp = 1 
#     # Continue while digit place
#     while max_val // exp > 0:
#         # Create 10 empty buckets (0 to 9)
#         buckets = [[] for _ in range(10)]
#         # Put each number in correct bucket
#         for num in arr:
#             digit = (num // exp) % 10
#             buckets[digit].append(num)
#         # Collect numbers back in order
#         arr = []
#         for bucket in buckets:
#             for num in bucket:
#                 arr.append(num)
#         # move to next digit place
#         exp *= 10
#     return arr
# mylist = [170,45,75,90,802,24,2,66]
# sorted_list = radix_sort(mylist)
# print(sorted_list)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def radixSortWithBubbleSort(arr):
    max_val = max(arr)
    exp=1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        for bucket in buckets:
            sorted(bucket)
        i = 0
        for bucket in buckets:
            for num in bucket:
                arr[i] = num
                i+=1
        exp *= 10
mylist = [170,45,75,90,802,24,2,66]
radixSortWithBubbleSort(mylist)
print(mylist)     
        
# Insertion Sort
# Python built-in sort()
# Counting Sort
# Timsort
# Quick Sort
# Merge Sort

