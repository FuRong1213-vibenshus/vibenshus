# 2018 Football World Cup Challenge -  www.101computing.net/2018-world-cup-goals-analysis/
import time
import numpy as np
import pandas as pd


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


data = pd.read_csv("goals.txt", delimiter=";", header=None, usecols=[
                   0, 1, 2], names=['player', 'country', 'time'])
data2 = pd.DataFrame(data)


def totalGoalsCountry(name):
    return data2[data2['country'].str.contains(name)].__len__()


def timesScored(name):
    return data2['player'].value_counts()[name]


def playersScoredCountry(name):
    return data2[data2["country"].str.contains(name)].drop_duplicates(['player'])['player'].values


def goalsScoredTotal():
    return data2.__len__()


def numgoals45min():
    return data2[data2['time'] <= 45].__len__()


def numgoals45to90():
    return data2[(data2['time'] > 45) & (data2['time'] <= 90)].__len__()


def extratime():
    return data2[(data2['time'] > 90)].__len__()


def allplayers():
    return data2.drop_duplicates(['player'])['player'].sort_values().values


def allCountries():
    return data2.drop_duplicates(['country'])['country'].sort_values().values


##################### Main Program Starts Here ##############################
userChoice = ""

while userChoice != "X":
    menu()
    userChoice = input(
        "> Select an option from the menu (A to G) or X to exit:").upper()
    if userChoice == "A":
        print(totalGoalsCountry(input("Country name: ")))
    elif userChoice == "B":
        print(timesScored(input("Player name: ")))
    elif userChoice == "C":
        print(playersScoredCountry(input("Country name: ")))
    elif userChoice == "D":
        print(goalsScoredTotal())
    elif userChoice == "E":
        print(numgoals45min())
    elif userChoice == "F":
        print(numgoals45to90())
    elif userChoice == "G":
        print(extratime())
    elif userChoice == "H":
        print(allplayers())
    elif userChoice == "I":
        print(allCountries())
    time.sleep(3)
    print("\n\n\n")
print("Good bye!")