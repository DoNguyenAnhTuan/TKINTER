from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox



class Account():
    def __init__(self, currentUser):
        self.window = Toplevel()
        self.window.config(background='HoneyDew')
        self.window.geometry('850x700+100+100')

        self.currentUser = currentUser[0]
        self.img = Image.open('image\\user.png')
        self.img = self.img.resize((90, 95))
        self.photo = ImageTk.PhotoImage(self.img)
        self.label = Label(self.window, image=self.photo, background='HoneyDew')
        self.label.image = self.photo
        self.label.place(x=390, y=20)


        self.accLb = Label(self.window, text='TÀI KHOẢN', font='Calibri 20', width=20, height=1,
                            background='HoneyDew',
                            foreground='black', justify=RIGHT)
        self.accLb.place(x=295, y=140)

        self.nameLb = Label(self.window, text='Tài khoản', font='Calibri 16', width=20, height=1,
                            background='HoneyDew',
                            foreground='black', justify=RIGHT)
        self.nameLb.place(x=150, y=200)

        self.lineframe = Frame(self.window, height=1, background='white', width=600)
        self.lineframe.place(x=150, y=250)

        self.nameconEn = Entry(self.window,  font='Calibri 16', width=30,
                            background='HoneyDew',
                            foreground='black', justify=CENTER)
        self.nameconEn.insert(0, self.currentUser[0])
        self.nameconEn.place(x=400, y=200)

        self.lineframe2 = Frame(self.window, height=1, background='white', width=600)
        self.lineframe2.place(x=150, y=350)

        self.phoneLb = Label(self.window, text='Số điện thoại', font='Calibri 16', width=20, height=1,
                            background='HoneyDew',
                            foreground='black', justify=RIGHT)
        self.phoneLb.place(x=150, y=300)

        self.phoneconEn = Entry(self.window, font='Calibri 16', width=30,
                            background='HoneyDew',
                            foreground='black', justify=CENTER)
        self.phoneconEn.insert(0, self.currentUser[3])
        self.phoneconEn.place(x=400, y=300)

        self.lineframe3 = Frame(self.window, height=1, background='white', width=600)
        self.lineframe3.place(x=150, y=450)

        self.emailLb = Label(self.window, text='Email', font='Calibri 16', width=20, height=1,
                            background='HoneyDew',
                            foreground='black', justify=RIGHT)
        self.emailLb.place(x=150, y=400)

        self.emailEn = Entry(self.window,  font='Calibri 16', width=30,
                            background='HoneyDew',
                            foreground='black', justify=CENTER)
        self.emailEn.insert(0, self.currentUser[1])
        self.emailEn.place(x=400, y=400)

        self.addressLb = Label(self.window, text='Địa chỉ', font='Calibri 16', width=20, height=1,
                            background='HoneyDew',
                            foreground='black', justify=RIGHT)
        self.addressLb.place(x=150, y=500)

        self.addressconEn = Entry(self.window,  font='Calibri 16', width=30,
                            background='HoneyDew',
                            foreground='black', justify=CENTER)
        self.addressconEn.insert(0, self.currentUser[2])
        self.addressconEn.place(x=400, y=500)

        self.lineframe4 = Frame(self.window, height=1, background='black', width=600)
        self.lineframe4.place(x=150, y=550)

        self.SignOutBtn = Button(self.window, text='ĐĂNG XUẤT', width=15, font='Calibri 14', background='#191931',
                          foreground='white', height=1, command=lambda: self.window.quit())
        self.SignOutBtn.place(x=380, y=600)

