"""The game guess the number made by the computer.
The image and sound files are located in the repository by
name 'Image-and-sound-for-the-published-repositories'"""


"""Игра: Угадай число загаданное компьютером.
Файлы изображения и звука находятся в repository по имени
 'Image-and-sound-for-the-published-repositories'"""



import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random
from playsound import playsound


class App(tk.Tk):  # Главное Окно
    def __init__(self):
        super().__init__()

        self.geometry('400x650+600+25')
        self.title('''Игра "Угадай число"''')
        self.iconbitmap(default="C:\FOTO  Python\monitor26.ico")

        # создание фото для вставки
        self.foto1 = ImageTk.PhotoImage(file="C:\FOTO  Python\comp12.jpg")

        # окно-диалог
        self.button = tk.Button(self, image=self.foto1, command=self.exzit)
        self.button.pack(padx=10, pady=10)


        self.label = tk.Label(self, text='''Сейчас сыграем в игру "Угадай число".
Компьютер загадает число от "1" до "20" 
включительно. Вам предстоит угадать его.
От компьютера будут подсказки.''',
                              font='Times 14', foreground="#355286")
        self.label.pack(padx=0, pady=0)

        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var4 = tk.StringVar()

        self.var4.set('                                            ')

        # подсказка вверху
        self.label = tk.Label(self, textvariable=self.var2,
                              font='Times 20 bold', fg="#008000")
        self.label.pack(padx=10, pady=10)

        # поле ввода числа
        self.entry_1 = tk.Entry(self, textvariable=self.var1,
                                justify='center', width=5,
                                font='Times 30 bold')
        self.entry_1.pack()

        # подсказка внизу
        self.label = tk.Label(self, textvariable=self.var3,
                              font='Times 20 bold', fg='#ea0000')
        self.label.pack(padx=10, pady=10)

        # дать ответ
        self.foto2 = ImageTk.PhotoImage(file="C:\FOTO  Python\more003.jpg")
        self.button = tk.Button(self, image=self.foto2, command=self.com1)
        self.button.pack(padx=10, pady=10)

        # играть еще
        self.button = tk.Button(self, textvariable=self.var4, fg='#c46200',
                                font='Times 20 bold', command=self.go)
        self.button.pack(padx=10, pady=20)

        self.num = random.randint(1, 20)
        self.z = 0

    def Check_s1(self, TestS1, ValidSymbole):
        self.TestS1 = TestS1
        self.ValidSymbole = ValidSymbole
        flag = True
        for val1 in self.TestS1:
            if not (val1 in self.ValidSymbole):
                flag = False
                break
        if flag == True:
            return True
        else:
            return False

    def com1(self):

        prob = str('                        ')
        PVal = "1234567890"
        print(self.num)
        if not self.Check_s1((self.var1.get()), PVal) \
                or len(str(self.var1.get())) == 0:
            self.del_entry()
            self.f = 0
            messagebox.showerror('''ОШИБКА''', prob + '''   НЕДОПУСТИМЫЙ ВВОД:
                        (символы, буквы или нет данных)
                                        Введите  число.''')
        # угадали
        elif int((self.var1.get())) == self.num:
            self.z = self.z + 1
            self.f = 1
            self.var2.set('  УРА!!!   ВЫ   УГАДАЛИ.')
            self.var3.set('за    %s   попытки(ок)' % self.z)
            self.musika_pob()
            self.var4.set('      ИГРАТЬ ЕЩЁ      ')

        elif int((self.var1.get())) < self.num:
            self.z = self.z + 1
            self.f = 0
            self.var2.set('БОЛЬШЕ  "%s"' % self.var1.get())
            self.var3.set('                      ')
            self.del_entry()
            self.musika_neud()

        elif int((self.var1.get())) > self.num:
            self.z = self.z + 1
            self.f = 0
            self.var3.set('МЕНЬШЕ  "%s"' % self.var1.get())
            self.var2.set('                      ')
            self.del_entry()
            self.musika_neud()

        else:
            self.f = 0
            print('OK')


    def go(self):
        if self.f == 1:
            self.destroy()
            self.__init__()

        elif self.f != 1:
            messagebox.showinfo('''ВНИМАНИЕ''', '''Сначала угадайте число''')

        elif self.f == None:
            messagebox.showinfo('''ВНИМАНИЕ''', '''Сначала угадайте число''')

    def del_entry(self):
        self.entry_1.delete(0, last=5)


    def zakrit(self):
        self.destroy()

    def exzit(self):
        choice = messagebox.askyesno("Выход из игры",
                         "Вы действительно хотите\n      выйти из игры?")
        print(choice)
        if choice == True:
            print('Выходим')
            self.zakrit()
        if choice == False:
            print('Остаемся')


    def musika_pob(self):
        playsound('C:\\FOTO  Python\\m-aplodismenty.mp3')

    def musika_neud(self):
        playsound('C:\\FOTO  Python\\m-vozglas-razocharovanie-tolpyi.mp3')



if __name__ == "__main__":
    app = App()
    app.mainloop()
