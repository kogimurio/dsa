mylist = [64, 87, 1, 3, 50, 1000, 34, 55, 23, 11, 0]

n = len(mylist)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if mylist[j] > mylist[j + 1]:
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
            swapped = True
    if not swapped:
        break
print(mylist)