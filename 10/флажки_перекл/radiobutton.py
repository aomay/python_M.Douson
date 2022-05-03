from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_wdget()
    def create_wdget(self):
        Label(self, text = 'укажите ваши любимые жанры кино:').grid()
        Label(self, text = 'выберите все те, что вам по душе:').grid()
        self.favorite = StringVar()
        self.favorite.set(None)
        Radiobutton(self, text = 'Комедия', variable = self.favorite,
                    value = 'комедия', command = self.update_text).grid()
        Radiobutton(self, text = 'Драмма', variable = self.favorite,
                    value = 'драмма', command = self.update_text).grid()
        Radiobutton(self, text = 'Мелодрамма', variable = self.favorite,
                    value = 'мелодрамма' ,command = self.update_text).grid()
        self.result_text = Text(self, height = 5, width = 30, wrap = WORD)
        self.result_text.grid()
    def update_text(self):
        message = 'Ваш любимый жанр - '
        message += self.favorite.get()
        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, message)

def main():
    root = Tk()
    root.title('кино')
    root.geometry('300x280')
    app = Application(root)
    root.mainloop()

main()
