#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Product {
	char* name;
	double price;
	
};

struct ProductStock {
	struct Product product;
	int quantity;
};

struct Shop {
	double cash;
	struct ProductStock stock[20];
	int index;
};

struct Customer {
	char* name;
	double budget;
	struct ProductStock shoppingList[10];

	int index;
};

// Function prototypes
void display_menu();
void purchase();
void create_and_stock_shop();
void print_product(product);
void Customer read_customer();
void print_customer(Customer);
void print_shop(Shop);
void shopping_basket(Customer, Shop);
void total_cost(Customer, Shop);
void check_budget(Customer, total_cost);
void update_budget(Customer, total_cost);
void update_cash(Shop , total_cost);
void update_stock(Customer, Shop);
void add_order();



void display_menu()
{char choice;

	printf ("Please see your shopping options");
    printf ("\n(1) View Shop Balance");
    printf("\n(2) View Stock");
    printf ("\n(3) View Customer Order");
    printf ("\n(4) Start Shopping");
    printf ("\n(5) Input Manual Order");
    printf ("\n(6) Quit");
	printf("Choose one option (1/2/3/4/5/6): ");

scanf("%c", &choice);}

void purchase()
{char choice;
	printf ("Would you like to purchase these iteams");
    printf ("\t(1) Yes, please continue to payment");
    printf ("\t(2) I would like to submit another order");
    printf ("\t(3) Exit");
	printf ("Choose one option (1/2/3):");

scanf("%c", &choice);}


struct Shop createAndStockShop()
{
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("/stock.csv", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

	read = getline(&line, &len, fp);
	float cash = atof(line);
	// printf("cash in shop is %.2f\n", cash);
	
	struct Shop shop = { cash };

    while ((read = getline(&line, &len, fp)) != -1) {
        // printf("Retrieved line of length %zu:\n", read);
        // printf("%s IS A LINE", line);
		char *n = strtok(line, ",");
		char *p = strtok(NULL, ",");
		char *q = strtok(NULL, ",");
		int quantity = atoi(q);
		double price = atof(p);
		char *name = malloc(sizeof(char) * 50);
		strcpy(name, n);
		struct Product product = { name, price };
		struct ProductStock stockItem = { product, quantity };
		shop.stock[shop.index++] = stockItem;
		// printf("NAME OF PRODUCT %s PRICE %.2f QUANTITY %d\n", name, price, quantity);
    }
	
	return shop;
}

void printProduct(struct Product p)
{
	printf("PRODUCT NAME: %s \nPRODUCT PRICE: %.2f\n", p.name, p.price);
	printf("-------------\n");
}

struct Customer read_customer() {
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("customer.csv", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    // Read the first line to get customer name and budget
    read = getline(&line, &len, fp);
    char *name = strtok(line, ",");
    double budget = atof(strtok(NULL, ","));
    struct Customer customer = {name, budget};

    // Read the remaining lines for the shopping list
    while ((read = getline(&line, &len, fp)) != -1) {
        char *n = strtok(line, ",");
        char *q = strtok(NULL, ",");
        int quantity = atoi(q);

        char *productName = malloc(sizeof(char) * 50);
        strcpy(productName, n);

        struct Product product = {productName, 0.0}; // Assuming price is not available in the customer file
        struct ProductStock stockItem = {product, quantity};

        customer.shoppingList[customer.index++] = stockItem;
    }

    fclose(fp);
    if (line)
        free(line);

    return customer;
}

void printCustomer(struct Customer c)
{
	printf("CUSTOMER NAME: %s \nCUSTOMER BUDGET: %.2f\n", c.name, c.budget);
	printf("-------------\n");
	for(int i = 0; i < c.index; i++)
	{
		printProduct(c.shoppingList[i].product);
		printf("%s ORDERS %d OF ABOVE PRODUCT\n", c.name, c.shoppingList[i].quantity);
		double cost = c.shoppingList[i].quantity * c.shoppingList[i].product.price; 
		printf("The cost to %s will be €%.2f\n", c.name, cost);
	}
}



void printShop(struct Shop s)
{
	printf("Shop has %.2f in cash\n", s.cash);
	for (int i = 0; i < s.index; i++)
	{
		printProduct(s.stock[i].product);
		printf("The shop has %d of the above\n", s.stock[i].quantity);
	}
}


void total_cost(struct customer, struct Shop Product);
{
    //printf("this is the cost function")
    
    cost =0.0
    // iterate through basked
    for i in self.shopping_list:
    // match the products with the shop products
    shop_product = next((p for p in shop.stock if p.product.name == i.product.name), None)
    // work out the cost
        if shop_product:
        cost += i.quantity * shop_product.product.price
        or else output an error message
        else:
        printf("Product %c not found in the shop.", {i.product.name})
        
        return cost
}


int main(void) {

display_menu();
x = 6
switch (x); 
{

	case 1:
		// print shop stock
		printf("You have choosen to review the shop balance");
		struct Shop shop = createAndStockShop();
		printf("The shop currently has a balance of €%.2f\n", shop.cash);
		break;
	
	

	case 2:
		// print shop balance
		printf("------------------------------------");
		printf("You have choosen to review the stock");
		printf("------------------------------------");
		struct Shop shop = createAndStockShop();
		printShop(shop);
		printf("\n");
		break;


	case 3:
		// print customer order
		printf("------------------------------------");
		printf("Customer Order is:");
		printf("------------------------------------");
		struct customer read_customer();
		printCustomer(Customer);
		printf("\n");
    

	case 4:
	// 
	printf("We have inputted your shopping list, and checked the stock:")
    
	shop = create_and_stock_shop()
                // read customer file
                customer= read_customer()
                // shopping variable is shopping basket calling customer and shop
                shopping= shopping_basket(customer, shop)
                // print
                printf("We have added the following to shopping basket %c", {shopping})
                // set price variable as output from total cost function
                price= total_cost(shopping, shop)
                // print 
                printf("The total cost for these items is: €","%d%.2f", {price})
                // print new line
                printf("\n")
                //set choice variable
                choice = purchase()
                // while choice is not 3
                while choice != '3':
                    // if choice is 1
                    if choice == '1':
                        // print
                        printf("Proceeding to purchase\n")
                        // check if fund are available
                        has_funds = check_budget(customer, price)
                        if has_funds:
                                # print
                                print("Your starting budget was: €",customer["budget"])
                                # new budget is update budget function calling customer and price
                                nu_budget = update_budget(customer,price)
                                # print
                                print("Your new budget is: €", "%.2f" % nu_budget)
                                # new cash is update cash function calling shop & price
                                nu_cash = update_cash(shop,price)
                                # print
                                print("\nThe Shop's new cash balance is: €", "%.2f" % nu_cash)
                                # print new line
                                print("\n")
                                # update stock - calling shopping & function
                                update_stock(shopping, shop)
                                # print new line
                                print("\n")
                                # print
                                print("Returning to Main Menu")
                                break
                        else:{
                            // if not return
                            printf("Reverting to main menu");}
                            pass

                    elif choice =='2':{
                        // change order
                        print("Input new order file - please choose option 3 on the main menu");
					}
                        break;  

                    else:
                        break


	case 5:
	// 
	

	case 6:
		printf("GoodBye");
		break;

}
    return 0;
}