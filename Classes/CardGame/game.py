from card import *
from deck import *

class Game:
  def __init__(self):
    pass
  
  def game_setup(self):
    pass
  
  def main(self):
    pass
  

#Main Program Starts here...    
deckOfCards = Deck()
deckOfCards.shuffle()
scorePlayer1 = 0
scorePlayer2 = 0
roundNumber = 1
print(deckOfCards)
while not deckOfCards.isEmpty():
  print("\n--- Round " + str(roundNumber) + " ---")
  roundNumber += 1
  card1 = deckOfCards.deal()
  card2 = deckOfCards.deal()
  print("    Card 1: " + card1.__str__())
  print("    Card 2: " + card2.__str__())
  if card1.rank>card2.rank:
    print("     Card 1 wins!")
    scorePlayer1 += 1
  elif card1.rank<card2.rank:
    print("     Card 2 wins!")
    scorePlayer2 += 1  
  else:
    print("     It's a draw!")

print("\n--- Game Over! ---")
print("Score Player 1:" + str(scorePlayer1))
print("Score Player 2:" + str(scorePlayer2))
if scorePlayer1>scorePlayer2:
  print("Player 1 wins!")
elif scorePlayer1<scorePlayer2:
  print("Player 2 wins!")
else:
  print("It's a draw!")
