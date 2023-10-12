import math

def limit(f, x, a):
  """Calculates the limit of f(x) as x approaches a.

  Args:
    f: A function that takes a single argument.
    x: The value to approach.
    a: The limit value.

  Returns:
    The limit of f(x) as x approaches a.
  """

  if f(a) == 0:
    return 0

  h = 0.000001
  return (f(x + h) - f(x - h)) / (2 * h)

def derivative(f, x):
  """Calculates the derivative of f(x).

  Args:
    f: A function that takes a single argument.
    x: The value at which to calculate the derivative.

  Returns:
    The derivative of f(x).
  """

  return limit(lambda h: (f(x + h) - f(x)) / h, x, 0)

# Example usage
def f(x):
  return x**2

print(limit(f, 2, 4))
print(derivative(f, 2))