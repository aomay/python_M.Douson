from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    '''Сковорода. Основной класс игры. здесь считаются очки,
    выводится вся информация, создаются поворы, увеличивается сложность'''
    image = games.load_image('pan.bmp')
    def __init__(self):
        super().__init__(image = Pan.image,
                        x = games.mouse.x,
                        bottom = games.screen.height)
        self.score = games.Text(size = 60,
                                value = 0,
                                color = color.black,
                                top = 5,
                                right = games.screen.width - 10)
        games.screen.add(self.score)
        self.time = games.Text(size = 30,
                                value = 0,
                                color = color.black,
                                top = 5,
                                left = 30)
        games.screen.add(self.time)
        self.frame = 0
        self.chef_1 = None
        self.chef_2 = None
    def update(self):
        self.frame += 1
        self.time.value = self.frame // 50
        self.x = games.mouse.x
        if self.x < 0:
            self.x = 0
        if self.x > games.screen.width:
            self.x = games.screen.width
        self.check_catch()
        self.up_dif()
    def check_catch(self):
        '''увеличивает счет'''
        for pizza in self.overlapping_sprites:
            self.score.value += 1
            self.score.right = games.screen.width - 10
            pizza.handle_caught()
    def up_dif(self):
        '''постепенно увеличивает сложность игры. выдаёт номер уровня сообщением.'''
        if self.frame == 1:
            self.chef_1 = Chef()
            games.screen.add(self.chef_1)
            games.screen.add(games.Message(value = 'lvl 1',
                                        size = 100,
                                        color = color.black,
                                        x = games.screen.width / 2,
                                        y = games.screen.height / 2,
                                        lifetime = 200))
        if self.frame / 50 == 15:
            self.chef_1.hold(200)
            self.chef_1.up_speed(5)
            games.screen.add(games.Message(value = 'lvl 2',
                                        size = 100,
                                        color = color.black,
                                        x = games.screen.width / 2,
                                        y = games.screen.height / 2,
                                        lifetime = 200))
        if self.frame / 50 == 40:
            self.chef_1.hold(200)
            Pizza.speed = 2
            games.screen.add(games.Message(value = 'lvl 3',
                                        size = 100,
                                        color = color.black,
                                        x = games.screen.width / 2,
                                        y = games.screen.height / 2,
                                        lifetime = 200))
        if self.frame / 50 == 60:
            Pizza.speed = 1
            self.chef_2 = Chef()
            games.screen.add(self.chef_2)
            self.chef_1.hold(200)
            self.chef_2.hold(200)
            self.chef_1.up_speed(4)
            self.chef_2.up_speed(4)
            games.screen.add(games.Message(value = 'lvl 4',
                                        size = 100,
                                        color = color.black,
                                        x = games.screen.width / 2,
                                        y = games.screen.height / 2,
                                        lifetime = 200))
        if self.frame / 50 == 100:
            self.chef_1.hold(200)
            self.chef_2.hold(200)
            Pizza.speed = 2
            games.screen.add(games.Message(value = 'lvl 5',
                                        size = 100,
                                        color = color.black,
                                        x = games.screen.width / 2,
                                        y = games.screen.height / 2,
                                        lifetime = 200))
        if self.frame / 50 == 140:
            self.chef_1.hold(200)
            self.chef_2.hold(200)
            Pizza.speed = 3
            games.screen.add(games.Message(value = 'lvl 6',
                                        size = 100,
                                        color = color.black,
                                        x = games.screen.width / 2,
                                        y = games.screen.height / 2,
                                        lifetime = 200))

class Pizza(games.Sprite):
    '''Пицца. Так завершает игру при падении на нижнюю границу.'''
    image = games.load_image('pizza.bmp')
    speed = 1
    def __init__(self, x, y = 90):
        super().__init__(image = Pizza.image,
                        x = x,
                        y = y,
                        dy = Pizza.speed)
    def update(self):
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
    def handle_caught(self):
        self.destroy()
    def end_game(self):
        '''завершение игры'''
        end_message = games.Message(value = 'конец игры',
                                    size = 60,
                                    color = color.red,
                                    x = games.screen.width / 2,
                                    y = games.screen.height / 2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

class Chef(games.Sprite):
    image = games.load_image('chef.bmp')
    odds_change = 200
    speed = 2
    def __init__(self, y = 55):
        super().__init__(image = Chef.image,
                        x = games.screen.width / 2,
                        y = y,
                        dx = Chef.speed)
        self.odds_change = Chef.odds_change
        self.time_til_drop = 0
    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        self.check_drop()
    def hold(self, t):
        '''не бросать пиццу в течение времени t'''
        self.time_til_drop += t
    def up_speed(self, speed):
        '''устанавливает скорость шефа (изначально - 2)'''
        self.dx = speed
    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
            self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1

def main():
    wall_img = games.load_image('wall.jpg', transparent = False)
    games.screen.background = wall_img
    the_pan = Pan()
    games.screen.add(the_pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()
main()
