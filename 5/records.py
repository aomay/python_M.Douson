
rec = []
ch = None

print(
'''
Меню рекордов:
0 - выйти
1 - показать рекорды
2 - добавить рекорд
'''
)

while ch != '0':
    ch = input('\nваш выбор: ')
    if ch == '0':
        print('Пока')
    elif ch == '1':
        for entry in rec:
            name, score = entry
            print(name, '\t', score)
    elif ch == '2':
        name = input('введите имя: ')
        score = int(input('введите счет: '))
        entry = (score, name)
        rec.append(entry)
        rec.sort(reverse = True)
        rec = rec[:3]
        print('рекорд записан!')
    else:
        print('нет варианта', ch)

input('нажмите enter')
