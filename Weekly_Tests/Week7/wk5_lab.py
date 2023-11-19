# Lab Wk5 Exercises
# video completed in wk7 to expand on topic
# starting code is the code from the wk 5 lecture


# self is in reference to the current class - whatever class you are working in 

class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.addresses = [address]




    def __repr__(self):
        return f"Person({self.name},{self.age})\nADDRESS:{self.addresses[0]}"
    

    def add_address(self, new_address):
        self.addresses.append(new_address)

    
    def get_all_addresses(self):
        return self.addresses
        
    

class Student(Person):

    def __init__(self, name, age, address):
        Person.__init__(self, name, age, address)
        #removing this as we have set up a college program class and will add via that class instead
        #self.college_course = college_course
        #connects student to the program
        # student can only have one program
        self.college_programme = None

    def __repr__(self):
        #return f"Student({self.name}, {self.age}, {self.college_course})"
        string = f"Student({self.name}, {self.age})"
        # if there is a program he is enrolled on print the info
        if (self.college_programme != None):
            string += f'{self.college_programme}'
        
        return string


    def home_address(self):
        return self.addresses[0]


    def college_address(self):
        if (len(self.addresses)==1):
            return self.home_address()
        else:
            return self.addresses[1]
        
    
    ## you could extent this call to add additional enrollment requirements


class CollegeProgramme:
    # answers Q4

    def __init__(self, name, level, university, limit=1):
        self.name = name
        self.level = level
        self.university = university
        # this limits number on the program
        self.limit = 1
        # this is a list of modules which we will connect to the module list / many modules below to a college program
        # this is a "has many" relationship - 1 progra mhas many modules
        self.modules = []
        # addling a "has many" list of students
        self.students = []

    # sets the print out format once print is called
    def __repr__(self) -> str:
        return f"CollegeProgramme({self.name}, {self.level}, {self.university})"
    
    # returns to the above modules list[]
    def add_module(self, new_module):
        self.modules.append(new_module)

    def get_modules(self):
        return self.get_modules
    
    # Answer Q5
    def is_module_on_program(self, search_term):
        for module in self.modules:
            if (module.name == search_term):
                return True
        return False



    # Answer 6
    def enroll_student(self, new_student):
        # answer 7 is the if / else statement here
        if ( new_student.age < 18):
            print("Cannot enroll People under 18 on this program")
        
        elif (len(self.students)== self.limit):
            print("The program is full") 
            
        else:    
            self.students.append(new_student)
            # linking to the college program variable under student - self here means the program as we are in program classs
            new_student.college_programme = self


class CollegeModule:
    # answers Q4

    def __init__(self, name, level, num_credits):
        self.name = name
        self.level = level
        self.num_credits = num_credits

    def __repr__(self):
        return f"CollegeModule({self.name}, {self.level}, {self.num_credits})"

class Address:

    def __init__(self, house_number, street, town, county, eircode, country="Ireland"):
            self.house_number = house_number
            self.street = street
            self.town = town
            self.county = county
            self.eircode = eircode
            self.country = country

        

    def __repr__(self):
        string = "\n"
        string += f"{self.house_number} {self.street},\n{self.town},\n{self.county},\n{self.eircode},\n{self.country}"
        return string
    

# test address and student address functionality

#address1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
#address2 = Address("4", "Othercourt", "Avondale", "Galway", "H35K6Z1")
#p1 = Person("John", 36, address1)
#p1 = Student("John", 36, address1)
# p1.add_address(address1)
#p1.add_address(address2)
#print(p1)
#print(len(p1.get_all_addresses()))
#print(p1.home_address())
#print(p1.college_address())


# test college program functionality
# answers Q4
# set a college program or think of it as a college course
#hdipda = CollegeProgramme ("Higher Diploma in Data Analytics", 8, "ATU")
#print(hdipda)

# answers Q5
# set college course modules - set up under college module and these are pulled in to college program
#module1 = CollegeModule("MPP", 8, 5)
#module2 = CollegeModule("Computational Thinking", 8, 5)
# add the modules
#hdipda.add_module(module1)
#hdipda.add_module(module2)

#print(hdipda.is_module_on_program("MPP"))
#print(hdipda.is_module_on_program("Into to Business"))


# answers q6
# enroll student functionality test
address1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
p1 = Student("John", 36, address1)

hdipda = CollegeProgramme ("Higher Diploma in Data Analytics", 8, "ATU")

module1 = CollegeModule("MPP", 8, 5)
module2 = CollegeModule("Computational Thinking", 8, 5)
hdipda.add_module(module1)
hdipda.add_module(module2)

#enroll student - no print out for this 
hdipda.enroll_student(p1)
print(p1)


# test 7
address1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
p2 = Student("Jake", 15, address1)
hdipda.enroll_student(p2)
print(p2)

p3 = Student("Bob", 22, address1)
hdipda.enroll_student(p3)