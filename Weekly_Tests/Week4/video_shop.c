/* Build a simulation of a shop in C */

// Entities
// Shop
// Customer(s)
// Product(s)
// Stock

// Model the entites
// Print product info
// print customer info

// add item to customer list
// read in stock from a file

#include <string.h>   /* allows us to break down the CSV file - string tokeniser */
#include <stddef.h>   /* https://www.tutorialspoint.com/c_standard_library/stddef_h.htm */
#include <stdio.h>    /* https://www.tutorialspoint.com/c_standard_library/stdio_h.htm */
#include <stdlib.h>   /* https://www.tutorialspoint.com/c_standard_library/stdlib_h.htm */
#include <errno.h>    /* gives errors a code output? */

int getline(char **lineptr, size_t *n, FILE *stream)
{
static char line[256];
char *ptr;
unsigned int len;

   if (lineptr == NULL || n == NULL)
   {
      errno = EINVAL;
      return -1;
   }

   if (ferror (stream))
      return -1;

   if (feof(stream))
      return -1;

   fgets(line,256,stream);

   ptr = strchr(line,'\n');
   if (ptr)
      *ptr = '\0';

   len = strlen(line);

   if ((len+1) < 256)
   {
      ptr = realloc(*lineptr, 256);
      if (ptr == NULL)
         return(-1);
      *lineptr = ptr;
      *n = 256;
   }

   strcpy(*lineptr,line);
   return(len);
}






// data structures

struct Product 
{
    /* data */
    char* name;
    double price;

};


struct ProductStock
{
    /* data - contains the product struct above Product - links product with the stock we have */
    /* a struct can hold any data type including another struct */
    struct Product product;
    int quantity;

};


struct Shop
{
    /* data */
    double cash;
    struct ProductStock stock[20];
    int index;

};


struct Customer
{
    /* data */
    char* name;
    double budget;
    struct ProductStock shoppinglist[10];
    // adding index to let us keep track of how many items they have bought
    int index;
};



// method to print out the product info
// void methods so it prints but doesnt action anything

void printProduct(struct Product p)
{
  printf("PRODUCT NAME: %s\nPRODUCT PRICE: %.2f\n", p.name, p.price); 
  printf("--------------------\n"); 
}


void printCustomer(struct Customer c )
{
  printf("CUSTOMER NAME: %s\nCUSTOMER BUDGET: %.2f\n", c.name, c.budget); 
  printf("--------------------\n");  
  // initiating index for dominic
  for (int i = 0; i< c.index ; i++)
  {
    printProduct(c.shoppinglist[i].product);
    // chain of access - go to customer by customer name, their shopping list, from the array getting the individual product stock quantity - could also get product name ( giving exact directions where to go)
    printf("%s ORDERS %d OF THE ABOVE PRODUCT\n", c.name, c.shoppinglist[i].quantity);

    double cost = c.shoppinglist[i].quantity * c.shoppinglist[i].product.price;
    printf("The cost to %s will be €%.2f\n", c.name, cost );
  }
}

// read in from CSV file
// break apart
// create stock variable and add to struct that represents shop

struct Shop createAndStockShop()
{
  struct Shop shop = { 200 };
  
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("stock.csv", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        //printf("Retrieved line of length %zu:\n", read);
        // printf("%s IS A LINE\n", line);
        char *n = strtok(line, ",");   /// break line apart on commma - c pulls data in as a character array
        ///printf("NAME OF PRODUCT %s\n" , name);
        char *p = strtok(NULL, ",");   /// skip first and go to second - null is a special character, not passing any info
        ///printf("PRICE OF PRODUCT %s\n" , price);
        char *q = strtok(NULL, ",");   /// getting Quantity here
        int quantity = atoi(q);
        double price = atof(p);
        char *name = malloc(sizeof(char) *50);
        strcpy(name, n);
        struct Product Product = {name, price};
        struct ProductStock stockitem = {Product, quantity};
        shop.stock[shop.index++] = stockitem;
        ///printf("QUANTITY OF PRODUCT %s\n" , quantity);
      

    }

  return shop;

}

void printShop(struct Shop s)
{
  printf("Shop has %.2f in cash\n", s.cash);
  for (int i =0; i < s.index; i++)
  {
    printProduct(s.stock[i].product);
    printf("THE SHOP HAS %d of the above\n", s.stock[i].quantity );
  }

}



// some of these outputs should be methods
int main(void)
{
    // struct Customer dominic = {"Dominic", 100.0};
    // // printf("Customer name is %s\n", dominic.name);
    // //printCustomer(dominic);

    // // add product
    struct Product coke = {"can of coke", 1.10};
    // struct Product bread = {"bread", 0.7};
    // // printf("The %s costs %f\n", coke.name, coke.price);
    printProduct(coke);


    // // add stock
    // struct ProductStock cokestock = {coke, 20};
    // struct ProductStock breadstock = {bread, 2};
    // //printf("The shop has %d of the product %s\n", cokestock.quantity, cokestock.product.name);


    // // following code adds to dominics shopping list - counts what is in it and increases by one
    // dominic.shoppinglist[dominic.index++] = cokestock;
    // dominic.shoppinglist[dominic.index++] = breadstock;

    //printCustomer(dominic);

    struct Shop shop = createAndStockShop();
    printShop(shop);



    return 0;
}
