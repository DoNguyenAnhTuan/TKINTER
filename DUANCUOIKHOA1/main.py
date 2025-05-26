from tkinter import *
from home import Home
from menu import MenuMain
class Main():
    def __init__(self, phone):
        self.window = Toplevel()
        self.window.geometry('850x800+100+100')
        self.window.title('Phần mềm quản lý...')
        self.phone = phone
        self.frame = Frame(self.window, width=850, height=800, background='#191931')
        self.frame.place(x=0, y=0)


        self.menu = MenuMain(self.window, self.frame, self.phone)
        self.home = Home(self.frame)

        self.window.mainloop()