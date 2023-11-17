/* Write a program to check two given integers, and return true if one of them is 30 or if their sum is 30. */


// https://www.programiz.com/c-programming/examples/add-numbers
// https://www.w3schools.com/c/c_booleans.php



#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int main()
{

int nx = 0;
int ny = 0;

printf("Enter two integers: ");
scanf("%d %d", &nx, &ny);


if ((nx ==30)|| (ny== 30)) 
{
  printf("one of these is equal to 30");

} else if ((nx + ny == 30)) 
{
    printf("Total 30 when added together");
} else
{
    printf("Neither are 30 and do not equal 30 when added together\n");
}

}
