/* Doing Questions from Wk1 in C code as opposed to Python */
/* Modify the previous program such that only the users Alice and Bob are greeted with their names. */

#include <stdio.h>

#include <string.h>

int main (void){

    char name[20];

    printf("What is your name?\n");


/* fgets input  */ 
    fgets(name, 20, stdin);

/* strips down spaces - removes the enter when we add it to submit name, and \0 terminates at the end of our input */
/* 20 characters only accept name and new line */
    name[strcspn(name,"\n")] ='\0';

/* strcmp here is another function in c -  */
/* || means or  */

    if ((strcmp(name, "Alice") ==0 ) || (strcmp(name, "Bob") ==0 ))

    {
        printf("Hello %s!\n", name);
    }
    else
    {
        printf("Hello Peasant!\n");
    }



}
