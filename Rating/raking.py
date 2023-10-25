import pandas as pd

def replace_values(df, columns, exclude_columns):
  """Replaces all the column values from 0 to False and 1 to True, excluding the specified columns.

  Args:
    df: The Pandas DataFrame.
    columns: The list of columns to replace values.
    exclude_columns: The list of columns to exclude.

  Returns:
    The Pandas DataFrame with the replaced values.
  """

  for column in columns:
    if column not in exclude_columns:
      df[column] = df[column].replace_values({0: False, 1: True})

  return df

# Example usage
df = pd.DataFrame({
  "column_1": [0, 1, 0],
  "column_2": [1, 0, 1],
  "column_3": [0, 1, 0],
})

# Replace values in all columns except "column_3"
df = replace_values(df, columns=["column_1", "column_2"], exclude_columns=["column_3"])

print(df)