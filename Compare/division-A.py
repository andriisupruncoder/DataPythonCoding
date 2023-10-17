def is_divisible(x, y):
  return x % y == 0


def generate_perfect_array(n):
  """
  Generates a perfect array of length n.

  Args:
    n: The length of the array.

  Returns:
    A perfect array of length n.
  """

  array = []
  for i in range(1, n + 1):
    # Find the smallest number in the range [1, 1000] that is divisible by i.
    x = 1
    while not is_divisible(x, i):
      x += 1
    array.append(x)
  return array


def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    array = generate_perfect_array(n)
    print(*array)


if __name__ == "__main__":
  main()