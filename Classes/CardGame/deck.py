from card import *
from pile import *


class Deck(Pile):
    def __init__(self) -> None:
        self.cards = [
            Card(rank, suit, RANKS[rank])
            for rank in RANKS
            for suit in SUITS
            #for value in RANKS.values()
        ]
        self.shuffle()