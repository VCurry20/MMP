from dataclasses import dataclass, field
from typing import List
import csv

@dataclass
class Product:
    name: str
    price: float = 0.0

    def __repr__(self):
        return f'NAME: {self.name} PRICE: {self.price}'


@dataclass 
class ProductStock:
    product: Product
    quantity: int

    def name(self):
            return self.product.name
        
    def unit_price(self):
            return self.product.price
            
    def cost(self):
            return self.unit_price() * self.quantity
            
    def __repr__(self):
            return f"PRODUCT: {self.product} QUANTITY: {self.quantity} PRICE: {self.product.price}"


@dataclass 
class Shop:
    cash: float = 0.0
    stock: List[ProductStock] = field(default_factory=list)

    def create_and_stock_shop(self):
        with open('stock.csv') as csv_file:
        # read the csv, noting that the delimiers are the ,'s
            csv_reader = csv.reader(csv_file, delimiter=',')
            # first row is after the header - next function skips the function and starts on the first two
            first_row = next(csv_reader)
            # set the cash variable - as a float - first place / first line
            self.cash= float(first_row[0])
            # for the rows in the csv file - iterate through
            for row in csv_reader:
                # save stock variable
                # set product and quantity as class product
                product = Product(row[0], float(row[1]))
                # set variable of current stock
                # each stock item is now set under product stock also
                current_stock = ProductStock(product, float(row[2]))
                # add to shop list
                self.stock.append(current_stock)
 

    
    # print the stock with the price
    def print_shop(self):
        for ProductStock in self.stock:
            print(f"Product: {ProductStock.product.name},  quantity: {ProductStock.quantity}, Price: {ProductStock.product.price}\n")

    # update the stock
    def update_stock(self, basket):
        for shop_product in self.stock:
            for customer_product in basket:
                if shop_product.product.name ==  customer_product.product.name:
                    old_quantity = shop_product.quantity
                    customer_quantity = customer_product.quantity
                    new_quantity = old_quantity - customer_quantity
                    if new_quantity < 0:
                        print(f"Warning: Insufficient stock for {customer_product.product.name}")
                        continue
                    shop_product.product.quantity = new_quantity
                    # print
                    print(f"Updated stock for {customer_product.product.name} - Old: {old_quantity}, New: {new_quantity}")


    def update_cash(self, total_cost):
    # shop cash is shop cash plus total cost
        self.cash = self.cash + total_cost
    # return shop cash
        return self.cash

    def __repr__(self):
         # print out of full shop
         print(f"Full Shop Print Out")
         print("--------------------")
         print(f"Shop Balance {self.cash}")
         print("--------------------")
         for ProductStock in self.stock:
            print(f"Product: {ProductStock.product.name},  quantity: {ProductStock.quantity}, Price: {ProductStock.product.price}\n")
         
        

