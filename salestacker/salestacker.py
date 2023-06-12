import csv
import random

customers = []
sales_records = []
header = ["salesid", "customerid", "Name", "Product", "Price", "Date", "Address", "Payment Method", "Shipping Status", "Stock Status"]

def generate_salesid():
    return str(random.randint(100000, 999999))

def generate_customerid():
    return str(random.randint(100000, 999999))

def load_customers():
    with open("sales.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            customer = {
                "ID": row[0],
                "Name": row[1]
            }
            customers.append(customer)

def add_sale():
    if not customers:
        print("No customers found. Please add customers first.")
        return

    print("Add Sale")
    print("Customers:")
    for i, customer in enumerate(customers, start=1):
        print(f"{i}. {customer['ID']} - {customer['Name']}")

    customer_id = generate_customerid()
    customer = next((c for c in customers if c["ID"] == customer_id), None)

    if not customer:
        print("Invalid customer ID.")
        return

    sales_id = generate_salesid()

    sale = {
        "salesid": sales_id,
        "customerid": customer_id,
        "Name": customer["Name"],
        "Product": input("Enter the product name: "),
        "Price": input("Enter the product price: "),
        "Date": input("Enter the date: "),
        "Address": input("Enter the address: "),
        "Payment Method": input("Enter the payment method: "),
        "Shipping Status": input("Enter the shipping status: "),
        "Stock Status": input("Enter the stock status: ")
    }

    sales_records.append(sale)
    print("Sale added successfully.")

def edit_sale():
    if not sales_records:
        print("No sales records found for editing.")
        return

    sales_id = input("Enter the sales ID to edit: ")
    sale = next((s for s in sales_records if s["salesid"] == sales_id), None)

    if not sale:
        print("Invalid sales ID.")
        return

    print("Current values for editing:")
    for key, value in sale.items():
        print(f"{key}: {value}")

    field = input("Select the field to edit: ")
    if field not in sale:
        print("Invalid field.")
        return

    new_value = input("Enter the new value: ")
    sale[field] = new_value

    print("Sale record edited successfully.")

def delete_sale():
    if not sales_records:
        print("No sales records found for deletion.")
        return

    sales_id = input("Enter the sales ID to delete: ")
    sale = next((s for s in sales_records if s["salesid"] == sales_id), None)

    if not sale:
        print("Invalid sales ID.")
        return

    sales_records.remove(sale)
    print("Sale record deleted successfully.")

def export_csv():
    if not sales_records:
        print("No sales records found to export.")
        return

    filename = input("Enter the filename to save the CSV (e.g., sales.csv): ")

    try:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(sales_records)

        print(f"{filename} saved successfully as a CSV file.")
    except IOError:
        print("An error occurred while writing to the file.")

def main():
    load_customers()

    while True:
        print("\nSales Tracking Application")
        print("1. Add Sale")
        print("2. Edit Sale Record")
        print("3. Delete Sale Record")
        print("4. View Sales Records")
        print("5. Export to CSV")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_sale()
        elif choice == "2":
            edit_sale()
        elif choice == "3":
            delete_sale()
        elif choice == "4":
            for sale in sales_records:
                print("--------")
                for key, value in sale.items():
                    print(f"{key}: {value}")
            print("--------")
        elif choice == "5":
            export_csv()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
