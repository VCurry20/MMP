/* Doing Questions from Wk1 in C code as opposed to Python */
/* Write a program that asks the user for a number n and prints the sum of the numbers 1 to n */
/* video 3.1 */
/* Video 3 process as a function - procedural programming */



#include <stdio.h>

/* making a function */
int sumNumbers(int n)
{
    int sum = 0;
    /* for loop - index i, i less than or equal to n, every time increment i++ (add one) */
    /* start point i=0, checks its equal or less than 0 and then completes action */
    for (int i = 0; i<=n; i++)
    {
        /* short hand for the below would be sum+=i */
        sum = sum + i;
    }

    return sum;

}


int main (void){

    int n = 0;

    printf("Enter a number\n");

    /* scan input - %d is a whole number, take this input and put it in the memory space for n */    
    scanf("%d", &n);

    /* call the function */
    int s = sumNumbers(n);

    printf("The Sum of 1 to %d is %d\n", n, s);

}