from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Man(games.Sprite):
    image = games.load_image('man.bmp')
    def __init__(self):
        super().__init__(image = Man.image,
                        y = games.mouse.y,
                        x = games.mouse.x)
        self.time = games.Text(size = 30,
                                value = 0,
                                color = color.black,
                                top = 5,
                                left = 30)
        games.screen.add(self.time)
        self.frame = 0
    def update(self):
        self.frame += 1
        self.time.value = self.frame // 50
        self.x = games.mouse.x
        if self.left < 40:
            self.left = 40
        if self.right > games.screen.width - 40:
            self.right = games.screen.width - 40
        self.y = games.mouse.y
        if self.bottom > games.screen.height - 40:
            self.bottom = games.screen.height - 40
        if self.top < 40:
            self.top = 40
        self.up_dif()
        self.die()
    def die(self):
        if self.overlapping_sprites:
            self.destroy()
            end_message = games.Message(value = 'game over!',
                                        size = 60,
                                        color = color.red,
                                        x = games.screen.width / 2,
                                        y = games.screen.height / 2,
                                        lifetime = 400,
                                        after_death = games.screen.quit)
            games.screen.add(end_message)
    def up_dif(self):
        if self.frame == 1:
            killer1 = Killer('top')
            games.screen.add(killer1)
        if self.frame / 50 == 1:
            killer2 = Killer('bot')
            games.screen.add(killer2)
        if self.frame / 50 == 10:
            killer3 = Killer('left')
            games.screen.add(killer3)
        if self.frame / 50 == 20:
            killer2 = Killer('right')
            games.screen.add(killer2)
        if self.frame / 50 == 30:
            Bullet.bullet_speed = 2
        if self.frame / 50 == 40:
            Bullet.bullet_speed = 3
            Killer.shot_range = 50
        if self.frame / 50 == 50:
            Bullet.bullet_speed = 5

class Killer(games.Sprite):
    odds_change = 50
    image = games.load_image('killer.bmp')
    shot_range = 100         #интервал между выстрелами в кадрах
    def __init__(self, position):
        if position == 'top':
            self.set_x = games.screen.width / 2
            self.set_y = 20
            self.set_dx = 2
            self.set_dy = 0
            self.shot_dx = 0
            self.shot_dy = 1
        elif position == 'bot':
            self.set_x = games.screen.width / 2
            self.set_y = games.screen.height - 20
            self.set_dx = 2
            self.set_dy = 0
            self.shot_dx = 0
            self.shot_dy = -1
        elif position == 'left':
            self.set_x = 20
            self.set_y = games.screen.height / 2
            self.set_dx = 0
            self.set_dy = 2
            self.shot_dx = 1
            self.shot_dy = 0
        elif position == 'right':
            self.set_x = games.screen.width - 20
            self.set_y = games.screen.height / 2
            self.set_dx = 0
            self.set_dy = 2
            self.shot_dx = -1
            self.shot_dy = 0
        super().__init__(image = Killer.image,
                        x = self.set_x,
                        y = self.set_y,
                        dx = self.set_dx,
                        dy = self.set_dy)
        self.frame = 0
    def update(self):
        if self.left < 40 or self.right > games.screen.width - 40:
            self.dx = -self.dx
        if self.top < 40 or self.bottom > games.screen.height - 40:
            self.dy = -self.dy
        if random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
            self.dy = -self.dy
        self.frame += 1
        self.shot()
    def shot(self):
        if self.frame % Killer.shot_range == 0:
            new_bullet = Bullet(x = self.x, y = self.y, dx = self.shot_dx, dy = self.shot_dy)
            games.screen.add(new_bullet)

class Bullet(games.Sprite):
    bullet_speed = 1
    image = games.load_image('bullet.bmp')
    def __init__(self, x = 20, y = 20, dx = 0, dy = 0):
        super().__init__(image = Bullet.image,
                        x = x,
                        y = y,
                        dx = dx * Bullet.bullet_speed,
                        dy = dy * Bullet.bullet_speed)


def main():
    wall_img = games.load_image('background.bmp', transparent = False)
    games.screen.background = wall_img
    the_man = Man()
    games.screen.add(the_man)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()
main()
