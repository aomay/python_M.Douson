class Player(object):
    def __init__(self, name, score = 0):
        '''игрок с именем и счетом'''
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name + ':\t' + self.score
        return rep

def ask_y_n(question):
    '''задать вопрос с ответом y/n'''
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
        return response

def ask_num(question, min, max):
    '''попросить выбрать число от min до max'''
    resp = None
    while resp not in range(min, max):
        resp = int(input(question))
    return resp

if __name__ == '__main__':
    print('это модуль! импортируйте его в вашу программу!')
