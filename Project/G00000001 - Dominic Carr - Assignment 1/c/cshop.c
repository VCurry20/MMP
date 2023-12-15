#include <string.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

struct Product {
    char *name;
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
    char *name;
    double budget;
    struct ProductStock shoppingList[10];
    int index;
};

// Function prototypes
void display_menu();
void purchase();
struct Shop create_and_stock_shop();
void print_product(struct Product);
struct Customer read_customer();
void print_customer(struct Customer);
void print_shop(struct Shop);
double total_cost(struct Customer, struct Shop);
int check_budget(struct Customer, double);
double update_budget(struct Customer *customer, double total_cost);
void update_cash(struct Shop *shop, double);
void update_stock(struct Customer *customer, struct Shop *shop);
void shopping_basket(struct Customer customer, struct Shop shop);

void display_menu()
{
    char choice;

    printf("Please see your shopping options");
    printf("\n(1) View Shop Balance");
    printf("\n(2) View Stock");
    printf("\n(3) View Customer Order");
    printf("\n(4) Start Shopping");
    printf("\n(5) Input Manual Order");
    printf("\n(6) Quit");
    printf("Choose one option (1/2/3/4/5/6): ");

    scanf(" %c", &choice);
}

void purchase()
{
    char choice;
    printf("Would you like to purchase these items");
    printf("\t(1) Yes, please continue to payment");
    printf("\t(2) I would like to submit another order");
    printf("\t(3) Exit");
    printf("Choose one option (1/2/3): ");

    scanf(" %c", &choice);
}

