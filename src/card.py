class Card:
    def __repr__(self):
        return str((self.name, self.rules, self.value))


class Batman(Card):
    def __init__(self):
        self.name = 'Batman'
        self.value = 1
        self.rules = "Guess a player's hand"
        self.action = 'guess'


class Catwoman(Card):
    def __init__(self):
        self.name = 'Catwoman'
        self.value = 2
        self.rules = 'Look at a hand'
        self.action = 'look'


class Bane(Card):
    def __init__(self):
        self.name = 'Bane'
        self.value = 3
        self.rules = 'Compare hands; lower hand is out'
        self.action = 'compare'


class Robin(Card):
    def __init__(self):
        self.name = 'Robin'
        self.value = 4
        self.rules = 'Protection until next turn'
        self.action = 'immune'


class PoisonIvy(Card):
    def __init__(self):
        self.name = 'Poison Ivy'
        self.value = 5
        self.rules = 'One player discards their hand'
        self.action = 'discard'


class TwoFace(Card):
    def __init__(self):
        self.name = 'Two-Face'
        self.value = 6
        self.rules = 'Trade hands'
        self.action = 'trade'


class HarleyQuinn(Card):
    def __init__(self):
        self.name = 'Harley Quinn'
        self.value = 7
        self.rules = 'Discard if caught with TWO-FACE or POISON IVY'


class Joker(Card):
    def __init__(self):
        self.name = 'Joker'
        self.value = 8
        self.rules = 'Lose if discarded'
        self.action = 'lose'


def get_card(v):
    return {
        1: Batman,
        2: Catwoman,
        3: Bane,
        4: Robin,
        5: PoisonIvy,
        6: TwoFace,
        7: HarleyQuinn,
        8: Joker
    }[v]()
