def check_if_in(list_of_strings, other_string):
  return any(string in other_string for string in list_of_strings)

list_of_strings = ["hello", "world"]
other_string = "hello world"

print(check_if_in(list_of_strings, other_string))