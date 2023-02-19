from card import *
import random

class Pile:

    def __init__(self) -> None:
        self.cards = []

    def len(self) -> int:
        return len(self.cards)

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card: Card) -> None:
        self.cards.remove(card)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop(0)
    def isEmpty(self)-> bool:
        return len(self.cards) == 0
    def __str__(self) -> str:
        return ', '.join(str(card) for card in self.cards)