# Modify the Person class, from the lecture notes, such that a person can have multiple addresses. 
# You can use a list for this purpose. 
# Add a method to the Person class to add a new address.

# https://stackoverflow.com/questions/59462102/taking-multiple-inputs-into-lists

class Person:

    def __init__(self, name, age, address= None):
        self.name = name
        self.age = age
        if address is None:
             self.address = []
        else:
             self.address = address

    def add_address(self, address):
         self.address.append(address)


    def __repr__(self):
        return f"Person({self.name},{self.age})\nADDRESS:{self.address}"
    

class Student(Person):

    def __init__(self, name, age, college_course, address):
        Person.__init__(self, name, age, address)
        self.college_course = college_course
        

    def find_address


    def __repr__(self):
        return f"Student({self.name}, {self.age}, {self.college_course}, {self.address})"




class Address:

    def __init__(self, house_number, street, town, county, eircode, country="Ireland"):
            self.house_number = house_number
            self.street = street
            self.town = town
            self.county = county
            self.eircode = eircode
            self.country = country
            #self.address.append(address)
        

    def __repr__(self):
        string = "\n"
        string += f"{self.house_number} {self.street},\n{self.town},\n{self.county},\n{self.eircode},\n{self.country}"
        return string
    



address1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
address2 = Address("43", "HouseHouse", "SomeArea", "Galway", "H61K7T4")
address3 = Address("67", "AnotherHours", "OtherArea", "Galway", "H47K2T3")

#address = [ address1, address2]


p1 = Person("John", 36, address1)
#print(p1)



p2 = Student("John", 36, "Computer Science", address2)
print(p2)
