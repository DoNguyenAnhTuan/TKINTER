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

        self.img = Image.open('image\\color1.png')
        self.img = self.img.resize((160, 165))
        self.photo = ImageTk.PhotoImage(self.img)
        self.label = Label(self.window, image=self.photo, background='HoneyDew')
        self.label.image = self.photo
        self.label.place(x=20, y=80)

        text = Text(self.window, wrap=WORD, height=10, width=45, bg='HoneyDew', font='Calibri 20', bd=0, fg='black')
        text.insert(INSERT,
                    '''Danh sách các màu sắc trong trò chơi: "Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink",
                  "Magenta"''')
        text.place(x=200, y=90)

        self.img1 = Image.open('image\\color2.jpg')
        self.img1 = self.img1.resize((160, 165))
        self.photo1 = ImageTk.PhotoImage(self.img1)
        self.label1 = Label(self.window, image=self.photo1, background='HoneyDew')
        self.label1.image = self.photo1
        self.label1.place(x=650, y=300)

        text = Text(self.window, wrap=WORD, height=10, width=45, bg='HoneyDew', font='Calibri 20', bd=0, fg='black')
        text.insert(INSERT,
                    """Để bắt đầu trò chơi, hãy nhấn vào nút bắt đầu, thời gian sẽ đếm ngược từ 60 giây về 0. Trong khoảng thời gian này, hãy trả lời thật nhiều đáp án nhất có thể""")
        text.place(x=20, y=320)

        self.img2 = Image.open('image\\color3.png')
        self.img2 = self.img2.resize((160, 165))
        self.photo2 = ImageTk.PhotoImage(self.img2)
        self.label2 = Label(self.window, image=self.photo2, background='HoneyDew')
        self.label2.image = self.photo2
        self.label2.place(x=20, y=520)

        text = Text(self.window, wrap=WORD, height=10, width=45, bg='HoneyDew', font='Calibri 20', bd=0, fg='black')
        text.insert(INSERT,
                    """Lưu ý rằng, hãy trả lời theo màu sắc của của chữ đang hiển thị, đừng trả lời theo nội dung của chữ nhé. Để bắt đầu màn chơi mới, nhấn vào nút đặt lại bên phải""")
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
