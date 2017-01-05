import random

from card import get_card


class Deck:
    def __init__(self):
        self.cards = []

        for _ in range(5):
            self.cards.append(get_card(1))
        for _ in range(2):
            self.cards.append(get_card(2))
            self.cards.append(get_card(3))
            self.cards.append(get_card(4))
            self.cards.append(get_card(5))
        self.cards.append(get_card(6))
        self.cards.append(get_card(7))
        self.cards.append(get_card(8))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
        # Index is set to 1 to simulate "discarding" the top card
        self.index = 1

    def empty(self):
        return self.index == len(self.cards)

    def draw(self):
        # TODO: Trigger end of game rules when deck is empty
        if not self.empty():
            drawn = self.cards[self.index]
            self.index += 1
            return drawn
