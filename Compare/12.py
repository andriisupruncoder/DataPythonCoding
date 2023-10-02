def bubble_sort(array):
  n = len(array)
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
  return array

# Example usage
array = [5, 2, 4, 6, 1]
print(bubble_sort(array))