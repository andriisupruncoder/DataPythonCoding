import random

def generate_random_matrix(rows, columns):
  """Generates a random matrix with the specified number of rows and columns.

  Args:
    rows: The number of rows in the matrix.
    columns: The number of columns in the matrix.

  Returns:
    A random matrix with the specified number of rows and columns.
  """

  matrix = []
  for i in range(rows):
    row = []
    for j in range(columns):
      row.append(random.randint(0, 100))
    matrix.append(row)
  return matrix


def add_matrices(matrix1, matrix2):
  """Adds two matrices together.

  Args:
    matrix1: The first matrix.
    matrix2: The second matrix.

  Returns:
    The sum of the two matrices.
  """

  if matrix1.shape != matrix2.shape:
    raise ValueError("Matrices must be the same shape.")

  result_matrix = [[0 for i in range(len(matrix1[0]))] for j in range(len(matrix1))]

  for row in range(len(matrix1)):
    for column in range(len(matrix1[0])):
      result_matrix[row][column] = matrix1[row][column] + matrix2[row][column]

  return result_matrix


def print_matrix(matrix):
  """Prints a matrix to the console.

  Args:
    matrix: The matrix to print.
  """

  for row in matrix:
    print(row)


# Generate two random matrices.

matrix1 = generate_random_matrix(100, 100)
matrix2 = generate_random_matrix(100, 100)

# Add the two matrices together.

sum_matrix = add_matrices(matrix1, matrix2)

# Print the sum matrix to the console.

print("Sum matrix:")
print_matrix(sum_matrix)