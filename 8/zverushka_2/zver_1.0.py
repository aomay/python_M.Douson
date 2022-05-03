#изучение классов
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
        rep = 'питомец: ' + self.__name + '\n'
        rep += 'голод:   ' + str(self.__hunger) + '\n'
        rep += 'уныние:  ' + str(self.__boredom)
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
        print('привет, меня зовут ', self.name, ' и я чувствую себя ', self.mood())
        self.__pass_time()
    def eat(self, food = 0):
        while food not in range(2, 6):
            food = int(input('сколько порций скормить питомцу (2-5)? '))
        self.__hunger -= food
        if self.__hunger < 0:
            self.__hunger = 0
        print('поел!')
        self.__pass_time()
    def play(self, fun = 0):
        while fun not in (2, 3, 4, 5):
            fun = int(input('сколько минут играть с питомцем (2-5)? '))
        self.__boredom -= fun
        if self.__boredom < 0:
            self.__boredom = 0
        print('поиграл!')
        self.__pass_time()

def main():
    crit = Critter(input('введите имя питомца: '))
    crit.talk()
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
            crit.talk()
        elif choice == '2':
            crit.eat()
        elif choice == '3':
            crit.play()
        elif choice == '4':
            crit.name = input('введите новое имя: ')
        elif choice == '111':
            print(crit)
        else:
            print('в меню нет пункта ', choice)

main()
