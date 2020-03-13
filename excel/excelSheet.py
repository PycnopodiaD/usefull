import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
sheet.title = 'something'
sheet['A1'] = 'Hello world'
wb.create_sheet(index=2, title='thisone')
wb.remove(wb['thisone'])
