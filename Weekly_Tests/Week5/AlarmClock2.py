## This alarm combines clock and alarm clock
# polymorphism - both clocks running together
# the subclass doesnt effect the running of the superclass


# import the clock from the clock program - import everything
from Clock import *

# clock is the super class
# Alarm is the sub class - alarm clock extents from clock 
class AlarmClock(clock):


    # set "alarm time"
    def __init__(self, hours, mins, secs, aHour, aMin, aSec):
        super().__init__(hours, mins, secs)
        self.aHour =aHour
        self.aMin = aMin
        self.aSec = aSec

    # pull in tick class from clock.py / super class- and we add to it, add in another check
    # add to the super class and extends it
    # if clock time equals alarm time


    def tick(self):
        if(self.hours == self.aHour and self.mins == self.aMin and self.secs == self.aSec):
            print("ALARM, get up!!!!")
        
        super().tick() # moved in this version



    # FORMATS FOR A NEW OUTPUT  - - this overwrites the one imported from clock
    def __repr__(self):
        return f"Alarm Clock: {super().__repr__()}"

# this part ensure we are only running what is in this file = we are not running the clock from the clock.py file
# it is only importing the script and not running
if __name__=="__main__":

    c = AlarmClock( 10, 20, 50, 10, 20 , 55)
    c2 = clock(11, 55, 10)

    arr =[c, c2]



    while (True):
        for clock in arr:
            print(clock)
            clock.tick()
            #print(c)
            time.sleep(1)

