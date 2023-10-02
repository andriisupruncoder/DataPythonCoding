import numpy as np

def add_matrices_numpy(matrix1, matrix2):
  """Adds two matrices together using NumPy.

  Args:
    matrix1: The first matrix.
    matrix2: The second matrix.

  Returns:
    The sum of the two matrices.
  """

  return np.add(matrix1, matrix2)


# Example usage:

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

sum_matrix = add_matrices_numpy(matrix1, matrix2)

print(sum_matrix)