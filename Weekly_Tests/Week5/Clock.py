# make a clock in python

# validate ot tick method in this class 
# validate - check submitted time to see if it is correct - checks encapsulation - data entered is valid

# clock 1 and Clock 2 operate seperately but can use the data code

import time


# class is clock - here we can add data
class clock:
    # double underline method - constructor in this case
    # self means ours or us
    # self is passed into every method

    def __init__(self, hours, mins, secs):
        self.hours= hours
        self.mins= mins
        self.secs= secs
        self.validate()
        # validate function will validate and set to zero if any of the rules are broken
    

    def validate(self):
        if (self.hours > 12 or self.mins > 60 or self.secs > 60):
            self.hours = 0
            self.mins =0
            self.secs =0

    
    def tick(self):

        self.secs += 1

        if (self.secs > 59):
            self.mins += 1
            self.secs =0

        if (self.mins > 59):
            self.hours += 1
            self.mins =0

        if (self.hours > 12):
            self.hours =1
            self.mins =0
            self.secs =0


    # return string representation of a class
    # this is us defininig what output we want - how we want it to look
    # without this it will just give a predetermined one as per the class
    def __repr__(self):
        return f"{self.hours}:{self.mins}:{self.secs}"

if __name__=="__main__":
    c= clock(10, 20, 50)
    c2 = clock(11, 23, 55)

    # infinite loop - it will keep ticking
    # time function will ensure it only ticks once every second - this is a library function
    while(True):
        c.tick()
        c2.tick()
        print(F"Clock1 {c}")
        print(f"Clock2 {c2}")
        time.sleep(1)





