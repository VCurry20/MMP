import csv

class Product:
    # if no price is listed it will go to zero automatically - helpful when you do not know everthing
    def __init__(self, name, price=0):
        self.name = name
        self.price = price
    
    # print rep
    # product stock calls from this formatting too
    def __repr__(self):
        return f'NAME: {self.name} PRICE: {self.price}'

class ProductStock:
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    # just for getting out the name
    # convenience method
    def name(self):
        return self.product.name
    
    # just for getting out the name
    # convenience method
    def unit_price(self):
        return self.product.price
        
    # product stock is now responsible for how much it costs
    # function within class
    # for what the customer wants to but and also to check what is in the shop
    # you only have to have it here and not write if for all other classes
    # encapsulation
    def cost(self):
        return self.unit_price() * self.quantity
    
    # prints out product and quantity
    # takes product from product class
    # defaults to zero if nothing listed
    # this relies on the product class and pulls from there
    def __repr__(self):
        return f"{self.product} QUANTITY: {self.quantity}"

class Customer:

    def __init__(self, path):
        # shopping list - customer csv pulled in here
        # the proc it was in a def
        self.shopping_list = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.name = first_row[0]
            self.budget = float(first_row[1])
            for row in csv_reader:
                name = row[0]
                quantity = float(row[1])
                p = Product(name)
                ps = ProductStock(p, quantity)
                # add this to the shopping list which is wthin this code
                self.shopping_list.append(ps) 
                
    def calculate_costs(self, price_list):
        for shop_item in price_list:
            for list_item in self.shopping_list:
                if (list_item.name() == shop_item.name()):
                    list_item.product.price = shop_item.unit_price()
    
    def order_cost(self):
        cost = 0
        
        for list_item in self.shopping_list:
            cost += list_item.cost()
        
        return cost
    
    # print rep
    def __repr__(self):
        
        str = f"{self.name} wants to buy"
        for item in self.shopping_list:
            cost = item.cost()
            str += f"\n{item}"
            if (cost == 0):
                str += f" {self.name} doesn't know how much that costs :("
            else:
                str += f" COST: {cost}"
                
        str += f"\nThe cost would be: {self.order_cost()}, he would have {self.budget - self.order_cost()} left"
        return str 
        
class Shop:
    
    # path to csv
    def __init__(self, path):
        self.stock = []
        # similar to procedural
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.cash = float(first_row[0])
            for row in csv_reader:
                # note this is calling the other class
                p = Product(row[0], float(row[1]))
                # note this is calling the other class
                ps = ProductStock(p, float(row[2]))
                self.stock.append(ps)
    
    # return text based representation - string in this case
    def __repr__(self):
        str = ""
        str += f'Shop has {self.cash} in cash\n'
        # take from the above self stock list
        for item in self.stock:
            # this formatting comes from the product stock class
            str += f"{item}\n"
        return str


# print out the rep method from shop class
# if there was no repr method in shop it would take it from its parent class
# no parent class for shop
# when there is no parent class ...who knows!?
s = Shop("stock.csv")
#print(s)

c = Customer("../customer.csv")
c.calculate_costs(s.stock)
print(c)