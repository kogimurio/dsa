mylist = [64, 87, 1, 3, 50, 1000, 34, 55, 23, 11, 0]


n = len(mylist)
for i in range(1, n):
    insert_index = i
    current_value = mylist.pop(i)
    for j in range(i-1):
        if mylist[j] > current_value:
            insert_index = j
    mylist.insert(insert_index, current_value)
print(mylist)

n = len(mylist)
for i in range(1, n):
    insert_index = i
    current_value = mylist[i]
    for j in range(i-1):
        if mylist[j] > current_value:
            mylist[j+1] = mylist[j]
            insert_index = j
        else:
            break
    mylist[insert_index] = current_value
print(mylist)