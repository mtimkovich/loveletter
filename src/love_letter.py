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
        self.is_immune = False

    def status(self, *msg):
        print(self.name, *msg)

    def draw(self):
        self.status('draws a card')
        self.hand.append(self.deck.draw())

    def todo(self, a):
        print('TODO:', a, 'not defined')

    def nop(self):
        pass

    def lose(self):
        self.status('is out of this round')
        self.out = True

    def immune(self):
        self.status('is immune until next turn')
        self.is_immune = True

    def play(self, card_index):
        card = self.hand[card_index]
        self.hand.remove(card)

        self.status('played', card.name)

        # execute card's actions
        getattr(self, card.action, lambda: self.todo(card.action))()
        print()

    # def discard(self):
    #     self.status('discarded', self.hand[0].name)

    #     if self.hand[0].value == 8:
    #         self.lose()

    #     self.hand = []

    #     if not self.out:
    #         self.draw()


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

if __name__ == '__main__':
    deck = Deck()

    players = [
        Player('One', deck),
        Player('Two', deck)
    ]

    for p in players:
        p.draw()
    print()

    # Game loop
    done = False
    players_out = 0
    while not deck.empty() and not done:
        for i, p in enumerate(players):
            # Check if p is the last player alive
            if players_out == len(players)-1:
                print('Player', p.name, 'wins')
                done = True
                break

            p.is_immune = False

            p.draw()
            p.play(0)

            if p.out:
                players_out += 1
