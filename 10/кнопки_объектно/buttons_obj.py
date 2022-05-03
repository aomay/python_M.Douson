from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.btn1 = Button(self, text = 'кнопка 1')
        self.btn1.grid()
        self.btn2 = Button(self)
        self.btn2.grid()
        self.btn2.configure(text = 'кнопка 2')
        self.btn3 = Button(self)
        self.btn3.grid()
        self.btn3['text'] = 'кнопка 3'

def main():
    root = Tk()
    root.title('окно с кнопками')
    root.geometry('400x200')
    app = Application(master = root)
    root.mainloop()

main()
