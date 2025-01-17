import pandas as pd

# Specify the Excel file path
file_path = 'ML Lab - 1.xlsx'  # Replace with the path to your Excel file

# Read the entire sheet
data = pd.read_excel(file_path)

# Display all the values in the sheet
print(data)
