import numpy as np

# Step 1: Create a NumPy array
array = np.arange(12)  # Creates a 1D array with values from 0 to 11
print("Original Array:")
print(array)

# Step 2: Reshape the array into different dimensions
reshaped_array_2x6 = array.reshape(2, 6)  # Reshape into a 2x6 array
print("\nReshaped Array (2x6):")
print(reshaped_array_2x6)

reshaped_array_3x4 = array.reshape(3, 4)  # Reshape into a 3x4 array
print("\nReshaped Array (3x4):")
print(reshaped_array_3x4)

# Step 3: Transpose of the reshaped array
transposed_array_2x6 = reshaped_array_2x6.T
print("\nTranspose of 2x6 Array:")
print(transposed_array_2x6)

transposed_array_3x4 = reshaped_array_3x4.T
print("\nTranspose of 3x4 Array:")
print(transposed_array_3x4)

# Step 4: Demonstrate swapping axes
swapped_axes_array = reshaped_array_3x4.swapaxes(0, 1)  # Swap axes of the 3x4 array
print("\nArray with Swapped Axes (3x4 to 4x3):")
print(swapped_axes_array)
