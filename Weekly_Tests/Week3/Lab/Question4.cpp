/* Write a program that accepts two integers and returns true if either one is 5, or their sum, or difference, is 5 */


// https://www.w3schools.com/c/c_switch.php
// 

#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int main()
{

int nx = 0;
int ny = 0;

printf("Enter two integers: ");
scanf("%d %d", &nx, &ny);


if ((nx ==5) || (ny== 5)) 
{
  printf("one of these is equal to 5");

} else if ((nx + ny == 5)) 
{
    printf("Total 5 when added together");
} else if ((nx - ny == 5)) 
{
    printf("5 is the differnce between them");
} else
{
    printf("Neither are 5 and do not equal 5 when added together\n");
}

}