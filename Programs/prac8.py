# Import the NumPy library
import numpy as np

# Create a NumPy array from a Python list
python_list = [1, 2, 3, 4, 5]
numpy_array_from_list = np.array(python_list)

# Create a NumPy array using built-in functions (e.g., zeros, ones)
numpy_array_zeros = np.zeros((2, 3))  # 2x3 array of zeros
numpy_array_ones = np.ones((3, 2))    # 3x2 array of ones

# Display the created arrays
print("Array created from a Python list:")
print(numpy_array_from_list)
print("Shape:", numpy_array_from_list.shape)
print("Data type:", numpy_array_from_list.dtype)
print("Size:", numpy_array_from_list.size)
print("Number of dimensions:", numpy_array_from_list.ndim)
print()

print("Array of zeros:")
print(numpy_array_zeros)
print("Shape:", numpy_array_zeros.shape)
print("Data type:", numpy_array_zeros.dtype)
print("Size:", numpy_array_zeros.size)
print("Number of dimensions:", numpy_array_zeros.ndim)
print()

print("Array of ones:")
print(numpy_array_ones)
print("Shape:", numpy_array_ones.shape)
print("Data type:", numpy_array_ones.dtype)
print("Size:", numpy_array_ones.size)
print("Number of dimensions:", numpy_array_ones.ndim)
