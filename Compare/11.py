def bubble_sort(list_to_sort):
  n = len(list_to_sort)

  for i in range(n):
    for j in range(0, n - i - 1):
      if list_to_sort[j] > list_to_sort[j + 1]:
        list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]

  return list_to_sort

unsorted_list = [5, 2, 4, 6, 1, 3]

sorted_list = bubble_sort(unsorted_list)

print(sorted_list)