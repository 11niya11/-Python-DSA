# arrays.py
# Basic array operations in Python

# 1. Create an array (list in Python)
arr = [10, 20, 30, 40, 50]
print("Initial array:", arr)

# 2. Access elements
print("First element:", arr[0])
print("Last element:", arr[-1])

# 3. Insert element
arr.append(60)
print("After append:", arr)

# 4. Update element
arr[2] = 35
print("After update:", arr)

# 5. Delete element
arr.remove(20)
print("After remove:", arr)

# 6. Traversal
print("Traversal:")
for i in arr:
    print(i, end=" ")

# 7. Search element
if 40 in arr:
    print("\n40 found in array")
else:
    print("\n40 not found")
