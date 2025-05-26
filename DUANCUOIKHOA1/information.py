from tkinter import *
from PIL import Image, ImageTk



class Information():
    def __init__(self, window):
        self.window = window
        self.img = Image.open(r"D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\DUANCUOIKHOA1\image\phone-call-icon.png")
        self.img = self.img.resize((150, 160))

        self.photo = ImageTk.PhotoImage(self.img)

        self.label = Label(self.window, image=self.photo, background='#191931')
        self.label.image = self.photo
        self.label.place(x=360, y=20)


        self.searchLb = Label(self.window, text='THÔNG TIN CHƯƠNG TRÌNH', font='Calibri 20', width=25, height=1,
                            background='#191931',
                            foreground='white', justify=RIGHT)
        self.searchLb.place(x=270, y=200)

        text = Text(window, wrap=WORD, height=10, width=50, bg='#191931', font='Calibri 20', bd=0, fg='white')
        text.insert(INSERT,
                    "Ứng dụng quản lý danh bạ giúp người dùng có thể lưu trữ thông tin danh bạ,"
                    "thêm, xóa, sửa dữ liệu mới, xem thông tin danh bạ và nhiều hơn thế nữa..."
                    "\n\n"
                    "Người xây dựng: Nguyễn Minh Thông\n"
                    "Ngày thực hiện: 05/10/2022\n"
                    "Số phiên bản: 1.0.0")
        text.place(x=100, y=250)

        self.lineframe = Frame(self.window, height=1, background='white', width=600)
        self.lineframe.place(x=150, y=550)

