from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pizza(games.Sprite):
    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy

def main():
    wall_img = games.load_image('wall.jpg', transparent = False)
    games.screen.background = wall_img
    pizza_img = games.load_image('pizza.bmp', transparent = True)
    pizza = Pizza(pizza_img,
                    x = 320,
                    y = 240,
                    dx = 1,
                    dy = 1)
    games.screen.add(pizza)
    games.screen.mainloop()

main()
