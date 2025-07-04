import numpy as np

# Create a 2D NumPy array (matrix)
array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# Display the original array
print("Original Array:")
print(array)

# Accessing specific elements
print("\nAccessing Specific Elements:")
print("Element at (1, 2):", array[1, 2])  # Output: 7

# Accessing specific rows and columns
print("\nAccessing Specific Rows and Columns:")
print("Row 1:", array[1])  # Output: [5, 6, 7, 8]
print("Column 2:", array[:, 2])  # Output: [3, 7, 11]

# Slicing operations
print("\nSlicing Operations:")
print("First two rows and columns (2x2 subarray):")
print(array[:2, :2])  # Output: [[1, 2], [5, 6]]
print("All rows and last two columns:")
print(array[:, -2:])  # Output: [[ 3, 4], [ 7, 8], [11, 12]]

# Boolean indexing
print("\nBoolean Indexing:")
mask = array > 5
print("Array with elements greater than 5:")
print(array[mask])  # Output: [ 6, 7, 8, 9, 10, 11, 12]

# Fancy indexing
print("\nFancy Indexing:")
rows = [0, 2]
cols = [1, 3]
print("Elements from specified rows and columns:")
print(array[rows, cols])  # Output: [ 2, 12]
