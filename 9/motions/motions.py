import games

class Cell(object):
    '''одна клетка карты'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def location(self):
        rep = '(' + str(self.x) + ':' + str(self.y) + ')'
        return rep
    def __str__(self):
        rep = '(' + str(self.x) + ':' + str(self.y) + ')'
        return rep

class Map(object):
    '''карта, состоящая клеток Cells'''
    def __init__(self , home_x = 0, home_y = 0, exit_x = 1, exit_y = -3):
        self.cells = [Cell(0, -1).location, Cell(-1, -1).location,
        Cell(-1, 0).location, Cell(0, -2).location, Cell(0, -3).location,
        Cell(1, -3).location, Cell(0, 1).location, Cell(1, 1).location,
        Cell(1, 2).location,]
        self.home = Cell(home_x, home_y)
        self.exit = Cell(exit_x, exit_y)
        self.cells.append(self.home.location)
        self.cells.append(self.exit.location)
    def __str__(self):
        return str(self.cells)
    def check_pass(self, player, course):
        '''проверяет возможность прохода игрока player по направлению course'''
        if course == 'w':
            if Cell(player.x, player.y + 1).location in self.cells:
                rep = True
            else:
                rep = False
        elif course == 'a':
            if Cell(player.x - 1, player.y).location in self.cells:
                rep = True
            else:
                rep = False
        elif course == 's':
            if Cell(player.x, player.y - 1).location in self.cells:
                rep = True
            else:
                rep = False
        elif course == 'd':
            if Cell(player.x + 1, player.y).location in self.cells:
                rep = True
            else:
                rep = False
        return rep

class Player(object):
    def __init__(self, name, home_x = 0, home_y = 0):
        self.name = name
        self.x = home_x
        self.y = home_y
    def __str__(self):
        rep = 'игрок: ' + self.name
        return rep
    @property
    def position(self):
        return '(' + str(self.x) + ':' + str(self.y) + ')'
    def go(self, course):
        '''движение игрока на 1 клетку по направлению course'''
        if course == 'w':
            self.y += 1
        elif course == 'a':
            self.x -= 1
        elif course == 's':
            self.y -= 1
        elif course == 'd':
            self.x += 1

def main():
    name = str(input('введите имя: '))
    player_1 = Player(name)
    print(player_1, '\tположение: ', player_1.position)
    map_1 = Map()
    #print(map_1)
    while player_1.position != map_1.exit.location:
        course = games.ask_course('выберите направление(w/a/s/d):')
        if map_1.check_pass(player_1, course):
            player_1.go(course)
        else:
            print('прохода нет')
        print(player_1, '\tположение: ', player_1.position)
    else:
        print('вы нашли выход!')
main()
