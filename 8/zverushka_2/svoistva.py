class Critter(object):
    total = 0
    @staticmethod
    def status():
        print('всего питомцев: ', Critter.total)
    def __init__(self, name):
        self.__name = name
        print('создан новый питомец!')
        Critter.total += 1
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
    def talk(self):
        print('привет меня зовут: ', self.name)

crit = Critter('ааа')
print('имя питомца: ', crit.name)

crit.name = input('введите новое имя питомца: ')
print('новое имя питомца: ', crit.name)

input()
