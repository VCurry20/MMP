/* Write a program to check if two or more non-negative given integers have the same rightmost digit. */

// https://www.w3schools.com/c/c_booleans.php
// https://gist.github.com/Dimich7/cad76fbe56e923072fb0
// https://www.geeksforgeeks.org/modulo-operator-in-c-cpp-with-examples/



#include <stdio.h>
#include <stdlib.h>

int main(void){


int a;
int b;

printf("Type two numbers & press enter: \n");

scanf("%d %d", &a, &b);

if (abs(a % 10) == abs(b % 10)) 
{
  printf("They have the same right hand digit");

} else 
{
    printf("Not a match - have I learned nothing but if statements?!");
}

}