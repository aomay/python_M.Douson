class Card(object):
    RANKS = ['A', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['c', 'd', 'h', 's']
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            rep = '<пусто>'
        return rep
    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    def populate(self):
        self.cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.add(Card(rank, suit))
    def shufffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('карты кончились')

class Unprintable_cards(Card):
    def __str__(self):
        print('<нельзя напечатать>')

class Positionable_card(Card):
    def __init__(self, rank, suit, face_up = True):
        super().__init__(rank, suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = 'XX'
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up

card1 = Positionable_card('A', 's')
print(card1)
card1.flip()
print(card1)
