#телевизор как объект. переключение каналов и громкости
class Tv(object):
    '''ТВ'''
    def __init__(self, ch, vol):
        self.__ch = ch
        self.__vol = vol
    def __str__(self):
        rep = 'канал: ' + str(self.__ch) + '    громкость: ' + str(self.__vol)
        return rep
    @property
    def ch(self):
        return self.__ch
    @ch.setter
    def ch(self, new_ch):
        if int(new_ch) not in range(1, 101):
            print('в тв всего 100 каналов')
        else:
            self.__ch = new_ch
    @property
    def vol(self):
        return self.__vol
    @vol.setter
    def vol(self, new_vol):
        if int(new_vol) not in range(1, 11):
            print('максимальная громкость - 10')
        else:
            self.__vol = new_vol

def main():
    tv1 = Tv(ch = 0, vol = 0)
    choice = ''
    while choice != '0':
        print('''
        !!!ТВ включен!!!
        1 - выбрать канал
        2 - установить громкость
        0 - выкл.''')
        print(tv1)
        choice = input('выбор: ')
        if choice == '1':
            tv1.ch = input('введите номер канала: ')
        elif choice == '2':
            tv1.vol = input('выберите громкость: ')
        elif choice == '0':
            print('выключение...')
        else:
            print('нет варианта', choice)

main()
