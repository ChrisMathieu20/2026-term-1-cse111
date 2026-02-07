import csv
from datetime import datetime

current_date_time = datetime.now()

def read_dictionary(filename,key_column_index):
    dictionary = {}
    with open(filename,"rt") as csv_file:
        reader = csv.reader(csv_file,delimiter=",")
        next(reader)
        for row in reader:
            key_value = row[key_column_index]
            dictionary[key_value] = row
    return dictionary

def main():
    try:
        PRODUCT_NUMBER_INDEX = 0
        PRODUCT_NAME_INDEX = 1
        RETAIL_PRICE_INDEX = 2
        STORE_NAME = "Timothy's Store"
        products_dict = read_dictionary("products.csv",PRODUCT_NUMBER_INDEX)
        print(STORE_NAME)
        with open("request.csv","rt") as requests_file:
            reader = csv.reader(requests_file,delimiter=",")
            next(reader)
            items = 0
            subtotal = 0
            for row in reader:
                key = row[0]
                product = products_dict[key]
                name = product[PRODUCT_NAME_INDEX]
                price = float(product[RETAIL_PRICE_INDEX])
                quantity = int(row[1])
                print(f"{name}: {quantity} @ {price}")
                items += quantity
                amount = quantity * price
                subtotal += amount
        print(f"Number of Items: {items}")
        print(f"Subtotal: {subtotal:.2f}")
        tax = subtotal * 6 / 100
        print(f"Sales Tax: {tax:.2f}")
        total = subtotal + tax
        print(f"Total: {total:.2f}")
        print(f"Thank you for shopping at the {STORE_NAME}")
        print(f"{current_date_time:%a %b %w %I:%M:%S %Y}")
    except FileNotFoundError as not_found_err:
        print(not_found_err)
    except PermissionError as permission_err:
        print(permission_err)
    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file\n{key_err}")

if __name__ == "__main__":
    main()