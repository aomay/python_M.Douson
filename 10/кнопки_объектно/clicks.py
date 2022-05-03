from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.button_clicks = 0
        self.create_widgets()
    def create_widgets(self):
        self.btn1 = Button(self)
        self.btn1['text'] = 'количество кликов: ' + str(self.button_clicks)
        self.btn1['command'] = self.update_count
        self.btn1.grid()
    def update_count(self):
        self.button_clicks += 1
        self.btn1['text'] = 'количество кликов: ' + str(self.button_clicks)

def main():
    root = Tk()
    root.title('кликер')
    root.geometry('200x100')
    app = Application(root)
    root.mainloop()

main()
