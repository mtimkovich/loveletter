#!/usr/bin/env python3
from deck import Deck
from player import Player

if __name__ == '__main__':
    deck = Deck()

    players = [
        Player('One', deck),
        Player('Two', deck)
    ]

    for i, p in enumerate(players):
        p.players = players
        p.index = i
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
