
def handle_file_exceptions(file_name):
  try:
    with io.open(file_name, "r") as f:
      # Do something with the file
      print("yes")
  except FileNotFoundError:
    print("File not found:", file_name)
  except IOError as e:
    print("I/O error:", e)

# Example usage
handle_file_exceptions("my_file.txt")