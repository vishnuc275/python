import csv
with open('cars.csv', 'r',) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)