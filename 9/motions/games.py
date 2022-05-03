#модуль для игр

class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name + '\t' + str(self.score)
        return rep

def ask_y_n(quest):
    resp = None
    while resp not in ('y', 'n'):
        resp = input(quest).lower()
    return resp

def ask_num(quest, low, hight):
    resp = None
    while resp not in range(low, hight):
        resp = int(input(quest))
    return resp

def ask_course(quest):
    resp = None
    while resp not in ['w', 'W', 'a', 'A', 's', 'S', 'd', 'D']:
        resp = input(quest).lower()
    return resp

if __name__ == '__main__':
    print('Это модуль классов и функций для игр. Его стоит импортировать.')
    input('press enter')
