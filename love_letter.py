#!/usr/bin/python
import random

class Card:
    def __init__(self, value):
        self.value = value

        self.description = {
                1: {'name': 'Batman', 'rules': "Guess a player's hand"},
                2: {'name': 'Catwoman', 'rules': 'Look at a hand'},
                3: {'name': 'Bane', 'rules': 'Compare hands; lower hand is out'},
                4: {'name': 'Robin', 'rules': 'Protection until next turn'},
                5: {'name': 'Poison Ivy', 'rules': 'One player discards their hand'},
                6: {'name': 'Two-Face', 'rules': 'Trade hands'},
                7: {'name': 'Harley Quinn', 'rules': 'Discard if caught with TWO-FACE or POISON IVY'},
                8: {'name': 'Joker', 'rules': 'Lose if discarded'}
        }

    def rules(self):
        return self.description[self.value]['rules']

    def name(self):
        return self.description[self.value]['name']

    def __repr__(self):
        return str((self.name(), self.value))

class Deck:
    def __init__(self):
        self.cards = []
        self.index = 1

        for i in xrange(5):
            self.cards.append(Card(1))
        for i in xrange(2):
            self.cards.append(Card(2))
            self.cards.append(Card(3))
            self.cards.append(Card(4))
            self.cards.append(Card(5))
        self.cards.append(Card(6))
        self.cards.append(Card(7))
        self.cards.append(Card(8))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
        self.index = 1

    def draw(self):
        if self.index == len(self.cards):
            return None

        drawn = self.cards[self.index]
        self.index += 1
        return drawn

if __name__ == '__main__':
    deck = Deck()

    card = deck.draw()
    print card
    print card.rules()

