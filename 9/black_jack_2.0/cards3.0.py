class Card(object):
    '''одна карта'''
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['c', 'd', 'h', 's']
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit
    def __str__(self):
        rep = self.__rank + self.__suit
        return rep

class Hand(object):
    '''рука одного игрока'''
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
    def give(self, other_hand, card):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(hand, top_card)
                else:
                    print('в колоде кончились карты!!!')

class Unprintable_card(Card):
    def __str__(self):
        rep = '<нельзя напечатать>'
        return rep

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

def main():
        card1 = Card(rank = 'A', suit = 'h')
        card2 = Unprintable_card(rank = 'A', suit = 'q')
        card3 = Positionable_card(rank = 'A', suit = 'c')

        print('печатаю CARD')
        print(card1)
        print('печатаю Unprintable_card')
        print(card2)
        print('печатаю Positionable_card')
        print(card3)
        print('переворачиваю')
        card3.flip()
        print('еще раз печатаю Positionable_card')
        print(card3)
        print('переворачиваю')
        card3.flip()
        print('еще раз печатаю Positionable_card')
        print(card3)


main()
