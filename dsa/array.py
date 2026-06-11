my_array = [7, 12, 9, 4, 11]
min_val = my_array[0]

for x in my_array:
    if x < min_val:
        min_val = x
print("Min value is:", min_val)
print(my_array)