#тамагочи
#виртуальный питомец

class Critter(object):

    def __init__(self, name, boredom = 0, hunger = 0):
        self.name = name
        self.boredom = boredom
        self.hunger = hunger

    def __pass_time(self):
        self.boredom += 1
        self.hunger += 1

    @property
    def __mood(self):
        unhappiness = self.boredom + self.hunger
        if unhappiness < 5:
            m = 'прекрасно'
        elif 5 <= unhappiness <= 10:
            m = 'неплохо'
        elif 11 <= unhappiness <= 15:
            m = 'бывало и лучше'
        else:
            m = 'плохо'
        return m

    def talk(self):
        print('привет, меня зовут ', self.name, '. я чуствую себя ', self.__mood)

    def eat(self, food = 4):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        print('покушано')
        self.__pass_time()

    def play(self, fun = 4):
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        print('поиграно')
        self.__pass_time()

def main():
    crit_name1 = input('введите имя питомца: ')
    crit1 = Critter(crit_name1)
    ch = ''
    while ch != '0':
        print('''
        0 - выход
        1 - узнать состояние питомца
        2 - покормить
        3 - поиграть
        ''')
        ch = input('выберите действие: ')
        if ch  == '0':
            print('пока')
        elif ch == '1':
            crit1.talk()
        elif ch == '2':
            crit1.eat()
        elif ch == '3':
            crit1.play()
        else:
            print('нет такого пункта меню')

main()
input('press enter')
