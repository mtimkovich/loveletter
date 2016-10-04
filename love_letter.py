#!/usr/bin/python
import random

class Card:
    def __init__(self, value):
        self.value = value

        ''' 
        TODO: Possibly make a grammar to describe card actions
        actions:
            target
            look at hand
            get player input (either player or player and card)
            compare hands
            make player lose
            immunity 
            discard hand
            trade hands
        '''
        self.description = {
                1: {
                    'name': 'Batman', 
                    'rules': "Guess a player's hand",
                    'target': 'other'
                   },
                2: {
                    'name': 'Catwoman', 
                    'rules': 'Look at a hand',
                    'target': 'other'
                   },
                3: {
                    'name': 'Bane',
                    'rules': 'Compare hands; lower hand is out',
                    'target': 'other'
                   },
                4: {
                    'name': 'Robin',
                    'rules': 'Protection until next turn',
                    'target': 'self'
                   },
                5: {
                    'name': 'Poison Ivy',
                    'rules': 'One player discards their hand',
                    'target': 'any'
                   },
                6: {
                    'name': 'Two-Face',
                    'rules': 'Trade hands',
                    'target': 'other'
                   },
                7: {
                    'name': 'Harley Quinn',
                    'rules': 'Discard if caught with TWO-FACE or POISON IVY',
                    'target': 'self'
                   },
                8: {
                    'name': 'Joker',
                    'rules': 'Lose if discarded',
                    'target': 'self'
                   }
        }

    def rules(self):
        return self.description[self.value]['rules']

    def name(self):
        return self.description[self.value]['name']

    def __repr__(self):
        return str((self.name(), self.value))

class Player:
    def __init__(self, name, deck):
        self.hand = []
        self.name = name
        self.deck = deck
        self.points = 0

    def draw_hand(self):
        for _ in xrange(2):
            self.draw(self.deck)

    def draw(self):
        self.hand.append(self.deck.draw())

    def play(self, card_index):
        card = self.hand[card_index]
        self.hand.remove(card)
        # execute card's actions

    def discard(self):
        # TODO: Print cards that were discarded
        self.hand = []
        self.draw_hand()

class Deck:
    def __init__(self):
        self.cards = []
        # Index is set to 1 to simulate "discarding" the top card
        self.index = 1

        for _ in xrange(5):
            self.cards.append(Card(1))
        for _ in xrange(2):
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

    card = deck.draw()
    print card
    print card.rules()

