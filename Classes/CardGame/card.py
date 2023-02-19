import random
from enum import Enum

SUITS = (chr(9825 ), chr(9824 ), chr( 9827 ), chr(9826)) 
RANKS = {"Ace":11,"King":10,"Queen":10,"Jack":10,"10":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}


class Card():
    #rank: int
    #suit: SUITS
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
    def __str__(self) -> str:
        return f'{self.rank}{self.suit}'