import numpy as np

# Create two sample numpy arrays
array1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
array2 = np.array([2.1, 3.2, 4.3, 5.4, 6.5])

# Define the tolerance
tolerance = 1
def get_common_elements(array1, array2, tolerance):
# Create a boolean mask to check if elements of array1 are within tolerance of elements in array2
	within_tolerance_mask = np.abs(array1[:, np.newaxis] - array2) <= tolerance

# Check which elements of array1 are within tolerance of elements in array2
	existence_mask = np.any(within_tolerance_mask, axis=1)

# Get the elements of array1 that are within tolerance of elements in array2
	return  array1[existence_mask]

# Print the existing elements
