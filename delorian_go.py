"""
Name:delorain_go.py
Author:Rex
Date:5/2/23
Purpose:Vrmm Vrmmmm
"""
#Import files needed
import delorian_desc
import utils
from time import sleep


#TODO:Import files needed
#TODO:Create class Delorian and set attributes (year,data,passanger,speed)
#TODO:Create choice system to determine what user chooses to do
#TODO:Create methods for all choices
#TODO:(Extra) Import tts and have car honk at user
#TODO:Test if user is going fast enough to time travel at the end of the 4 choices

#Define main
def main():
    #Make object
    delorian = delorian_desc.Delorian()

    #Print title
    print(utils.title("Marty's Drivable Time Machine"))

    #Prompt user about what's going on
    name = input("What's your name?")
    sleep(1)
    print(f"{name}, we're trying to get to the year: {delorian.get_year()}")
    sleep(1.5)
    print(f"We're traveling to the date: {delorian.get_date()}")
    sleep(1.5)
    print(f"Your passanger is a {delorian.get_passanger()}")
    sleep(1.5)
    print(f"We need to hit atleast 88 mph to get enough speed to time travel!")
    sleep(1.5)
    
    #Set up loop
    x=0
    while x < 4:
        #Ask user whether they want to accelerate, brake, honk, or stall
        print('')
        delorian.make_choice(delorian.choice())
        print(f"The delorian is going {delorian.get_speed()} mph.")
        x +=1

    #Test if user is going fast enough
    delorian.time_travel()
    

#If alone, else module
if __name__ =="__main__":
    main()
