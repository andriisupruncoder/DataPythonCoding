def any_in_string(string, strings_list):
  for s in strings_list:
    if s in string:
      return True
  return False

strings_list = ["hello", "world"]
string = "hello world"

if any_in_string(string, strings_list):
  print("Found a match!")
else:
  print("No match found.")