from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_wdgets()
    def create_wdgets(self):
        Label(self, text = 'Введите данные для создания нового рассказа: ').grid(
row = 0, column = 0, columnspan = 2, sticky = W)
        Label(self, text = 'Имя человека:').grid(row = 1, column = 0, sticky = W)
        self.ent_name = Entry(self, width = 20)
        self.ent_name.grid(row = 1, column = 1, sticky = W)
        Label(self, text = 'Существительное во мн. ч.:').grid(
row = 2, column = 0, sticky = W)
        self.ent_s = Entry(self, width = 20)
        self.ent_s.grid(row = 2, column = 1, sticky = W)
        Label(self, text = 'глагол в инфинитиве:').grid(row = 3, column = 0, sticky = W)
        self.ent_verb = Entry(self, width = 20)
        self.ent_verb.grid(row = 3, column = 1, sticky = W)
        Label(self, text = 'прилагательное(-ые):').grid(row = 4, column = 0, sticky = W)
        self.adj1 = BooleanVar()
        Checkbutton(self, text = 'нетерпеливый', variable = self.adj1,
).grid(row = 4, column = 1, sticky = W)
        self.adj2 = BooleanVar()
        Checkbutton(self, text = 'радостный', variable = self.adj2,
).grid(row = 4, column = 2, sticky = W)
        self.adj3 = BooleanVar()
        Checkbutton(self, text = 'пронизывающий', variable = self.adj3,
).grid(row = 4, column = 3, sticky = W)
        Label(self, text = 'часть тела:').grid(row = 5, column = 0, sticky = W)
        self.peace = StringVar()
        self.peace.set(None)
        Radiobutton(self, text = 'пупок', variable = self.peace, value = 'пупок',
).grid(row = 5, column = 1, sticky = W)
        Radiobutton(self, text = 'палец', variable = self.peace, value = 'большой палец левой ноги',
).grid(row = 5, column = 2, sticky = W)
        Radiobutton(self, text = 'мозг', variable = self.peace, value = 'костный мозг',
).grid(row = 5, column = 3, sticky = W)
        Button(self, text = 'получить результат', command = self.up_text).grid(
row = 6, column = 0, sticky = W)
        self.result_text =  Text(self, width = 60, height = 10, wrap = WORD)
        self.result_text.grid(row = 7, column = 0, sticky = W, columnspan = 4)
    def up_text(self):
        message_adj = ''
        if self.adj1.get():
            message_adj += 'нетерпеливое, '
        if self.adj2.get():
            message_adj += 'радостное, '
        if self.adj3.get():
            message_adj += 'пронизывающее, '
        message_peace = self.peace.get()
        message_name = self.ent_name.get()
        message_s = self.ent_s.get()
        message_verb = self.ent_verb.get()
        result_message = 'Знаменитый путешественник ' + message_name +\
' уже совсем отчаялся довершить дело всей своей жизни' +\
' - поиск затеряного города в котором, по легенде, обитали ' +\
message_s + '. Но однажды ' + message_name + ' и ' + message_s +\
' столкнулись лицом к лицу. Мощные, ' + message_adj +\
'ни с чем не сравнимое чувство охватило душу путешественника. Цель была достигнута. ' +\
message_name + ' ощутил как на его ' + message_peace +\
' скатилась слеза. И тут внезапно ' +\
message_s + ' перешли в атаку и сожрали героя. Мораль: если задумал ' +\
message_verb + ' делай это осторожно!'
        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, result_message)

def main():
    root = Tk()
    root.title('сумасшедший сказочник')
    root.geometry('620x430')
    app = Application(root)
    root.mainloop()
main()
