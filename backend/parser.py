import csv

list = []
with open("backend/parsed_all_data_cleaned.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    list.append(row)

