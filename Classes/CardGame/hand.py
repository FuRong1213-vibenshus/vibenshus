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

        ## TBD

        return value
    