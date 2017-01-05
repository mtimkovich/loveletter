#!/usr/bin/env python3
import random
from card import get_card


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

        if card.action == 'lose':
            self.out = True
        print(card)

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
    done = False
    while not deck.empty() and not done:
        for i, p in enumerate(players):
            if all(x.out for x in (players[:i] + players[i+1:])):
                print('Player {} wins'.format(p.name))
                done = True
                break

            print(p.name)
            p.draw()

            p.play(0)
