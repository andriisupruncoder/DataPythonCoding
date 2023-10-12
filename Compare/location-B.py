import os

def get_current_file_location():
  """Returns the current file location."""

  # Get the current working directory.
  current_working_directory = os.getcwd()

  # Get the filename of the current file.
  filename = os.path.basename(__file__)

  # Combine the current working directory and filename to get the current file location.
  current_file_location = os.path.join(current_working_directory, filename)

  # Return the current file location.
  return current_file_location

# Get the current file location.
current_file_location = get_current_file_location()

# Print the current file location.
print(current_file_location)