import csv
outputFile = open('output.csv', 'w', newline='')
outputWriter.writerow(['Tofu', 'Tempha', 'Quorn', 'Beans'])
outputWriter = csv.writer(outputFile)
outputFile.close()
