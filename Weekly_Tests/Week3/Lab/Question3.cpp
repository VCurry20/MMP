/* Write a program to compute the sum of the two given integers. 
If the sum is in the range 10..20 inclusive return
30. */


// https://www.programiz.com/c-programming/c-do-while-loops
// https://www.w3schools.com/c/c_variables.php



#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int main()
{

int nx = 0;
int ny = 0;

printf("Enter two integers: ");
scanf("%d %d", &nx, &ny);


int nNew = nx + ny;

if (( nNew >= 10 && nNew <= 20 ))
{
  printf("30");

} else
{
    printf("not 30\n");
}

}