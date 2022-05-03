#изучение классов
#3 питомца
from random import randrange as r
class Critter(object):
    '''виртуальный питомец'''
    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.__hunger = hunger
        self.__boredom = boredom
        print('создан новый питомец!')
    def __pass_time(self):
        self.__hunger += 1
        self.__boredom += 1
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if new_name == '':
            print('имя не может быть пустой строкой!')
        else:
            self.__name = new_name
            print('имя успешно изменено! ')
    def __str__(self):
        rep = 'питомец: ' + self.__name + '\t'
        rep += 'голод:\t' + str(self.__hunger) + '\t'
        rep += 'уныние:\t' + str(self.__boredom)
        return rep
    def mood(self):
        unhappy = self.__hunger + self.__boredom
        if unhappy < 5:
            m = 'прекрасно'
        elif 5 <= unhappy <= 10:
            m = 'неплохо'
        elif 11 <= unhappy <= 15:
            m = 'неочень'
        elif 15 <= unhappy:
            m = 'ужасно'
        return m
    def talk(self):
        print(self.name, '\tчувствует себя ', self.mood())
        self.__pass_time()
    def eat(self, food):
        self.__hunger -= food
        if self.__hunger < 0:
            self.__hunger = 0
        self.__pass_time()
    def play(self, fun):
        self.__boredom -= fun
        if self.__boredom < 0:
            self.__boredom = 0
        self.__pass_time()


def main():
    crit1 = Critter(name = input('введите имя 1го питомца:\t'), hunger = r(10), boredom = r(10))
    crit2 = Critter(name = input('введите имя 2го питомца:\t'), hunger = r(10), boredom = r(10))
    crit3 = Critter(name = input('введите имя 3го питомца:\t'), hunger = r(10), boredom = r(10))
    zoopark = (crit1, crit2, crit3)
    choice = None
    while choice != '0':
        print('''
----------МЕНЮ------------
    0 - выход
    1 - самочувствие
    2 - покормить
    3 - поиграть
    4 - переименовать
--------------------------
        ''')
        choice = input('выбор: ')
        print()
        if choice == '0':
            print('пока')
        elif choice == '1':
            for crit in zoopark:
                crit.talk()
        elif choice == '2':
            q_food = ''
            while q_food not in range(2, 6):
                q_food = int(input('сколько порций скормить питомцу (2-5)?\t'))
            for crit in zoopark:
                crit.eat(food = q_food)
            print('поели!')
        elif choice == '3':
            q_fun = ''
            while q_fun not in (2, 3, 4, 5):
                q_fun = int(input('сколько минут играть с питомцем (2-5)?\t'))
            for crit in zoopark:
                crit.play(q_fun)
            print('поиграли!')
        elif choice == '4':
            name_choiced = ''
            while name_choiced not in (crit1.name, crit2.name, crit3.name):
                name_choiced = input('имя какого питомца изменить? \nстарое имя:    ')
            if name_choiced == crit1.name:
                crit1.name = input('новое имя:\t')
            elif name_choiced == crit2.name:
                crit2.name = input('новое имя:\t')
            elif name_choiced == crit3.name:
                crit3.name = input('новое имя:\t')
        elif choice == '111':
            for crit in zoopark:
                print(crit)
        else:
            print('в меню нет пункта ', choice)

main()
