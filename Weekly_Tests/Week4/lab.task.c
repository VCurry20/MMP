#include <stdio.h>    /* https://www.tutorialspoint.com/c_standard_library/stdio_h.htm */
#include <string.h>   /* allows us to break down the CSV file - string tokeniser */
#include <stdlib.h>   /* https://www.tutorialspoint.com/c_standard_library/stdlib_h.htm */
#include <errno.h>    /* gives errors a code output? */


/* https://www.w3schools.com/c/c_structs.php */

struct Employee
{
    /* data */
    char* name;
    int age;
    double salary;
    int yearsWorked;
    char jobTitle;
};

struct Manager
{
    /* data */
    char* name;
    int age;
    double salary;
    struct Employee Employee[5];

};



struct Module
{
    /* data */
    char* name;
    int credits;

};


struct StudentModule
{
    /* data */
    struct Module modules;
    int quantity;
};


struct Student
{
    /* data */
    char* name;
    int age;
    //char* modules;
    struct Module modules[10];
    int index;
    
};


void printModule(struct Module m)
{
  printf("Module Name: %s\nModule Credits: %d\n", m.name, m.credits); 
  printf("--------------------\n"); 
}






int main (void)

{

    struct Student Ann ={ "Ann Joyce", 23, "English" };
    printf("Student name is %s\n", Ann.name);
    //printf("Student age is %d\n", Ann.age);
    //printf("Student modules are %s\n", Ann.modules);

    struct Student Jack ={ "Jack Murphy", 21, ("English", "Irish", "Science") };
    printf("Student name is %s\n", Jack.name);
    //printf("Student age is %d\n", Jack.age);
    //printf("Student modules are %s\n", Jack.modules);


    struct Module module={"English", 5};
    //printf("Module is %s and the credits are %d\n" , module.name, module.credits);
    printModule(module);

    struct Module module1={"Irish", 10};
    //printf("Module is %s and the credits are %d\n" , module1.name, module1.credits);
    printModule(module1);

    struct Module module2 ={"History", 10};
    printModule(module2);

    struct Student Student = {};
    Student.modules[0] = module;
    Student.modules[1] = module1;
    Student.modules[2] = module2;
    printModule(Student.modules[0]);
    

    return 0;
}
