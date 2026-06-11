def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
  
    
    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1
    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1
    return arr
mylist = [64, 87, 1, 3, 50, 1000, 34, 55, 23, 11, 0]
mysortedlist = countingSort(mylist)
print(mysortedlist)
