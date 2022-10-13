from Map import Map

class MyAdventureGame:
    def __init__(self):
        self.map = Map()
        pass

    def run(self):
        while True:
            print("Welcome to the Adventure Game!")
            print("As an avid traveller, you have decided to visit the Catacombs of Paris.")
            print("However, during your exploration, you find yourself lost.")
            print("You can choose to walk in multiple directions to find a way out.")
            print("Let's start with your name: ")
            name = input()
            print("Good luck, " +name+ ".")
            self.map.current_scene.run()
        

if __name__ == "main":
    mygame = MyAdventureGame()
    mygame.run()