#викторины


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
    '''читает следующую строку, вставляет ентер вместо /'''
    line = the_file.readline()
    line = line.replace('/', '\n')
    line = line[:-1]
    return line

def next_block(the_file):
    '''переходит к следующему блоку вопросов'''
    tema = next_line(the_file)
    vopr = next_line(the_file)
    variants = []
    for i in range(4):
        variants.append(next_line(the_file))
    otvet = next_line(the_file)
    comment = next_line(the_file)
    return tema, vopr, variants, otvet, comment

def welcome(title):
    '''приветствие'''
    print('Добро пожаловать в викторины')
    print('\t', title, '\n')

def main():
    viktorina = open_file('vikt_vopr.txt', 'r')
    title = next_line(viktorina)
    welcome(title)
    score = 0
    tema, vopr, variants, otvet, comment = next_block(viktorina)
    while tema:
        print('\t', tema, '\n', vopr)
        for i in range(4):
            print('\t', variants[i])
        vibor = input('введите номер ответа: ')
        if vibor == otvet:
            print('правильно!')
            print(comment)
            score += 1
        else:
            print('не правильно')
            print(comment)
        tema, vopr, variants, otvet, comment = next_block(viktorina)
    viktorina.close()
    print('ваш счет: ', score)

main()
input('press enter')
