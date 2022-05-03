#war или пьяница
#продолжаем изучать ООП

import games, cards

class W_Card(cards.Card):
    @property
    def value(self):
        if self.is_face_up:
            v = W_Card.RANKS.index(self.rank) + 6
        else:
            v = None
        return v

class W_Deck(cards.Deck):
    def populate(self):
        for suit in W_Card.SUITS:
            for rank in W_Card.RANKS:
                self.cards.append(W_Card(rank, suit))
    def __str__(self):
        rep = ''
        for i in range(len(self.cards)):
            rep += str(self.cards[i]) + '\t'
        return rep
class W_Player(cards.Hand):
        def __init__(self, name, score = 0):
            super().__init__()
            self.name = name
            self.score = score
        def win(self):
            print('\nигрок ', self.name, ' получает 1 поинт')
            self.score += 1

class W_Game(object):
    def __init__(self, names):
        self.deck = W_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.players = []
        for name in names:
            player = W_Player(name)
            self.players.append(player)
    def play(self):
        while len(self.deck.cards) >= len(self.players):
            input('\n\nсдаю карту\n')
            self.deck.deal(self.players, per_hand = 1)
            self.values = []
            for player in self.players:
                print('игрок: ', player.name, '\tкарта: ', player.cards[-1], '\tноминал: ', player.cards[-1].value)
            for player in self.players:
                self.values.append(player.cards[-1].value)
            for player in self.players:
                if player.cards[-1].value == max(self.values):
                    player.win()
        else:
            print('\t!!!конец игры!!!\n\tИГРОК\tСЧЁТ')
            for player in self.players:
                print('\t', player.name, '\t', player.score)



def main():
    print('добро пожаловать в игру!')
    names = []
    num = games.ask_num('сколько всего игроков?(2-4):', min = 2, max = 5)
    for i in range(num):
        name = input('введите имя игрока: ')
        #надо как-то добавить ограничение на одинаковые имена
        names.append(name)
    again = None
    while again != 'n':
        game = W_Game(names)
        game.play()
        again = games.ask_y_n('играть ещё?(y/n): ')

main()
