import array

import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Insertion
arr.insert(2, 10)  # Insert 10 at index 2

# Deletion
arr.remove(4)  # Remove the first occurrence of 4

# Searching
def search_array(arr, value):
    for index, element in enumerate(arr):
        if element == value:
            return index
    return -1

index = search_array(arr, 10)  # Find the index of 10

# Iteration
for element in arr:
    print(element)