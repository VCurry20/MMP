/* Doing Questions from Wk1 in C code as opposed to Python */
/* Modify the previous program such that only multiples of three or five are considered in the sum, e.g.
3, 5, 6, 9, 10, 12, 15 for n=17 */

#include <stdio.h>

/* making a function */
int sumNumbers(int n)
{
    int sum = 0;
    /* for loop - index i, i less than or equal to n, every time increment i++ (add one) */
    /* start point i=0, checks its equal or less than 0 and then completes action */
    /* if i divided by 5 equals 0 or i divided by 3 equals 0 - complete sum+=i */
    for (int i = 0; i<=n; i++)
    {
        if (((i%5)==0) || ((i%3)==0))
        {
            /* comment out this line if needed - this is just a check and a print out of the numbers used in the sum */
            printf("Found a Multiple of 5 or 3, it was %d\n", i);
            sum+=i;
        }
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