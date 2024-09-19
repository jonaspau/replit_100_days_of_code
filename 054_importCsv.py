import csv  # Imports the csv library

with open("Day54Totals.csv") as file:
    reader = csv.DictReader(file)
    total = 0

    for row in reader:
        total += float(row["Cost"]) * int(row["Quantity"])

print(f"Total sales: {round(total, 2)}")
