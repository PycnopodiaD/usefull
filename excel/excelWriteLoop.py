import openpyxl
wb = openpyxl.load_workbook('.xlsx')
sheet = wb['Sheet1']
ws=wb.active
names=ws['C']
for x in names:
    if x.value is None:
        break
    print(x.value)
