import csv
import datetime

current_date_and_time = datetime.datetime.now()
string = current_date_and_time.strftime('%a %b %d %I:%M:%S %Y')

PRODUCT_NUMBER_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

def read_products(filename):
    products = {}

    # open the products.csv file for reading and use a csv.reader to read each row
    with open(filename, 'rt') as products_file:
        reader = csv.reader(products_file)
        next(reader)

        # populate a dictionary named products with the contents of the products.csv file.
        for row in reader:
            number = row[0]
            name = row[1]
            price = row[2]

            products[number] = [name, price]

    return products

def process_request(dictionary):
    PRODUCT_NUMBER_INDEX = 0
    QUANTITY_INDEX = 1
    total_quantity = 0
    subtotal = 0
    # open the request.csv file for reading
    with open('/Users/abigailcluff/Documents/cse111/Week 9 and 10/request.csv', 'rt') as requests_file:
        reader = csv.reader(requests_file)
        next(reader)

        for row in reader:
            product_number = row[PRODUCT_NUMBER_INDEX]
            quantity = int(row[QUANTITY_INDEX])

            # Use the requested product number to find the corresponding item in products dictionary
            if product_number not in dictionary:
                print("No such product")
            else:
                request = dictionary[product_number]
                # print the product name, requested quantity, and product price
                print(f'{request[0]}: {row[QUANTITY_INDEX]} @ {request[1]}')
                # Sum the number of ordered items.
                total_quantity += quantity
                # Sum the subtotal due.
                subtotal += (float(request[1]) * quantity)
                # Compute the sales tax amount. Use 6% as the sales tax rate.
                sales_tax = round(subtotal * 0.06, 2)
                # Compute the total amount due.
                total = subtotal + sales_tax
        
        print('')
        print(f'Number of Items: {total_quantity}')
        print(f'Subtotal: {subtotal}')
        print(f'Sales Tax: {sales_tax}')
        print(f'Total: {total}')
    
def main():
    print('Inkom Emporium')
    products = read_products('/Users/abigailcluff/Documents/cse111/Week 9 and 10/products.csv')
    print('')
    process_request(products)
    print('')
    print('Thank you for shopping at the Inkom Emporium.')
    print(string)

main()