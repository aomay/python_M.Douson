#Блек-Джек
#изучаю ООП повторно

import games, cards

class BJ_card(cards.Card):
    ACE_VALUE = 1
    @property
    def value(self):
        if self.is_face_up:
            v = BJ_card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_deck(cards.Deck):
    def populate(self):
        for suit in BJ_card.SUITS:
            for rank in BJ_card.RANKS:
                self.cards.append(BJ_card(rank, suit))

class BJ_hand(cards.Hand):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def __str__(self):
        rep = self.name + '\t' + super().__str__()
        if self.total:
            rep += str(self.total)
        return rep
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_card.ACE_VALUE:
                contains_ace = True
        if contains_ace and t <= 11:
            t += 10
        return t
    def is_busted(self):
        return self.total > 21

class BJ_player(BJ_hand):
    def is_hitting(self):
        resp = games.ask_y_n(self.name + '\tбудете брать еще карту?(y/n): ')
        return resp == 'y'
    def bust(self):
        print(self.name, ' перебрал')
        self.lose()
    def lose(self):
        print(self.name, ' проиграл')
    def win(self):
        print(self.name, ' выиграл')
    def push(self):
        print(self.name, ' сыграл с компьютером вничью')

class BJ_dealer(BJ_hand):
    def is_hitting(self):
        return self.total < 17
    def bust(self):
        print(self.name, ' перебрал')
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_game(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_player(name)
            self.players.append(player)
        self.dealer = BJ_dealer('Диллер')
        self.deck = BJ_deck()
        self.deck.populate()
        self.deck.shuffle()
    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp
    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()
        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print('добро пожаловать за игровой стол!')
    names = []
    num = games.ask_num('сколько всего игроков?(1-7): ', min = 1, max = 7)
    for i in range(num):
        name = input('введите имя игрока: ')
        names.append(name)
        print()
    game = BJ_game(names)
    again = None
    while again != 'n':
        game.play()
        again = games.ask_y_n('хотите сыграть еще?(y/n): ')

main()
