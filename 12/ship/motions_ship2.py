from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Ship(games.Sprite):
    speed = 2
    def update(self):
        if games.keyboard.is_pressed(games.K_w):
            self.y -= self.speed
        if games.keyboard.is_pressed(games.K_s):
            self.y += self.speed
        if games.keyboard.is_pressed(games.K_d):
            self.angle += 1
        if games.keyboard.is_pressed(games.K_a):
            self.angle -= 1
        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270
        if games.keyboard.is_pressed(games.K_5):
            self.angle = -90
def main():
    nebula_img = games.load_image('nebula.bmp', transparent = False)
    ship_img = games.load_image('ship.bmp')
    ship = Ship(image = ship_img, x = games.screen.width / 2, y = games.screen.height / 2)
    games.screen.add(ship)
    games.screen.background = nebula_img
    games.screen.mainloop()
main()
