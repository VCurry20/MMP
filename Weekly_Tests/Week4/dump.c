struct StudentModule
{
    /* data */
   // struct Student Module ; 
    int enrollments;
};





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
    



