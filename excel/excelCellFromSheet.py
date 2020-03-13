import openpyxl
wb = openpyxl.load_workbook('.xlsx')
sheet = wb['Sheet1']
sheet['A1'].value
print(f'Row {str(c.row)}, Column {c.column} is {c.value}')
print(f'Cell {c.coordinate} is {c.value}')

for i in range(1, 8, 2):
    print(i, sheet.cell(row=i, column=2).value)
