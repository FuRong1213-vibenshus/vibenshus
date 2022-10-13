from hashlib import new
from Room import Room
from dataclasses import dataclass

class HauntedRoom(Room):
    def __init__(self, description, name):
       super().__init__(description, name)
    def run():
        directions = ["right","left","backward"]
        print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
        userInput = ""
        while userInput not in directions:
            print("Options: right/left/backward")
            userInput = input()
            if userInput == "right":
                print("Multiple goul-like creatures start emerging as you enter the room. You are killed.")
                quit()
            elif userInput == "left":
                print("You made it! You've found an exit.")
                quit()
            elif userInput == "backward":
                introScene()
            else:
                print("Please enter a valid option.")
    

class MainEntrance(Room):
    def __init__(self, description, name):
       super().__init__(description, name)


class Map:
    def __init__(self):
        self.room_dic = {}
        main_entrance = MainEntrance("This is the main entrance to the game", \
                             "Main Entrance")
        self.room_dic["main"] =  main_entrance
        self.room_dic["hauntedroom"] = HauntedRoom("This is the HauntedRoom to the game", \
                             "HauntedRoom")
        self.current_scene = main_entrance
        
    def add_room(self, newroom):
        self.room_dic[newroom.name] = newroom
    
    