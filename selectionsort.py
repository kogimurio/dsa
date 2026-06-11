mylist = [64, 87, 1, 3, 50, 1000, 34, 55, 23, 11, 0]

n = len(mylist)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if mylist[j] < mylist[min_index]:
            min_index = j
    min_value = mylist.pop(min_index)
    mylist.insert(i, min_value)
print(mylist)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if mylist[j] < mylist[min_index]:
            min_index = j
    mylist[i], mylist[min_index] = mylist[min_index], mylist[i]
print(mylist)