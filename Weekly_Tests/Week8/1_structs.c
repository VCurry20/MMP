/* Video on structs */


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>

/* struct is a data type - composit data type - made up of over data types */
/*  */

struct A {
    int val;
    double val2;
    int val3;
};

/* nested struct */
/* struct B is just a struct made of A inside B */
struct B {
    struct A aInsideB;
};

/* accessing the data in Struct A - a.val - is the first value in the struct */
/* sets the printing output */
void printA(struct A a){
    printf("this is a 'val' (%d), this is 'val2' %.2f, and this is a 'val3' %d\n", a.val, a.val2, a.val3);

}

int main(void)
{
    /* creating a new instance of the struct */
    struct A a ={10, 20.2, 4};
    /* first printout */
    /* PrintA is the method we made above its is not struct*/
    printA(a);
    /* here we are just submitting one instance - we do not need to send in all three */
    struct A a2 ={ 100 };
    /* second printout */
    printA (a2);

    /* passing in the value */
    struct B b ={a};
    /* print or access the info inside - struct B - ainsideb */
    /* third printout */
    /* output will be the same as the first print - cos we put a into b*/
    printA(b.aInsideB);

  
    /* forth printout */
    /* third value from A which is in B*/
    printf("this is a 'val' (%d) from A which is inside the B\n", b.aInsideB.val3);

    /* fifth printout */
    struct A a3 = b.aInsideB; 
    printf("this is a 'val' (%d) from A which is inside the B", a3.val);
};