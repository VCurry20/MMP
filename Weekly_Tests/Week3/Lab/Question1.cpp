/* Write a program to calculate the absolute difference between n and 51. If n is greater than 51 return triple the
absolute difference */



#include <stdio.h>
#include <stdlib.h> //using  stdlib.h for abs() function

int sum51(int n)
{
    int x = 51; // Declare and initialize constant variable 'x'

    if (n > x) // Check if 'n' is greater than 'x'
    {
        return (n - x) * 3; // Return the result of the expression (n - x) multiplied by 3
    }
    else
    {
        return n; // Return the result of the expression x minus n
    }

    
}


// review video 2 = maybe no function is needed?"!
"

int main (void){

    int n = 0;

    printf("Enter a number\n" );

    scanf("%d", &n);

    int s = sum51(n);

    printf(" checking the sum function %d", s);

    s=abs(s);

    printf("Absolute Value = %d\n", n, s);
    return 0;

}



