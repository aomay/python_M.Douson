otvet = ''

while otvet not in ('да', 'нет'):
    otvet = input('сейчас лето? \n')
    if otvet not in ('да', 'нет'):
        print('ответьте да или нет')
print('спасибо за ответ')
