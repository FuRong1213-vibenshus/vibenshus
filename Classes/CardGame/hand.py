from pile import *

class Hand(Pile):
    
    def __init__(self, name: str) -> None:
        self.cards = []
        self.label = name

    def getHandValue(self):
        """Returns the value of the cards. Face cards are worth 10, aces are
        worth 11 or 1 (this function picks the most suitable ace value)."""
        value = 0
        numberOfAces = 0

        # Add the value for the non-ace cards:
        for card in self.cards:
            if card.rank == 'Ace':
                numberOfAces += 1
            else:
                value += card.value  # Numbered cards are worth their number.

        # Add the value for the aces:
        value += numberOfAces  # Add 1 per ace.
        for i in range(numberOfAces):
            # If another 10 can be added without busting, do so:
            if value + 10 <= 21:
                value += 10

        return value
    