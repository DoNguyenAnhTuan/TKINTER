from tkinter import *
from tkinter import messagebox

from main import Main
from signup import SignUp


class Login():
    def __init__(self):
        self.window = Tk()
        self.window.config(bg='AliceBlue')
        self.window.title('Màn hình login')
        self.window.geometry('380x300+100+100')

        f = open(r'''D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\user.txt''')
      
        listdata = f.readlines()
        self.datas = []
        for data in listdata:
            data = data.split(',')
            self.datas.append(data)

        self.label = Label(self.window, text='Đăng nhập', font=('Tahoma', 16, 'bold'), bg='AliceBlue')
        self.label.place(x=140, y=20)

        self.userNamelabel = Label(self.window, text='Số điện thoại', font=('Verdana', 13), bg='AliceBlue')
        self.userNamelabel.place(x=13, y=70)

        self.userNameInput = Entry(self.window, bd=2, width=17, font=('Verdana', 13))
        self.userNameInput.place(x=160, y=70)
        self.userNameInput.insert(0, '0392969357')

        self.passwordlabel = Label(self.window, text='Mật khẩu', font=('Verdana', 13), bg='AliceBlue')
        self.passwordlabel.place(x=13, y=120)
        self.pwdInput = Entry(self.window, bd=2, show="*", width=17, font=('Verdana', 13))
        self.pwdInput.insert(0, '12345678')
        self.pwdInput.place(x=160, y=120)

        self.buttonLogin = Button(self.window, text='Đăng nhập', width=28, relief='solid', font=('Verdana', 13, 'bold'),
                                  fg='white', bg='MediumSeaGreen', height=1, bd=1, command=lambda: self.thongbao())
        self.buttonLogin.place(x=13, y=160)

        self.noacclabel = Label(self.window, text='Chưa có tài khoản?', font=('Verdana', 13), bg='AliceBlue')
        self.noacclabel.place(x=110, y=210)
        self.signuplabel = Button(self.window, text='Đăng ký', width=28, relief='solid', font=('Verdana', 13, 'bold'),
                                  fg='SeaGreen', bg='AliceBlue', command=lambda : self.signUp())
        self.signuplabel.place(x=13, y=250)
        self.window.mainloop()

    def signUp(self):
        self.window.destroy()
        SignUp(self)

    def thongbao(self):
        status = False
        if self.userNameInput.get() == '':
            messagebox.showinfo('Thông báo', 'Số điện thoại không được bỏ trống')
        elif self.pwdInput.get() == '':
            messagebox.showinfo('Thông báo', 'Mật khẩu không được bỏ trống')
        else:
            for data in self.datas:
                pwd = data[4].split('\n')
                pwd = pwd[0]
                if str(data[3]) == str(self.userNameInput.get()) and str(pwd) == str(self.pwdInput.get()):
                    status = True

            if status == True:
                self.window.quit()
                Main(self.userNameInput.get())
            else:
                messagebox.showinfo('Thông báo', 'Số điện thoại hoặc mật khẩu không chính xác')
    def loginSc(self):
        self.window = Tk()
        self.window.config(bg='AliceBlue')
        self.window.title('Màn hình login')
        self.window.geometry('380x300+100+100')

        f = open(r'''D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\user.txt''')
        listdata = f.readlines()
        self.datas = []
        for data in listdata:
            data = data.split(',')
            self.datas.append(data)

        self.label = Label(self.window, text='Đăng nhập', font=('Tahoma', 16, 'bold'), bg='AliceBlue')
        self.label.place(x=140, y=20)

        self.userNamelabel = Label(self.window, text='Số điện thoại', font=('Verdana', 13), bg='AliceBlue')
        self.userNamelabel.place(x=13, y=70)

        self.userNameInput = Entry(self.window, bd=2, width=17, font=('Verdana', 13))
        self.userNameInput.place(x=160, y=70)

        self.passwordlabel = Label(self.window, text='Mật khẩu', font=('Verdana', 13), bg='AliceBlue')
        self.passwordlabel.place(x=13, y=120)
        self.pwdInput = Entry(self.window, bd=2, show="*", width=17, font=('Verdana', 13))
        self.pwdInput.place(x=160, y=120)

        self.buttonLogin = Button(self.window, text='Đăng nhập', width=28, relief='solid', font=('Verdana', 13, 'bold'),
                                  fg='white', bg='MediumSeaGreen', height=1, bd=1, command=lambda: self.thongbao())
        self.buttonLogin.place(x=13, y=160)

        self.noacclabel = Label(self.window, text='Chưa có tài khoản?', font=('Verdana', 13), bg='AliceBlue')
        self.noacclabel.place(x=110, y=210)
        self.signuplabel = Button(self.window, text='Đăng ký', width=28, relief='solid', font=('Verdana', 13, 'bold'),
                                  fg='SeaGreen', bg='AliceBlue', command=lambda: self.signUp())
        self.signuplabel.place(x=13, y=250)
        self.window.mainloop()
Login()