from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.inst_lbl = Label(self, text = 'чтобы узнать, как дожить до ста, введите пароль: ')
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.pw_lbl = Label(self, text = 'пароль: ')
        self.pw_lbl.grid(row = 1, column = 0, sticky = E)
        self.pw_ent = Entry(self, width = 20)
        self.pw_ent.grid(row = 1, column = 1, sticky = E)
        self.submit_btn = Button(self, text = 'OK', command = self.reveal)
        self.submit_btn.grid(row = 2, column = 1, sticky = E)
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 5, column = 0, columnspan = 2, sticky = W)
    def reveal(self):
        contents = self.pw_ent.get()
        if contents == 'secret':
            message = 'дожить до 99 и прожить еще год'
        else:
            message = 'ошибка доступа'
            self.pw_ent.delete(0, END)
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

def main():
    root = Tk()
    root.title('secret of 100')
    root.geometry('400x220')
    app = Application(root)
    root.mainloop()

main()
