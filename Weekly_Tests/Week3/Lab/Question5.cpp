/* Write a program to check if y is greater than x, and z is greater than y from three given integers x, y, z. 
Print appropriate messages using printf(). */


// https://www.geeksforgeeks.org/printf-in-c/
// https://www.w3resource.com/c-programming-exercises/basic-algo/c-programming-basic-algorithm-exercises-24.php



#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int main()
{

int nx = 0;
int ny = 0;
int nz = 0;

printf("Enter three integers: ");
scanf("%d %d %d", &nx, &ny, &nz);

printf("The integers you have submitted are %d, %d and %d\n", nx, ny, nz);

if (nx < ny && ny < nz) 
{
  printf("Your third input in the largest");

} else if (nx < ny && ny > nz)
{
    printf("Your second input in the largest");

} else if (nx > ny && ny > nz)
{
    printf("Your first number is the largest");
} else 
{
    printf("This is very bad error handling and excessive code\n");
}

}