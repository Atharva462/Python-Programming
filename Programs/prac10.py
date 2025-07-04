import numpy as np

# Create two NumPy arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([1, 2, 3, 4, 5])

# Perform element-wise operations
addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

# Use universal functions
sqrt_array1 = np.sqrt(array1)
log_array1 = np.log(array1)
exp_array1 = np.exp(array1)

# Print results
print("Array 1:", array1)
print("Array 2:", array2)
print("Element-wise Addition:", addition)
print("Element-wise Subtraction:", subtraction)
print("Element-wise Multiplication:", multiplication)
print("Element-wise Division:", division)
print("Square Root of Array 1:", sqrt_array1)
print("Logarithm of Array 1:", log_array1)
print("Exponential of Array 1:", exp_array1)
