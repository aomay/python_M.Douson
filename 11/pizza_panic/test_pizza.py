from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)
wall_img = games.load_image('wall.jpg', transparent = False)
games.screen.background = wall_img
pizza_img = games.load_image('pizza.bmp', transparent = True)
pizza = games.Sprite(pizza_img,
                    x = 320,
                    y = 240,
                    dx = 1,
                    dy = 1)
games.screen.add(pizza)
score = games.Text(value = 12133,
                    size = 60,
                    color = color.black,
                    x = 550,
                    y = 30)
games.screen.add(score)
won_message = games.Message(value = 'Победа!',
                            size = 60,
                            color = color.red,
                            x = games.screen.width/2,
                            y = games.screen.height/2,
                            lifetime = 250,
                            after_death = games.screen.quit)
#games.screen.add(won_message)

games.screen.mainloop()
