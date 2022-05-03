#таблица рекорддов с записью в файл records.txt


def open_file(file_name, mode):
    '''открывает файл, обрабатывает искл'''
    try:
        the_file = open(file_name, mode, encoding = 'utf-8')
    except IOError as e:
        print('не удается открыть файл', file_name, 'работа программы будет завершена')
        input('press enter')
    else:
        return the_file

def next_line(the_file):
    '''читает следующую строку'''
    line = the_file.readline()
    line = line[:-1]
    return line

def schet(the_file):
    '''создает следующую пару имя-счет из файла'''
    n = next_line(the_file)
    s = next_line(the_file)
    return n, s


def vnesti(name, score, slovar):
    '''добавляет или изменяет счет игрока'''
    if name in slovar:
        if slovar[name] < score:
            slovar[name] = score
    else:
        slovar[name] = score
    return slovar

def zapic(slovar, the_file, mode):
    scs = open_file(the_file, mode)
    for n in slovar:
        scs.write(n + '\n' + str(slovar[n]) + '\n')

    scs.close()



def records(sc):
    scores = open_file('records.txt', 'r')
    n, s = schet(scores)
    slovar = {}
    while n:
        s = int(s)
        slovar[n] = s
        n, s = schet(scores)
    scores.close()

    name = input('введите своё имя: ')

    slovar_new = vnesti(name, score, slovar)
    print(slovar_new)
    zapic(slovar_new, 'records.txt', 'w')

score = int(input('счет'))
records(score)
