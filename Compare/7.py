import numpy as np
import pandas as pd
import xlsxwriter

def matlab_to_excel(matlab_data, excel_file_path):
  # Convert MATLAB data to a NumPy array.
  numpy_data = np.array(matlab_data)

  # Create a Pandas DataFrame from the NumPy array.
  pandas_data = pd.DataFrame(numpy_data)

  # Write the Pandas DataFrame to an Excel file.
  with xlsxwriter.Workbook(excel_file_path) as workbook:
    worksheet = workbook.add_worksheet()
    worksheet.write_table(pandas_data)

# Example usage.
matlab_data = [[1, 2, 3], [4, 5, 6]]
excel_file_path = "matlab_data.xlsx"
matlab_to_excel(matlab_data, excel_file_path)