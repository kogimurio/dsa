def tri_recursion(k):
    if(k>0):
        results = k+tri_recursion(k-1)
        print(results)
    else:
        results = 0
    return results
print("\n\nRecursion Example Results")
tri_recursion(6)