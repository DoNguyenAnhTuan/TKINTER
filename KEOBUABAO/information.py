from tkinter import *
from PIL import Image, ImageTk



class Information():
    def __init__(self):
        self.window = Toplevel()
        self.window.config(background='HoneyDew')
        self.window.geometry('850x600+100+100')

        self.img = Image.open(r"D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\image\bao.png")
        self.img = self.img.resize((150, 160))
        self.photo = ImageTk.PhotoImage(self.img)
        self.label = Label(self.window, image=self.photo, background='HoneyDew')
        self.label.image = self.photo
        self.label.place(x=180, y=20)

        self.img = Image.open(r"D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\image\bua.png")
        self.img = self.img.resize((150, 160))
        self.photo = ImageTk.PhotoImage(self.img)
        self.label = Label(self.window, image=self.photo, background='HoneyDew')
        self.label.image = self.photo
        self.label.place(x=380, y=20)

        self.img = Image.open(r"D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\image\keo.png")
        self.img = self.img.resize((150, 160))
        self.photo = ImageTk.PhotoImage(self.img)
        self.label = Label(self.window, image=self.photo, background='HoneyDew')
        self.label.image = self.photo
        self.label.place(x=540, y=20)


        self.searchLb = Label(self.window, text='THÔNG TIN CHƯƠNG TRÌNH', font='Calibri 20', width=25, height=1,
                            background='HoneyDew',
                            foreground='black', justify=RIGHT)
        self.searchLb.place(x=270, y=200)

        text = Text(self.window, wrap=WORD, height=10, width=50, bg='HoneyDew', font='Calibri 20', bd=0, fg='black')
        text.insert(INSERT,
                    "Trò chơi Kéo Búa Bao là một trò chơi quen thuộc gắn liền với tuổi thơ của tất cả mọi người"
                    ". Chương trình cho phép đăng nhập, đăng ký và thao tác để chơi trò chơi"
                    "\n\n"
                    "Người xây dựng: Đỗ Nguyễn Anh Tuấn\n"
                    "Ngày thực hiện: 27/05/2023\n"
                    "Số phiên bản: 1.0.0")
        text.place(x=100, y=250)

        self.lineframe = Frame(self.window, height=1, background='white', width=600)
        self.lineframe.place(x=150, y=550)

