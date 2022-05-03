
#игра в анаграаммы

#создаем кортеж из слов

import random

words = ('утка',
        'стол',
        'окно',
        'пятница',
        'выходной')

#пргграмма выбирает слово и перемешает буквы

word = random.choice(words)
win = word
word1 = ''
while word:
    ch = random.randrange(len(word))
    lit = word [ch]
    word1 += lit
    word = word[:ch] + word[ch+1:]
    print ('word: ', word, '    word1: ', word1, '     len(word): ', len(word))
    input ('press enter')


input('press enter to exit')
