# prev1 = 0
# prev2 = 1


# print(prev1)
# print(prev2)
# For loop to generate fibonacci
# for fibo in range(18):
#     newFibo = prev2 + prev1
#     print(newFibo)
#     prev1 = prev2
#     prev2 = newFibo
    
# Recursion to generate fibonacci
# print(0)
# print(1)
# count = 2

# def fibonacci(prev1, prev2):
#     global count
#     if count <= 19:
#         newfabo = prev1 + prev2
#         print(newfabo)
#         prev2 = prev1
#         prev1 = newfabo
#         count += 1
#         fibonacci(prev1, prev2)
#     else:
#         return
# fibonacci(1, 0)



def F(n):
    if n <= 1:
        return n
    else:
        return F(n-1) + F(n-2)
print(F(5))




