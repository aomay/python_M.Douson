from tkinter import *
import random

class Application(Frame):
    def __init__(self, master, num):
        super().__init__(master)
        self.grid()
        self.create_wdgets()
        self.num = num
        self.tr = 1
    def create_wdgets(self):
        Label(self, text = 'Попробуйте отгадать число\n (от 1 до 100)за наименьшее\n\
количество попыток.\nЕсли Вы ошибётесь -\n получите подсказку!').grid(row = 0,
column = 0, sticky = W, columnspan = 2)
        Label(self, text = 'Ваш вариант:').grid(row = 1, column = 0, sticky = W, columnspan = 2)
        self.ent_var = Entry(self, width = 11)
        self.ent_var.grid(row = 1, column = 1, sticky = W)
        self.btn = Button(self, text = 'проверить', command = self.check)
        self.btn.grid(row = 2, column = 0, sticky = W)
        self.result_text = Text(self, width = 19, height = 2, wrap = WORD)
        self.result_text.grid(row = 3, column = 0, columnspan = 2, sticky = W)
    def check(self, num = 50):
        if int(self.ent_var.get()) < self.num:
            self.tr += 1
            self.result_text.delete(0.0, END)
            self.result_text.insert(0.0, 'больше...')
        elif int(self.ent_var.get()) > self.num:
            self.tr += 1
            self.result_text.delete(0.0, END)
            self.result_text.insert(0.0, 'меньше...')
        else:
            self.result_text.delete(0.0, END)
            message = 'вы победили! попыток потрачено:' + str(self.tr)
            self.result_text.insert(0.0, message)

def main():
    root = Tk()
    root.title('угадай число')
    root.geometry('210x230')
    num = 10
    app = Application(root, num)
    root.mainloop()
main()
