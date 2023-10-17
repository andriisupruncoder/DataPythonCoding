def find_perfect_array(n):
  """Finds a perfect array of length n.

  Args:
    n: The length of the array.

  Returns:
    A perfect array of length n.
  """

  # Initialize the array.
  array = []

  # Add elements to the array until it is perfect.
  while not is_perfect_array(array):
    array.append(1)

  return array

def is_perfect_array(array):
  """Checks if the given array is perfect.

  Args:
    array: The array to check.

  Returns:
    True if the array is perfect, False otherwise.
  """

  # Check if the array has the correct length.
  if len(array) != n:
    return False

  # Check if all elements in the array are divisible by their index.
  for i in range(len(array)):
    if array[i] % i != 0:
      return False

  # Check if the sum of the elements in the array is divisible by n.
  if sum(array) % n != 0:
    return False

  return True

# Get the number of test cases.
t = int(input())

# Solve each test case.
for i in range(t):
  # Get the length of the array.
  n = int(input())

  # Find a perfect array.
  array = find_perfect_array(n)

  # Print the array.
  print(" ".join(str(x) for x in array))