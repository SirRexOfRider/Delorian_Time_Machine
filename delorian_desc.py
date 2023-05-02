"""
Name:delorian_desc.py
Author:Rex
Date:5/2/23
Purpose:Set attributes of delorian and methods
"""
#Import tts from a differnt program
import pyttsx3
class TextToSpeech():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.rate = 200
        self.volume = 0.9
        self.voice = 0
    #Set properties before you add items to say
        self.engine.setProperty("rate", self.rate)
        self.engine.setProperty("volume", self.volume)
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[self.voice].id)


#Make class (Delorian)
class Delorian:
    #Set year,data,passanger,and speed
    def __init__(self):
        self._year = 2015
        self._date = "Oct 21"
        self._passanger="mad scientist"
        self._speed = 0
    #User chooses whether or not to accelerate,brake,honk, or stall
    def choice(self):
        choice = input("[A]ccelerate | [B]rake | [H]onk | [S]tall" ).lower()
        return choice
            
    #Determines what user chose
    def make_choice(self, choice):
        if choice == "a":
            self._speed += 30
            print("You accelerated")
        elif choice == "b":
            if self._speed >=20:
                self._speed -=20
            elif self._speed == 0:
                print("You aren't moving! Why would you brake?!?")
            else:
                print("You're going too slow already! Speed up!")
            print("Why would you brake!?!")
        elif choice == "x":
            print("You decided to not do anything.")
            pass
        elif choice == "h":
            self.honk()
   
    #Honk method
    def honk(self):
        tts=TextToSpeech()
        tts.engine.say("Honk")
        #Flush the say() que and play the audio
        tts.engine.runAndWait()



    #Time travel check
    def time_travel(self):
        if self._speed >= 88:
            print("Success! You arrived in the future!")
        else:
            print("The car wasn't going fast enough and ends up running into a side of a building.")

    

    #Used to get speed of car
    def get_speed(self):
        return self._speed

    #Used to get year we're traveling to
    def get_year(self):
        return self._year
    
    #Used to get data we're traveling to
    def get_date(self):
        return self._date
    
    #Used to describe your passanger
    def get_passanger(self):
        return self._passanger

    