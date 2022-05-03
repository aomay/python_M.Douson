from livewires import games, color
import random, math

games.init(screen_width=640, screen_height=480, fps=50)


class Explosion(games.Animation):
    sound = games.load_sound('explosion.wav')
    images = ['explosion1.bmp',
              'explosion2.bmp',
              'explosion3.bmp',
              'explosion4.bmp',
              'explosion5.bmp',
              'explosion6.bmp',
              'explosion7.bmp',
              'explosion8.bmp',
              'explosion9.bmp']

    def __init__(self, x, y):
        super().__init__(images=Explosion.images,
                         x=x, y=y, repeat_interval=4,
                         n_repeats=1, is_collideable=False)
        Explosion.sound.play()


class Wrapper(games.Sprite):
    def update(self):
        if self.bottom < 0:
            self.top = games.screen.height
        if self.top > games.screen.height:
            self.bottom = 0
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        self.destroy()


class Collider(Wrapper):
    def update(self):
        super().update()
        self.overlapping_asteroids = []
        if self.overlapping_sprites:
            for obj in self.overlapping_sprites:
                if isinstance(obj, Asteroid):
                    self.overlapping_asteroids.append(obj)
            for sprite in self.overlapping_asteroids:
                sprite.die()
        if self.overlapping_asteroids:
            self.die()

    def die(self):
        self.destroy()
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)


class Asteroid(Wrapper):
    POINTS = 30
    total = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    SPAWN = 2
    images = {SMALL: games.load_image('asteroid_small.bmp'),
              MEDIUM: games.load_image('asteroid_med.bmp'),
              LARGE: games.load_image('asteroid_big.bmp')}
    SPEED = 2

    def __init__(self, game, x, y, size):
        super().__init__(
            image=Asteroid.images[size],
            x=x, y=y,
            dx=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size,
            dy=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size,
            angle=random.randrange(360))
        self.size = size
        Asteroid.total += 1
        self.game = game

    def die(self):
        super().die()
        Asteroid.total -= 1
        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game=self.game,
                                        x=self.x, y=self.y,
                                        size=self.size - 1)
                games.screen.add(new_asteroid)
        if Asteroid.total == 0:
            self.game.advance()


class Ship(Collider):
    image = games.load_image('ship.bmp')
    ROTATION_STEP = 3
    VELOCITY_STEP = .05
    MISSILE_DELAY = 30
    MAX_VEL = 2

    def __init__(self, game, x, y):
        super().__init__(image=Ship.image,
                         x=x, y=y)
        self.missile_wait = 0
        self.game = game

    def update(self):
        super().update()
        if self.missile_wait > 0:
            self.missile_wait -= 1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_UP):
            angle1 = self.angle * math.pi / 180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle1)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle1)
            self.dx = min(max(self.dx, -Ship.MAX_VEL), Ship.MAX_VEL)
            self.dy = min(max(self.dy, -Ship.MAX_VEL), Ship.MAX_VEL)
            turbine = Turbine(ship_x=self.x, ship_y=self.y,
                              ship_angle=angle1)
            games.screen.add(turbine)
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

    def die(self):
        super().die()
        self.game.end()


class Turbine(games.Sprite):
    image = games.load_image('turbine.bmp')
    BUFFER = 30

    def __init__(self, ship_x, ship_y, ship_angle):
        super().__init__(image=Turbine.image,
                         x=ship_x + Turbine.BUFFER * -math.sin(ship_angle),
                         y=ship_y + Turbine.BUFFER * math.cos(ship_angle),
                         angle=ship_angle * 180 / math.pi)

    def update(self):
        self.destroy()


class Missile(Collider):
    image = games.load_image('missile.bmp', transparent=1)
    BUFFER = 10
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        angle = ship_angle * math.pi / 180
        x = ship_x + Missile.BUFFER * math.sin(angle)
        y = ship_y + Missile.BUFFER * -math.cos(angle)
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)
        super().__init__(image=Missile.image,
                         x=x, y=y, dx=dx, dy=dy,
                         angle=ship_angle)
        self.lifetime = Missile.LIFETIME

    def update(self):
        super().update()
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()
        for obj in self.overlapping_asteroids:
            if isinstance(obj, Ship):
                self.overlapping_asteroids.remove(obj)


class Game(object):
    def __init__(self):
        self.lvl = 0
        self.sound = games.load_sound('level.wav')
        self.score = games.Text(value=0, size=30,
                                color=color.white, top=5,
                                right=games.screen.width - 10,
                                is_collideable=0)
        games.screen.add(self.score)
        self.ship = Ship(game=self,
                         x=games.screen.width / 2,
                         y=games.screen.height / 2)
        games.screen.add(self.ship)

    def play(self):
        games.music.load('theme.mid')
        games.music.play(-1)
        nebula_image = games.load_image('nebula.bmp', transparent=0)
        games.screen.background = nebula_image
        self.advance()
        games.screen.mainloop()

    def advance(self):
        self.lvl += 1
        # место вокруг уорабля
        BUFFER = 150
        for i in range(self.lvl):
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min
            x_distannce = random.randrange(
                x_min, games.screen.width - x_min)
            y_distannce = random.randrange(
                y_min, games.screen.height - y_min)
            x = self.ship.x + x_distannce
            y = self.ship.y + y_distannce
            x %= games.screen.width
            y %= games.screen.height
            new_asteroid = Asteroid(game=self,
                                    x=x, y=y, size=Asteroid.LARGE)
            games.screen.add(new_asteroid)
        lvl_message = games.Message(
            value='lvl ' + str(self.lvl),
            size=90,
            x=games.screen.width / 2,
            y=games.screen.height / 2,
            color=color.yellow,
            lifetime=3 * games.screen.fps,
            is_collideable=0)
        games.screen.add(lvl_message)
        if self.lvl > 1:
            self.sound.play()

    def end(self):
        end_message = games.Message(
            value='game over',
            size=90,
            x=games.screen.width / 2,
            y=games.screen.height / 2,
            color=color.red,
            lifetime=5 * games.screen.fps,
            is_collideable=0)
        games.screen.add(end_message)


def main():
    game = Game()
    game.play()


main()
