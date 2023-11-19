/* MPP - Week 8 - C - Passing Arguments As Pointer */

/* if you want the data to change and stick out side of a method - use pointer */

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

struct Product {
    char* name;
    double price;
};

void passDirect(struct Product p)
{
    p.price = 1000.0;
    p.name = "Coke 330ml";
}

void passPointer(struct Product* p)
{
    p->price = 1000.0;
    p->name = "Coke 330ml";
}

int main()
{
    // these are two products
    struct Product a = {"Coke", 1.10};
    struct Product* b = &a;

    passDirect(a);
    printf("Price is now %.2f\n", a.price);
    passPointer(b);
    printf("Price is now %.2f\n", a.price);

}
