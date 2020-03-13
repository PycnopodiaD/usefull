import csv
exampleFile = open('.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData
