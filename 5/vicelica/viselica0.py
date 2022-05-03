#игра виселица
#списки, кортежи, псевдографика

import random

CHEL = ('''
______
|    |
|
|
|
|
''',
'''
______
|    |
|    O
|
|
|
''',
'''
______
|    |
|   _O_
|    |
|
|
''',
'''
______
|    |
|   _O_
|  | | |
|
|
''',
'''
______
|    |
|   _O_
|  | | |
|   | |
|
''')

MAX_OSH = len(CHEL) - 1
osh = 0

obmen = ''

variant = ''

used = []

abc = 'йцукенгшщзхъфывапролджэячсмитьбюё'

WORDS = ('утка',
        'стол',
        'окно',
        'пятница',
        'выходной')

print('привет. это игра ВИСЕЛИЦА. Чтобы выиграть, угадай слово по буквам.')
input('нажми enter чтобы начать')

word = random.choice(WORDS)
mask = '-' * len(word)

while mask != word and osh < MAX_OSH:
    print('\nИтак, твоё состояние на данный момент: \n', CHEL[osh])
    print('слово выглядит так: ', mask, '\nты ужк называл буквы:', used, '\nможно ошибиться еще ', MAX_OSH - osh, 'раз')

    while variant not in abc or len(variant) != 1:
        variant = input('\nпопробуй отгадать букву: ')
        if variant not in abc:
            print('\nможно использовать только буквы русского алфавита')

    if variant not in used:
        if variant in word:
            print('\nОТКРОЙТЕ БУКВУ \'', variant, '\'')
            for i in range (len(word)):
                if variant == word[i]:
                    obmen += variant
                else:
                    obmen += mask[i]
            mask = obmen
            obmen = ''
        else:
            print('\nнет такой буквы!')
            osh += 1
        used.append(variant)
    else:
        print('\nты уже называл эту букву!')
    variant = ''

if mask == word:
    print('\n\nТЫ ПОБЕДИЛ!\n')
else:
    print('\n\nПОТРАЧЕНО!\n', CHEL[osh])

print('было загадано слово: ', word)
input('нажми enter, чтобы выйти')
