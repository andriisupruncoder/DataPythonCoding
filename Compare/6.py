import openpyxl
import numpy as np

def matlab_to_excel(matlab_data, excel_file_path):
    """
    Translates MATLAB data to Excel.

    Args:
        matlab_data: The MATLAB data to be translated.
        excel_file_path: The path to the Excel file to be created.

    Returns:
        None.
    """

    # Check if the MATLAB data is a matrix.

    if not isinstance(matlab_data, np.ndarray):
        raise TypeError("The MATLAB data must be a matrix.")

    # Create a new Excel workbook and worksheet.

    wb = openpyxl.Workbook()
    ws = wb.active

    # Write the MATLAB data to the Excel worksheet.

    for i in range(matlab_data.shape[0]):
        for j in range(matlab_data.shape[1]):
            ws.cell(row=i + 1, column=j + 1).value = matlab_data[i, j]

    # Save the Excel workbook.

    wb.save(excel_file_path)


# Example usage.

matlab_data = np.array([[1, 2, 3], [4, 5, 6]])
excel_file_path = "matlab_data.xlsx"

matlab_to_excel(matlab_data, excel_file_path)