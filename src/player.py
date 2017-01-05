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
