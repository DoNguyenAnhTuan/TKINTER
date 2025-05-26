from tkinter import *

from account import Account
from information import Information



class MenuMain():
    def __init__(self, root, frame, phone):
        self.root = root
        self.frame = frame
        self.phone = phone
        menuBar = Menu(self.root)
        self.root.config(menu=menuBar)

        f = open(r'''D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\user.txt''')
        listdata = f.readlines()
        self.datas = []
        for data in listdata:
            data = data.split(',')
            self.datas.append(data)

        # Tạo menu trang chủ
        home = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='Trang chủ', menu=home)

        # Tạo menu con trong trang chủ
        home.add_command(label='Tài khoản', command= lambda : self.account())
        home.add_command(label='Thoát', command= lambda :self.Close())
        # ---------------------------------------

        # Tạo menu tùy chọn
        home = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='Tùy chọn', menu=home)

        # Tạo menu con trong con trong tùy chọn
        home.add_command(label='Tìm kiếm danh bạ', command=lambda : self.search())
        home.add_command(label='Danh sách danh bạ', command=lambda : self.showdata())
        # ---------------------------------------

        # Tạo menu thông tin
        infomation = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='Thông tin', menu=infomation)
        infomation.add_command(label='Thông tin ứng dụng',command=lambda : self.information())
    def Close(self):
        self.root.quit()

    def account(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

        currentuser = []
        for data in self.datas:
            if data[3] == self.phone:
                currentuser.append(data)
                break
        account = Account(self.frame, currentuser)

    def search(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()


        search = Search(self.frame)

    def showdata(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()
        home = Home(self.frame)

    def information(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()
        home = Information(self.frame)
