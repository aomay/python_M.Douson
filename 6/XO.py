#крестики-нолики

import random, time

BIP = ('1', '0', '1100', 'www', 'qqq')

HODI = ('твой ход: ', 'удиви меня: ', 'ходи уже: ')

WIN = ((0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6))

NICE_TURN = (4, 0, 2, 6, 8, 1, 3, 5, 7)

def instr():
    print('''
    выбирай поле согласно инструкции:
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
    '''
    )

def ask_1(quest):
    otvet = ''
    while otvet not in ('да', 'нет'):
        otvet = input(quest)
        if otvet not in ('да', 'нет'):
            print('просто ответь \'да\' или \'нет\'')
    return otvet

def vibor_polya(quest, start, finish):
    ch = None
    legal = []
    for i in range(start, finish):
        legal += str(i)
    while ch not in legal:
        ch = input(quest)
        if ch not in legal:
            print('только числа от 0 до 8')
    return int(ch)

def human_turn():
    ch = vibor_polya(random.choice(HODI), 0, 9)
    while pole[ch] in ('X', 'O'):
        ch = vibor_polya('попробуй другое поле: ', 0, 9)
    pole_human = pole[:]
    pole_human[ch] = h
    return pole_human

def bot_turn():
    pole_bot = pole[:]
    for i in NICE_TURN:
        if pole_bot[i] not in ('X', 'O'):
            pole_bot[i] = b
            for row in WIN:
                if pole_bot[row[0]] == pole_bot[row[1]] == pole_bot[row[2]] == b:
                    return pole_bot
            pole_bot[i] = ' '
    for i in NICE_TURN:
        if pole_bot[i] not in ('X', 'O'):
            pole_bot[i] = h
            for row in WIN:
                if pole_bot[row[0]] == pole_bot[row[1]] == pole_bot[row[2]] != ' ':
                    pole_bot[i] = b
                    return pole_bot
            pole_bot[i] = ' '
    for i in NICE_TURN:
        if pole_bot[i] not in ('X', 'O'):
            pole_bot[i] = b
            return pole_bot

def show_pole():
    print('\t', pole[0],'|' , pole[1], '|', pole[2])
    print('\t', '---------')
    print('\t', pole[3],'|' , pole[4], '|', pole[5])
    print('\t', '---------')
    print('\t', pole[6],'|' , pole[7], '|', pole[8])

def you_win(pole):
    for row in WIN:
        if pole[row[0]] == pole[row[1]] == pole[row[2]] != ' ':
            winner = pole[row[0]]
            return winner
    if ' ' not in pole:
        winner = 'N'
        return winner
    return None

def congrat():
    if you_win(pole) == h:
        print('---------------------')
        print('ты выиграл')
    elif you_win(pole) == b:
        print('---------------------')
        print('ты проиграл')
    else:
        print('---------------------')
        print('ничья')


# Основная часть

instr()
escho = 'да'

while escho == 'да':
    pole = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    resp = ask_1('хочешь ходить первым?: ')

    if resp == 'да':
        print('ты играешь за \'X\'')
        h = 'X'
        b = 'O'
    else:
        print('я начну. играй за \'O\'')
        h = 'O'
        b = 'X'

    while not you_win(pole):
        if h == 'X':
            pole = human_turn()
            show_pole()
            if not you_win(pole):
                pole = bot_turn()
                for i in range(3):
                    time.sleep(1)
                    print(random.choice(BIP))
                time.sleep(1)
                show_pole()
        else:
            pole = bot_turn()
            for i in range(3):
                time.sleep(1)
                print(random.choice(BIP))
            time.sleep(1)
            show_pole()
            if not you_win(pole):
                pole = human_turn()
                show_pole()

    congrat()
    escho = ask_1('играем еще?')
print('приходи, когда будешь готов!')
input('нажми enter чтобы выйти')