@dataclass
class Customer:
    name: str = ""
    budget: float = 0.0
    shopping_list: List[ProductStock] = field(default_factory=list)

    def read_customer(self): 
        with open('customer.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.name=first_row[0]
            self.budget=float(first_row[1])
            #c = Customer(first_row[0], float(first_row[1]))
            for row in csv_reader:
                name = row[0]
                quantity =int(row[1])
                p = Product(name)
                ps = ProductStock(p, quantity)
                self.shopping_list.append(ps)

    # print shopping list
    def print_customer(self):
         print(f'CUSTOMER NAME: {self.name} \nCUSTOMER BUDGET: {self.budget}')
         for ProductStock in self.shopping_list:
             print((f'\nPRODUCT NAME: {ProductStock.product.name}, \nQUANTITY: {ProductStock.quantity}'))

    # print Budget
    def print_budget(Customer):
        print (f"The Customer Budget is €{Customer.budget}")

    # define shopping basked function / call customer & shop
    def shopping_basket(self, shop):
        # sanity test
        print("Shopping!!!!")
        # set basket
        basket = []

        # iterate through the customer products
        for order_product in self.shopping_list:
            # is product in stock - set to false and check
            product_found = False
            # iterate through products in shop
            for stock_product in shop.stock :
                # it order product name= shop product this is in stock
                if order_product.product.name == stock_product.product.name:
                    # while product found is true
                    product_found = True
                    # if order quantity is less or equal to stock quantity
                    if order_product.quantity <= stock_product.quantity:
                        # add / append to basket
                        basket.append(ProductStock(stock_product.product, order_product.quantity))
                        # if this is not true output error warning
                    else:
                        print("----------------Warning--------------------")
                        print("Insufficient stock for:", order_product.product.name)

            # if product not in the shop - return this warning
            if not product_found:
                print("----------------Warning--------------------")
                print("Product not found in stock:", order_product.product.name)
        return basket


    def total_cost(self, shop):
        # sanity ck
        print("this is the cost function")
        # set the initial cost at zero
        cost =0.0
        # iterate through basked
        for i in self.shopping_list:
            # match the products with the shop products
            shop_product = next((p for p in shop.stock if p.product.name == i.product.name), None)
            # work out the cost
            if shop_product:
                cost += i.quantity * shop_product.product.price
            # or else output an error message
            else:
                print(f"Product {i.product.name} not found in the shop.")
        # return the cost 
        return cost
    
    # check budget function / call customer & total cost
    def check_budget(self, total_cost):
    # if customer budget is less than total cost
        if self.budget < total_cost:
            # print the following
            print ("You have insufficent funds, please review and resubmit your order")
            # break
            return False
        # else print the following
        else:
            print("You have sufficent funds to continue")
            # continue
            return True
        
    def update_budget(self, total_cost):
        #print("budget update")
        # customer budget equals customer budget minus total cost
        Customer.budget = Customer.budget-total_cost
        # return the new updated budget
        return Customer.budget


@dataclass
class ManualOrder:
    #name: input ("Enter your name: ")
   # budget: float(input("Enter your budget: EUR "))
    product: Product
    quantity: int
    #shopping_list: List[ProductStock] = field(default_factory=list)

    def Add_order ():
        m_order={}
        # Loop while True
        live = True
        while live:
            # set up product dict
            product = {}
            # product name is input from the following
            product["name"] = input ("\nWhat product would you like to order?")
            # product quantity is a float from the following 
            product["quantity"] = float(input(f"How many {product['name']} would you like to add to your order? "))
            # manual order products add to product list
            m_order ["products"].append(product)
            # end is wither there is additional input or now
            end = input ("\nDo you want to add additional products? Choose - Yes or No ")
            # end if the input is no - lower case
            if end.lower() == "no":
                ordering =False
        # return manual order
        return m_order


# define function - a function or action sequence
# define display
# this how how the display will look when the program is called and takes an input choice
# the program will come back to this after it finished all the options other than 6
def displaymenu ():
    # print out the various options
    print ("Please see your shopping options")
    print ("\t(1) View Shop Balance")
    print ("\t(2) View Stock")
    print ("\t(3) View Customer Order")
    print ("\t(4) Start Shopping")
    print ("\t(5) Input Manual Order")
    print ("\t(6) Quit")
    # set variable choice - it will be which ever input is choosen
    choice = input ("Choose one option (1/2/3/4/5/6):") .strip()
    # print new line - - this is for formatting
    print("\n")
    # return - output choice variable
    return choice

# define purchase - again this is a display / input function
def purchase():
    # print out display
    print ("Would you like to purchase these iteams")
    print ("\t(1) Yes, please continue to payment")
    print ("\t(2) I would like to submit another order")
    print ("\t(3) Exit")
    # set choice variable
    choice = input ("Choose one option (1/2/3):") .strip()
    # print new line - - this is for formatting
    print("\n")
    # return - output choice variable
    return choice





def main():
    print("Hello World!")
    # print out
    print("Welcome to the Shop")
    # set choice as input from display menu function
    choice = displaymenu()
    shop = Shop()
    customer= Customer()
    
    # while choice is no 6 continue
    while choice != '6':
        # if choice is 1
        if choice == '1':
            # print
            print("You have choosen to review the shop balance")
            shop.create_and_stock_shop()
            print(f"The shop currently has a balance of € {shop.cash}")
            print("\n")
            
        # if choice is 2
        elif choice =='2':
            # print
            print("------------------------------------")
            print("You have choosen to review the stock")
            print("------------------------------------")
            #shop.create_and_stock_shop()
            shop.print_shop()
            print("\n")

        # if choice is 3
        elif choice =='3':
            ## print
            print("------------------------------------")
            print("Customer Order is:")
            print("------------------------------------")
            customer.read_customer() 
            customer.print_customer()
            print("\n")

        # if choice is 4
        elif choice =='4':
                # print
                print("We have inputted your shopping list, and checked the stock:")
                shop.create_and_stock_shop()
                customer.read_customer()
                shopping_list=customer.shopping_list
                shopping=(customer.shopping_basket(shop))
                
                print("We have added the following to your shopping basket", shopping)

                price = sum(product_stock.product.price * product_stock.quantity for product_stock in shopping)
                print("The total cost for these items is: €", "{:.2f}".format(price))
                # print new line
                print("\n")
                # set choice variable
                choice = purchase()
                # while choice is not 3
                while choice != '3':
                    # if choice is 1
                    if choice == '1':
                        # print
                        print("Proceeding to purchase\n")
                        # check if fund are available
                        has_funds = customer.check_budget(price)
                        if has_funds:
                                # print
                                print("Your starting budget was: €",customer.budget)
                                # new budget is update budget function calling customer and price
                                nu_budget = customer.update_budget(customer.budget)
                                # print
                                print("Your new budget is: €", "%.2f" % nu_budget)
                                # new cash is update cash function calling shop & price
                                nu_cash = shop.update_cash(price)
                                # print
                                print("\nThe Shop's new cash balance is: €", "%.2f" % nu_cash)
                                # print new line
                                print("\n")
                                # update stock - calling shopping & function
                                shop.update_stock(shopping)
                                # print new line
                                print("\n")
                                # print
                                print("Returning to Main Menu")
                                break
                        else:
                            # if not return
                            print("Reverting to main menu")
                            pass

                    elif choice =='2':
                        # change order
                        print("Input new order file - please choose option 3 on the main menu")
                        break   

                    else:
                        break

        # if choice is 5
        elif choice =='5':
                # print("why isnt this working?")
                print("We will now process your manual order")
                print("\n")
                print("------------------------------------")
                print("We currently have the following in stock")
                print("------------------------------------")  
                # set shop variable        
                shop = shop.create_and_stock_shop()
                # print shop stock
                shop.print_shop(shop)
                # print new line
                print("\n")
                # customer variable is input to add order function
                customer= shop.Add_order()
                # shopping = shopping basket function calling customer and shop data
                shopping= shop.shopping_basket(customer, shop)
                # print
                print("We have added the following to shopping basket", shopping)
                # price variable = total cost of shopping - calling shopping and shop
                price= shop.total_cost(shopping, shop)
                # print
                print("The total cost for these items is: €","%.2f" %price)
                # print new line
                print("\n")
                # choice = purchase function
                choice = purchase()
                # while choice is not 3
                while choice != '3':
                    # if choice is 1
                    if choice == '1':
                        # print
                        print("Proceeding to purchase\n")
                        # check budget
                        has_funds = customer.check_budget(customer, price)
                        # if customer has the budget
                        if has_funds:
                                # print
                                print("Your starting budget was: €",customer["budget"])
                                # new budget is update budget function calling customer and price
                                nu_budget = customer.update_budget(customer,price)
                                # print
                                print("Your new budget is: €", "%.2f" % nu_budget)
                                # new cash is update cash function calling shop & price
                                nu_cash = shop.update_cash(shop,price)
                                # print
                                print("The Shop's new cash balance is: €", "%.2f" % nu_cash)
                                # print new line
                                print("\n")
                                # update stock - calling shopping & function
                                shop.update_stock(shopping, shop)
                                # print new line
                                print("\n")
                                # print
                                print("Returning to Main Menu")
                                break
                        else:
                            # or else revert to main menu
                            print("Reverting to main menu")
                            pass

                    # if choice is 2               
                    elif choice =='2':
                            # print
                            print("Input new order file - please choose option 3 on the main menu")
                            break 
                    # else break out
                    else:
                            break

        # if choice is 6
        elif choice =='6':
            # print
            print("Goodbye")
            # break
            break    

        choice = displaymenu()


# call main function and also end it
if __name__=="__main__": 
    main()