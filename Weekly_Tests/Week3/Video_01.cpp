/* Doing Questions from Wk1 in C code as opposed to Python */
/* Write a program that asks the user for their name and greets them with their name */

#include <stdio.h>

int main (void){

    char name[20];

    printf("What is your name?\n");

    fgets(name, 20, stdin);


    printf("Hello, %s", name);


}