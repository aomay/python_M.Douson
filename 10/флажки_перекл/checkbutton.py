from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_wdget()
    def create_wdget(self):
        Label(self, text = 'укажите ваши любимые жанры кино:').grid()
        Label(self, text = 'выберите все те, что вам по душе:').grid()
        self.likes_comedy = BooleanVar()
        Checkbutton(self, text = 'Комедия', variable = self.likes_comedy,
                    command = self.update_text).grid()
        self.likes_drama = BooleanVar()
        Checkbutton(self, text = 'Драмма', variable = self.likes_drama,
                    command = self.update_text).grid()
        self.likes_romance = BooleanVar()
        Checkbutton(self, text = 'Мелодрамма', variable = self.likes_romance,
                    command = self.update_text).grid()
        self.result_text = Text(self, height = 5, width = 30, wrap = WORD)
        self.result_text.grid()
    def update_text(self):
        likes = ''
        if self.likes_comedy.get():
            likes += 'вам нравятся комедии\n'
        if self.likes_drama.get():
            likes += 'вам нравятся драммы\n'
        if self.likes_romance.get():
            likes += 'вам нравятся мелодраммы\n'
        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, likes)

def main():
    root = Tk()
    root.title('кино')
    root.geometry('300x280')
    app = Application(root)
    root.mainloop()

main()
