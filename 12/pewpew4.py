from livewires import games
import random, math

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Asteroid(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image('asteroid_small.bmp'),
            MEDIUM : games.load_image('asteroid_med.bmp'),
            LARGE : games.load_image('asteroid_big.bmp')}
    SPEED = 2
    def __init__(self, x, y, size):
        super().__init__(
            image = Asteroid.images[size],
            x = x, y = y,
            dx = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size,
            dy = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size,
            angle = random.randrange(360))
        self.size = size
    def update(self):
        '''огибание экрана'''
        if self.bottom < 0:
            self.top = games.screen.height
        if self.top > games.screen.height:
            self.bottom = 0
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

class Ship(games.Sprite):
    image = games.load_image('ship.bmp')
    ROTATION_STEP = 3
    VELOCITY_STEP = .05
    MISSILE_DELAY = 25
    def __init__(self, x, y):
        super().__init__(image = Ship.image,
            x = x, y = y)
        self.missale_wait = 0
    def update(self):
        if self.missale_wait > 0:
            self.missale_wait -= 1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_UP):
            angle1 = self.angle * math.pi / 180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle1)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle1)
            turbine = Turbine(ship_x = self.x, ship_y = self.y,
                ship_angle = angle1, ship_dx = self.dx, ship_dy = self.dy)
            games.screen.add(turbine)
        if games.keyboard.is_pressed(games.K_SPACE) and self.missale_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missale_wait = Ship.MISSILE_DELAY
        if self.bottom < 0:
            self.top = games.screen.height
        if self.top > games.screen.height:
            self.bottom = 0
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

class Turbine(games.Sprite):
    image = games.load_image('turbine.bmp')
    lifetime = 1
    BUFFER = 29
    def __init__(self, ship_x, ship_y, ship_dx, ship_dy, ship_angle):
        super().__init__(image = Turbine.image,
            x = ship_x + Turbine.BUFFER * -math.sin(ship_angle),
            y = ship_y + Turbine.BUFFER  * math.cos(ship_angle),
            dx = ship_dx, dy = ship_dy, angle = ship_angle * 180 / math.pi)
    def update(self):
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

class Missile(games.Sprite):
    image = games.load_image('missile.bmp')
    BUFFER = 25
    VELOCITY_FACTOR = 7
    LIFETIME = 40
    def __init__(self, ship_x, ship_y, ship_angle):
        angle = ship_angle* math.pi / 180
        x = ship_x + Missile.BUFFER * math.sin(angle)
        y = ship_y + Missile.BUFFER * -math.cos(angle)
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)
        super().__init__(image = Missile.image,
            x = x, y = y, dx = dx, dy = dy,
            angle = ship_angle)
        self.lifetime = Missile.LIFETIME
    def update(self):
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()
        if self.bottom < 0:
            self.top = games.screen.height
        if self.top > games.screen.height:
            self.bottom = 0
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width


def main():
    nebula_image = games.load_image('nebula.bmp', transparent = 0)
    games.screen.background = nebula_image
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL,
            Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x, y, size)
        games.screen.add(new_asteroid)
    new_ship = Ship(x = games.screen.width / 2,
        y = games.screen.height / 2)
    games.screen.add(new_ship)
    games.screen.mainloop()
main()
