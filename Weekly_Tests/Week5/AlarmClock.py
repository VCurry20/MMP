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
        super().tick() ## you can also move this to the bottom of this paragraph of code - so print happens first
        if(self.hours == self.aHour and self.min == self.aMin and self.secs == self.aSec):
            print("ALARM, get up!!!!")


    
# this part ensure we are only running what is in this file = we are not running the clock from the clock.py file
# it is only importing the script and not running
if __name__=="__main__":

    c = AlarmClock( 10, 20, 50, 10, 20 , 55)


    while (True):
        c.tick()
        print(c)
        time.sleep(1)

# you can move the print in line 35 or 22 so that the alarm goes off before the time as such
