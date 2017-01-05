#!/usr/bin/env python3
import random
from card import *


class Player:
    def __init__(self, name, deck):
        self.hand = []
        self.name = name
        self.deck = deck
        self.points = 0
        self.out = False

    def draw(self):
        self.hand.append(self.deck.draw())

    def play(self, card_index):
        card = self.hand[card_index]
        self.hand.remove(card)
        # execute card's actions

    def discard(self):
        if self.hand[0].value() == 8:
            self.out = True

        print('Discarded ' + self.hand[0])
        self.hand = []

        if not self.out:
            self.draw()


class Deck:
    def __init__(self):
        self.cards = []
        # Index is set to 1 to simulate "discarding" the top card
        self.index = 1

        for _ in range(5):
            self.cards.append(card(1))
        for _ in range(2):
            self.cards.append(card(2))
            self.cards.append(card(3))
            self.cards.append(card(4))
            self.cards.append(card(5))
        self.cards.append(card(6))
        self.cards.append(card(7))
        self.cards.append(card(8))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
        self.index = 1

    def empty(self):
        return self.index == len(self.cards)

    def draw(self):
        # TODO: Trigger end of game rules when deck is empty
        if not self.empty():
            drawn = self.cards[self.index]
            self.index += 1
            return drawn

if __name__ == '__main__':
    deck = Deck()

    players = [
        Player('One', deck),
        Player('Two', deck)
    ]

    for p in players:
        p.draw()

    # Game loop

    players[0].draw()

    for p in players:
        print('{}: {}'.format(p.name, p.hand))
