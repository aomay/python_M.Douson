from tkinter import *

root = Tk()
root.title('окно с меткой и кнопками')
root.geometry('400x200')
app = Frame(root)
app.grid()
lbl = Label(app, text = 'метка 1')
lbl.grid()
btn1 = Button(app, text = 'кнопка 1')
btn1.grid()
btn2 = Button(app)
btn2.grid()
btn2.configure(text = 'кнопка 2')
btn3 = Button(app)
btn3.grid()
btn3['text'] = 'кнопка 3'

root.mainloop()
