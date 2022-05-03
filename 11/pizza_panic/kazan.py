from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collid()
    def check_collid(self):
        for pizza in self.overlapping_sprites:
            pizza.handle_collid()

class Pizza(games.Sprite):
    def handle_collid(self):
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)

def main():
    wall_img = games.load_image('wall.jpg', transparent = False)
    games.screen.background = wall_img
    kazan_img = games.load_image('pan.bmp')
    kazan = Pan(kazan_img,
                x = games.mouse.x,
                y = games.mouse.y)
    games.screen.add(kazan)
    pizza_img = games.load_image('pizza.bmp')
    pizza = Pizza(pizza_img,
                x = random.randrange(games.screen.width),
                y = random.randrange(games.screen.height))
    games.screen.add(pizza)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()
main()