struct Shop create_and_stock_shop()
{
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("stock.csv", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    read = getline(&line, &len, fp);
    float cash = atof(line);

    struct Shop shop = {cash};

    while ((read = getline(&line, &len, fp)) != -1)
    {
        char *n = strtok(line, ",");
        char *p = strtok(NULL, ",");
        char *q = strtok(NULL, ",");
        int quantity = atoi(q);
        double price = atof(p);
        char *name = malloc(sizeof(char) * 50);
        strcpy(name, n);
        struct Product product = {name, price};
        struct ProductStock stockItem = {product, quantity};
        shop.stock[shop.index++] = stockItem;
    }

    fclose(fp);
    if (line)
        free(line);

    return shop;
}

void print_product(struct Product p)
{
    printf("PRODUCT NAME: %s \nPRODUCT PRICE: %.2f\n", p.name, p.price);
    printf("-------------\n");
}

struct Customer read_customer()
{
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("customer.csv", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    read = getline(&line, &len, fp);
    char *name = strtok(line, ",");
    double budget = atof(strtok(NULL, ","));
    struct Customer customer = {name, budget};

    while ((read = getline(&line, &len, fp)) != -1)
    {
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

void print_customer(struct Customer c)
{
    printf("CUSTOMER NAME: %s \nCUSTOMER BUDGET: %.2f\n", c.name, c.budget);
    printf("-------------\n");
    for (int i = 0; i < c.index; i++)
    {
        print_product(c.shoppingList[i].product);
        printf("%s ORDERS %d OF ABOVE PRODUCT\n", c.name, c.shoppingList[i].quantity);
        double cost = c.shoppingList[i].quantity * c.shoppingList[i].product.price;
        printf("The cost to %s will be €%.2f\n", c.name, cost);
    }
}

void print_shop(struct Shop s)
{
    printf("Shop has %.2f in cash\n", s.cash);
    for (int i = 0; i < s.index; i++)
    {
        print_product(s.stock[i].product);
        printf("The shop has %d of the above\n", s.stock[i].quantity);
    }
}

double total_cost(struct Customer c, struct Shop s)
{
    double cost = 0.0;

    for (int i = 0; i < c.index; i++)
    {
        struct ProductStock *shop_product = NULL;

        for (int j = 0; j < s.index; j++)
        {
            if (strcmp(s.stock[j].product.name, c.shoppingList[i].product.name) == 0)
            {
                shop_product = &s.stock[j];
                break;
            }
        }

        if (shop_product != NULL)
        {
            cost += c.shoppingList[i].quantity * shop_product->product.price;
        }
        else
        {
            printf("Product %s not found in the shop.\n", c.shoppingList[i].product.name);
        }
    }

    return cost;
}

int check_budget(struct Customer customer, double total_cost)
{
    // If customer budget is less than total cost
    if (customer.budget < total_cost)
    {
        // Print the following
        printf("You have insufficient funds, please review and resubmit your order\n");
        // Return false
        return 0;
    }
    else
    {
        // Print the following
        printf("You have sufficient funds to continue\n");
        // Return true
        return 1;
    }
}

double update_budget(struct Customer *customer, double total_cost)
{
    // printf("budget update\n");
    // Customer budget equals Customer budget minus total cost
    customer->budget -= total_cost;
    // Return the new updated budget
    return customer->budget;
}

void update_cash(struct Shop *shop, double total_cost)
{
    // Shop cash is Shop cash plus total cost
    shop->cash += total_cost;
    // Return Shop cash
}

void update_stock(struct Customer *customer, struct Shop *shop)
{
    // Loop through each product in the customer's shopping list
    for (int i = 0; i < customer->index; i++)
    {
        // Loop through each product in the shop's stock
        for (int j = 0; j < shop->index; j++)
        {
            // If product names match
            if (strcmp(customer->shoppingList[i].product.name, shop->stock[j].product.name) == 0)
            {
                // Update the quantity in the shop's stock
                shop->stock[j].quantity -= customer->shoppingList[i].quantity;
                printf("Updated stock for %s - Old: %d, New: %d\n",
                       customer->shoppingList[i].product.name,
                       customer->shoppingList[i].quantity + shop->stock[j].quantity,
                       shop->stock[j].quantity);
                break;
            }
        }
    }
}

void shopping_basket(struct Customer customer, struct Shop shop)
{
    double price = total_cost(customer, shop);
    printf("We have added the following to the shopping basket\n");
    printf("The total cost for these items is: €%.2f\n", price);

    printf("Choose one option (1/2/3): ");
    char choice;
    scanf(" %c", &choice);

    while (choice != '3')
    {
        if (choice == '1')
        {
            printf("Proceeding to purchase\n");
            int has_funds = check_budget(customer, price);
            if (has_funds)
            {
                printf("Your starting budget was: €%.2f\n", customer.budget);
                update_budget(&customer, price);
                printf("Your new budget is: €%.2f\n", customer.budget);
                update_cash(&shop, price);
                printf("The Shop's new cash balance is: €%.2f\n", shop.cash);
                update_stock(&customer, &shop);
                printf("Returning to Main Menu\n");
                break;
            }
            else
            {
                // If not, return
                printf("Reverting to main menu\n");
            }
        }
        else if (choice == '2')
        {
            printf("Change order - Input new order file\n");
            break;
        }
        else
        {
            break;
        }
    }
}

int main(void)
{
    display_menu();

    int x = 6;
    switch (x)
    {
    case 1:
        printf("You have chosen to review the shop balance\n");
        struct Shop shop = create_and_stock_shop();
        printf("The shop currently has a balance of €%.2f\n", shop.cash);
        break;

    case 2:
        printf("------------------------------------\n");
        printf("You have chosen to review the stock\n");
        printf("------------------------------------\n");
        struct Shop shop2 = create_and_stock_shop();
        print_shop(shop2);
        printf("\n");
        break;

    case 3:
        printf("------------------------------------\n");
        printf("Customer Order is:\n");
        printf("------------------------------------\n");
        struct Customer customer = read_customer();
        print_customer(customer);
        printf("\n");
        break;

    case 4:
        printf("We have inputted your shopping list, and checked the stock:\n");
        shopping_basket(customer, shop);
        break;

    case 5:
        printf("Manual order processing not implemented\n");
        break;

    case 6:
        printf("Goodbye\n");
        break;
    }

    return 0;
}
