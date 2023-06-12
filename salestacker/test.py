import csv
import random

header = ["salesid","Name", "Product", "Price", "Date", "Address", "Payment Method", "Shipping Status", "Stock Status"]

def generate_salesid():
    return str(random.randint(100000, 999999))

def add_header(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for line in lines:
            file.write(line)

def add_salesid(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["customerid"] + header)
        writer.writeheader()

        for i, row in enumerate(rows, start=1):
            row["customerid"] = generate_salesid()
            writer.writerow(row)

filename = "customers.csv"

add_header(filename)


add_salesid(filename)

print(f"{filename} done")
