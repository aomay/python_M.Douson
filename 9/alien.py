#гибель пришельца
#демонстрирует взаимодействие объектов
class Player(object):
    def blast(self, enemy):
        print('игрок стреляет!')
        enemy.die()
class Alien(object):
    def die(self):
        print('пришелец умер!')

def main():
    hero = Player()
    invador = Alien()
    hero.blast(invador)

main()
