from livewires import games
import random

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
            dy = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)
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
    image2 = games.load_image('ship_turbine.bmp')
    ROTATION_STEP = 3
    def update(self):
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
            self.image = Ship.image2
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
            self.image = Ship.image2
def main():
    nebula_image = games.load_image('nebula.jpg')
    games.screen.background = nebula_image
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x, y, size)
        games.screen.add(new_asteroid)
    new_ship = Ship(image = Ship.image,
        x = games.screen.width / 2,
        y = games.screen.height / 2)
    games.screen.add(new_ship)
    games.screen.mainloop()
main()
