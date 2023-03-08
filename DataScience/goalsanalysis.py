#2018 Football World Cup Challenge -  www.101computing.net/2018-world-cup-goals-analysis/
import time

def menu():
  print("*********************************************")
  print("*                                           *")
  print("*      2018 World Cup: Goals Analysis       *")
  print("*                                           *")
  print("*********************************************")
  print("")
  print("> Select an option:")
  print("       > A: Total number of goals scored by a given country")
  print("       > B: Total number of goals scored by a given player")
  print("       > C: List the name of all the players who scored for a given country")
  print("       > D: Total number of goals by all countries")
  print("       > E: Total number of goals scored during the first half (45 minutes)")
  print("       > F: Total number of goals scored during the second half (45 minutes to 90 minutes)")
  print("       > G: Total number of goals scored during extra time (after 90 minutes of play)")
  print("       > X: Exit")
  print("")
  
#A Procedure to count the number of goals scored by a given country during the 2018 world cup
def goalsPerCountry():
  userInput = input("> Enter country:").title()
  
  file = open("goals.txt","r")
  goals = 0
  for line in file:
    data = line.split(";")
    player = data[0]
    country = data[1]
    minutes = int(data[2])
    if country == userInput:
       goals = goals + 1
  file.close()
  print("\n> " + userInput + " scored " + str(goals) + " goal(s) in the 2018 world cup.")


##################### Main Program Starts Here ##############################
userChoice=""
while userChoice!="X":
  menu()
  userChoice = input("> Select an option from the menu (A to G) or X to exit:").upper()
  if userChoice=="A":
    goalsPerCountry()
  elif userChoice=="B":
    print("To be completed...")
  #...
  time.sleep(3)
  print("\n\n\n")
print("Good bye!")    