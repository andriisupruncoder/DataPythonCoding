import PyPDF2
import xlsxwriter

def get_15_digit_numbers(pdf_file):
  """Returns a list of 15-digit numbers from the given PDF file."""

  pdf_reader = PyPDF2.PdfFileReader(pdf_file)
  numbers = []
  for page in pdf_reader.pages:
    for text in page.extractText().split():
      if len(text) == 15 and text[3] == " ":
        numbers.append(text)
  return numbers

def write_to_excel(numbers, excel_file):
  """Writes the given list of numbers to an Excel spreadsheet."""

  workbook = xlsxwriter.Workbook(excel_file)
  worksheet = workbook.add_worksheet()
  for number in numbers:
    worksheet.write_string(0, len(numbers), number)
  workbook.close()

def main():
  # Get the PDF file name from the user.
  pdf_file_name = input("Enter the name of the PDF file: ")

  # Get the Excel file name from the user.
  excel_file_name = input("Enter the name of the Excel file: ")

  # Get the 15-digit numbers from the PDF file.
  numbers = get_15_digit_numbers(pdf_file_name)

  # Write the numbers to the Excel file.
  write_to_excel(numbers, excel_file_name)

if __name__ == "__main__":
  main()