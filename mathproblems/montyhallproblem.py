#https://www.101computing.net/the-monty-hall-problem/
# The Monty Hall Problem - Frequency Analysis - www.101computing.net/the-monty-hall-problem
import random

#Let's initialise our 3 doors
doors = ["goat", "goat", "car"]

# Randomly position the two goats and the car behind the three doors
random.shuffle(doors)

# Randomly pick a door and display the selected door number
# Get the computer to identify the two doors which have not been selected
#   If only one of these two doors contains a goat, display the door number to reveal the goat
#   If both doors contain a goat, pick one of the two doors randomly and display its number to reveal the goat
# Get the computer to randomly decide whether it will keep the selected door or switch to the other closed door
# Reveal the content of all three doors
# Check if the car was behind the selected door
# Keep count of wins and loses when the user decide to switch doors or not
# Display these counters/statistics
# Repeat the above process 100 times.
# If your code is working fine you should reach statistics to confirm that:
#     When switching doors your are twice as likely to win the car
#     When not switching doors your are twice as likely to get the goat!



