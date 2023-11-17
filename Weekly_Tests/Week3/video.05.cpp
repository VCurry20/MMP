/* Doing Questions from Wk1 in C code as opposed to Python */
/* Write a program that asks the user for a number n and gives them the possibility to choose between
computing the sum and computing the product of 1,. . . ,n */

#include <stdio.h>
#include <string.h>

/* functions */
int sumOfNumbers(int n)
{
    int sum = 0;
    for (int i = 0; i<=n; i++)
    {
        sum+=i;  
    }
    return sum;
}

int productOfNumbers(int n)
{
    int sum = 1;
    for (int i = 1; i<=n; i++)
    {
        sum*=i;  
    }
    return sum;
}


int main (void){

    /* Declare Variables */
    int n = 0;
    char name[20];

    printf("Enter a number\n");
    /* scan input - %d is a whole number, take this input and put it in the memory space for n */    
    scanf("%d", &n);


    /* Clears the input buffer */
    while ((getchar()) != '\n');

    printf("Do you want to calculate sum or product?\n");
    /* fgets input  */ 
    fgets(name, 20, stdin);

    /* strips down spaces - removes the enter when we add it to submit name, and \0 terminates at the end of our input */
    /* 20 characters only accept name and new line */
    /* Clears \n from name variable */
    name[strcspn(name,"\n")] ='\0';


    /* call the function */  
    if ((strcmp(name, "sum") ==0 ))
    {
        // sum
        int s = sumOfNumbers(n);
        printf("The Sum of 1 to %d is %d\n", n, s);
    }
    else if ((strcmp(name, "product") ==0 ))
    {
        // product
        int p = productOfNumbers(n);
        printf("The product of 1 to %d is %d\n", n, p);
    }
    else
    {
        printf("The Program does not understand your input");
    }

}