# -*- coding: utf-8 -*-
"""ML_HW_Extra_Q5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1orKdc8CQiNpdYTEGEpfmumM03-PmPjib
"""

import numpy as np

# Function to generate a random triangular matrix and check if it's non-singular
def is_triangular_matrix_non_singular(size, matrix_type):
    # Generate a random triangular matrix with non-zero diagonal elements
    if matrix_type == 'upper':
        A = np.triu(np.random.rand(size, size) + 1, 0)  # Shift by +1 to avoid zero diagonal entries
    elif matrix_type == 'lower':
        A = np.tril(np.random.rand(size, size) + 1, 0)  # Shift by +1 to avoid zero diagonal entries
    else:
        raise ValueError("matrix_type must be 'upper' or 'lower'")

    # Calculate determinant
    det = np.linalg.det(A)

    # Check if the determinant is non-zero
    is_non_singular = det != 0

    return is_non_singular, det, A

# Check for an upper triangular matrix
upper_non_singular, upper_det, upper_matrix = is_triangular_matrix_non_singular(5, 'upper')

# Check for a lower triangular matrix
lower_non_singular, lower_det, lower_matrix = is_triangular_matrix_non_singular(5, 'lower')

upper_non_singular, upper_det, upper_matrix, lower_non_singular, lower_det, lower_matrix