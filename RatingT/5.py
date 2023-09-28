def round_float(number, precision=2):
  """Rounds a float to the specified precision.

  Args:
    number: The float to be rounded.
    precision: The number of decimal places to round to.

  Returns:
    The rounded float.
  """

  if precision < 0:
    raise ValueError("Precision must be non-negative.")

  multiplier = 10 ** precision
  rounded_number = round(number * multiplier)
  return rounded_number / multiplier
#example 
number = 3.14159
ndigits = 3
print(round_float(number, ndigits))