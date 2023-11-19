# procedural shop in python
# no classes or objects - dictionarys instead
# this will match the C version

import csv


#csv_reader = csv.reader(csv_file, delimiter=',')
 #       first_row = next(csv_reader)
  #      s.cash = float(first_row[0])

def create_and_stock_shop():
    shop = {}
    with open ('stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        shop["cash"] =float (first_row[0])
        shop["products"] = []

        for row in csv_reader:
            product = {}

            product["name"] = row[0]
            product["price"] = row[1]
            product["quantity"] = row[2]

            shop["products"].append(product)

    return shop

            #print_product(product)
        
   #pass 



def read_customer():
    customer = {}
    with open ('customer.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        customer["name"] =(first_row[0])
        customer["cash"] =float(first_row[1])
        customer["products"] = []

        for row in csv_reader:
            product = {}

            product["name"] = row[0]
            product["quantity"] = row[1]
            

            customer["products"].append(product)

    return customer

            #print_product(product)
    pass

def print_product(product):
    print(f'NAME:{product["name"] }, PRICE:{product["price"] }, QUANTITY{product["quantity"] }')
    #print(f'CUSTOMER NAME: {product["name"] }')



def print_customer(customer):
    print(f'NAME:{customer["name"] }, CASH:{customer["cash"] }')
    for product in customer["products"]:
        print(f'NAME:{product["name"] }, QUANTITY{product["quantity"] }')



def print_shop(shop):
    # wrap the initial create shop in the shop variable and add initial value
    print(f'INITAL CASH VALUE{shop["cash"] }')
    for product in shop["products"]:
        print_product(product)


shop = create_and_stock_shop()

print_shop(shop)

customer = read_customer()
print_customer(customer)

