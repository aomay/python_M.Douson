
import random

words = ('утка',
        'стол',
        'окно',
        'пятница',
        'выходной')

word = random.choice (words)

print ('приет, я загадал слово. Попробуй отгадать его по букве. У тебя 5 попыток.')

input ('нажми enter чтобы начать')

print ('в слове', len(word), 'букв')

lit = ''
k = 1

for k in range (5):
    lit = input ('попробуй отгадать букву или назови слово сразу: ')
    if len (lit) == 1:
        if lit in word:
            print ('в слове есть буква ', lit, '!')
        else:
            print ('нет такой буквы!')
        k += 1
    elif lit == word:
        break
    else:
        print ('ну не. давай лучше по буквам.')

if lit == word:
    print ('ты гений. ты отгадал слово с ', k+1, ' попыток')
    input ('press enter')
else:
    otvet = input ('пора отгадывать!: ')
    if otvet == word:
        print ('правильно! подарки в студию!')
        input ('press enter')
    else:
        print ('не то! в другой раз повезет) было загадано слово : ', word)
        input ('press enter')
