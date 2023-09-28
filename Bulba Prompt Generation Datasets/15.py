import re

def is_valid(s):
  """Returns True if s meets all requirements for a Massachusetts vanity plate, False otherwise."""

  # Check that the plate starts with at least two letters.
  if not re.match("^[A-Z]{2,}", s):
    return False

  # Check that the plate has a maximum of 6 characters and a minimum of 2 characters.
  if len(s) > 6 or len(s) < 2:
    return False

  # Check that numbers are only used at the end of the plate.
  if re.match(".*[0-9].*[A-Z]", s):
    return False

  # Check that the first number used is not a '0'.
  if re.match(".*0.*", s):
    return False

  # Check that there are no periods, spaces, or punctuation marks.
  if re.match("[^A-Z0-9]", s):
    return False

  return True

def main():
  # Prompt the user for a vanity plate.
  plate = input("Enter a vanity plate: ")

  # Check if the plate is valid.
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")

if __name__ == "__main__":
  main()