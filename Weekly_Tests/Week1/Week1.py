# Week 1 Questions


import math


# Write a program that asks a user their name and greets them
# https://www.tutorialspoint.com/how-do-i-input-a-string-from-the-user-in-python#:~:text=The%20most%20common%20method%20is,for%20use%20in%20the%20program.&text=%23%20Define%20a%20variable%20to%20store,Good%20to%20see%20you.%22)

name = input("Please enter your name: ")

print("Your Name is",name ,", nice to meet You.")


# modify the above code such that only users Alice and Bob are greeted with their names.
# https://stackoverflow.com/questions/28972790/how-to-loop-conditional-statements-based-on-specific-user-input-in-python

greeting = input("Please enter your name: ") # Get input

while greeting not in ['Alice', 'Bob']:      # Check to see if the name is Alice or Bob
    greeting = input("Hey, You!")
    break
else: #If it is Alice or Bob, proceed
    if greeting == "Alice":
        print("Hey Alice, great to see You")

    elif greeting == "Bob":
        print("Hey Bob, long time")


# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
# https://stackoverflow.com/questions/43901484/sum-of-the-integers-from-1-to-n
# https://stackoverflow.com/questions/50971279/prints-the-sum-of-the-numbers-1-to-n-in-python

output = ""
num = int(input("enter a integer: "))


if num == 0:
    print("Number must be above 0")
    print("Please try again")
        

for i in range(1, num+1):
    output += "{}".format(i)
    if i != num:
        output += "+"
output += " = {}".format(sum(range(num+1)))   
print (output)



# Simplier version

#n = int(input("Please choose a number? "))
#def sum_num (n):
#    return sum( range (n+1))

#total = sum_num(n)
#print ( "The sum of all numbers up to your choosen number is: ", total)





# Modify the previous program such that only multiples of 3 or 5 are considered in the sum
# https://stackoverflow.com/questions/5930300/how-to-find-the-sum-of-all-the-multiples-of-3-or-5-below-1000-in-python


output = ""
num = int(input("enter a integer: "))


if num == 0:
    print("Number must be above 0")
    print("Please try again")
        

for i in range(1, num+1):
    if (i % 3 == 0 or i % 5 == 0):
        output += "{}".format(i)
        if i != num:
            output += "+"
output += " = {}".format(sum(range(num+1)))   
print (output)



# Write a prrogram that asks the user for a number (n) and the choose between sum and product of (n)
# https://stackoverflow.com/questions/7361078/product-of-first-n-terms-in-a-sequence-in-python
# https://www.quora.com/How-can-we-write-a-program-that-asks-the-user-for-a-number-n-and-gives-them-the-possibility-to-choose-between-computing-the-sum-and-computing-the-product-of-1-n
# https://stackoverflow.com/questions/50971279/prints-the-sum-of-the-numbers-1-to-n-in-python


def sum(n): 
	sumN = (n*(n+1))/2 
	return sumN 

#print (sum(4))
# 10

def factorial(n):
    return math.factorial(n)

#print (factorial(4))
# 24


n = int(input("Enter a number: "))
choice = int(input("Enter 1 for sum until n or Enter 2 for product until n "))

if(choice==1): 
	print(sum(n)) 
elif(choice==2): 
	print(factorial(n))
     



# Program that prints a multiplication table for numbers up to 12
# https://www.programiz.com/python-programming/examples/multiplication-table

num = int(input("Enter a number: "))

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 13):
   print(num, 'x', i, '=', num*i)



# A program that prints all the prime numbers smaller than 100
# https://allinpython.com/print-prime-numbers-from-1-to100-in-python/

 # range function is not count last number (Ending number)
 # only 1 to 100 is counted
 
for i in range(2,101): 
    for j in range(2,101):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")


# end