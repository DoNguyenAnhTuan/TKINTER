from tkinter import *
from PIL import Image, ImageTk


class Guide():
    def __init__(self):
        self.window = Toplevel()
        self.window.config(background='HoneyDew')
        self.window.geometry('850x700+100+100')

        self.guideLb = Label(self.window, text='HƯỚNG DẪN TRÒ CHƠI', font='Calibri 20', width=25, height=1,
                             background='HoneyDew',
                             foreground='black', justify=RIGHT)
        self.guideLb.place(x=270, y=20)

        self.img = Image.open(r"D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\image\keo.png")
        self.img = self.img.resize((150, 165))
        self.photo = ImageTk.PhotoImage(self.img)
        self.label = Label(self.window, image=self.photo, background='HoneyDew')
        self.label.image = self.photo
        self.label.place(x=20, y=80)

        text = Text(self.window, wrap=WORD, height=10, width=45, bg='HoneyDew', font='Calibri 20', bd=0, fg='black')
        text.insert(INSERT,
                    """Trò chơi gồm 3 phần:\n- Phần thông báo trạng thái thắng thu\n- Phần chọn báo búa bao của người chơi\n- Phần hiểm thị thông tin chi tiết""")
        text.place(x=200, y=90)

        self.img1 = Image.open(r"D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\image\bua.png")
        self.img1 = self.img1.resize((150, 165))
        self.photo1 = ImageTk.PhotoImage(self.img1)
        self.label1 = Label(self.window, image=self.photo1, background='HoneyDew')
        self.label1.image = self.photo1
        self.label1.place(x=650, y=300)

        text = Text(self.window, wrap=WORD, height=10, width=45, bg='HoneyDew', font='Calibri 20', bd=0, fg='black')
        text.insert(INSERT,
                    """Người chơi bắt đầu bằng việc lựa chọn: kéo, búa hoặc bao. Sau khi chọn, máy sẽ chọn ngẫu nhiên một trong 3 loại trên và dựa theo nguyên tắc của kéo búa bao để phân định ván chơi""")
        text.place(x=20, y=320)

        self.img2 = Image.open(r"D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\image\bao.png")
        self.img2 = self.img2.resize((150, 165))
        self.photo2 = ImageTk.PhotoImage(self.img2)
        self.label2 = Label(self.window, image=self.photo2, background='HoneyDew')
        self.label2.image = self.photo2
        self.label2.place(x=20, y=520)

        text = Text(self.window, wrap=WORD, height=10, width=45, bg='HoneyDew', font='Calibri 20', bd=0, fg='black')
        text.insert(INSERT,
                    """Nếu người chơi thắng, điểm người chơi sẽ được +1. Nếu máy thắng, điểm của máy sẽ được +1. Nếu hòa, điểm của cả 2 sẽ được giữ nguyên""")
        text.place(x=200, y=550)
        # self.img = Image.open('image\\bua.png')
        # self.img = self.img.resize((150, 160))
        # self.photo = ImageTk.PhotoImage(self.img)
        # self.label = Label(self.window, image=self.photo, background='HoneyDew')
        # self.label.image = self.photo
        # self.label.place(x=380, y=20)
        #
        # self.img = Image.open('image\\bao.png')
        # self.img = self.img.resize((150, 160))
        # self.photo = ImageTk.PhotoImage(self.img)
        # self.label = Label(self.window, image=self.photo, background='HoneyDew')
        # self.label.image = self.photo
        # self.label.place(x=540, y=20)
        #
        #
        # self.searchLb = Label(self.window, text='THÔNG TIN CHƯƠNG TRÌNH', font='Calibri 20', width=25, height=1,
        #                     background='HoneyDew',
        #                     foreground='black', justify=RIGHT)
        # self.searchLb.place(x=270, y=200)

        self.lineframe = Frame(self.window, height=1, background='white', width=600)
        self.lineframe.place(x=150, y=550)
