/* Video 3 was error handing in extension of video 2*/

/* Clock in C */

#include <stdio.h>
#include <windows.h>
#include <errno.h>



/* Clock in C */
/* This uses a procedural approach - C does not have OOP */
/* This algorithm is the same as the python version */
/*  */


/* clock struct */
struct Clock {
    int hours;
    int mins;
    int secs;
};

void tick(struct Clock *c)
{
    c->secs += 1;

    if (c ->secs >59)
    {
        c->mins += 1;
        c->secs =0;
    }

    if (c ->mins >59)
    {
        c->hours += 1;
        c->mins =0;
    }

    if (c ->hours >12)
    {
        c->hours = 1;
        c->mins =0;
        c->secs =0;
    }
}

/* need to pass in the struct - explicitly pass it in */
void printClock(struct Clock c)
{
    printf("\n Clock");
    printf("\n%02d:%02d:%02d", c.hours, c.mins, c.secs);

}

/* need to pass in the struct - explicitly pass it in */
void validate (struct Clock*c)
{
    if (c->hours >12 || c->mins >60 || c->secs >60)
    {
        c-> hours=0;
        c-> mins=0;
        c-> secs=0;
    }
}

/* Differences */
/* here the data is in the structs and the methods are outside - seperate */
/* In Object orientated approach - they would be together in the class */


/* New struct created and then validated within the main call */
int main()
{
    struct Clock c ={10, 12, 23};
    validate(&c);

    /*While true*/
    while(1)
    {
        tick(&c);
        printClock(c);
        /*1000 miliseconds*/
        Sleep(1000);
    }

    return 0;
}
