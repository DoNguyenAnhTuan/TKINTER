from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk


class SignUp():
    def __init__(self):
        self.window = Tk()
        self.window.config(bg='AliceBlue')
        self.window.title('Màn hình đăng ký')
        self.window.geometry('700x600+100+100')
        self.label = Label(self.window, text='Đăng ký', font=('Tahoma', 16, 'bold'), bg='AliceBlue')
        self.label.place(x=480, y=20)

        self.img = Image.open('image\\popup-banner.jpg')
        self.img = self.img.resize((350, 600))

        self.photo = ImageTk.PhotoImage(self.img)

        self.label = Label(image=self.photo)
        self.label.image = self.photo
        self.label.place(x=0, y=0)

        self.icon = Image.open('image\\newuser.png')
        self.icon = self.icon.resize((20, 20))

        self.photo1 = ImageTk.PhotoImage(self.icon)

        self.label1 = Label(bg='AliceBlue', image=self.photo1)
        self.label1.place(x=450, y=25)

        self.userNamelabel = Label(self.window, text='Họ và tên',
             font=('Verdana', 13), bg='AliceBlue')
        self.userNamelabel.place(x=480, y=70)

        self.userNameInput = Entry(self.window, width=22, bd=2,
             font=('Verdana', 13))
        self.userNameInput.place(x=400, y=110)

        self.emaillabel = Label(self.window, text='Địa chỉ email',
             font=('Verdana', 13), bg='AliceBlue')
        self.emaillabel.place(x=470, y=140)

        self.emailNameInput = Entry(self.window, width=22, bd=2,
             font=('Verdana', 13))
        self.emailNameInput.place(x=400, y=170)

        self.phonelabel = Label(self.window, text='Số điện thoại', font=('Verdana', 13), bg='AliceBlue')
        self.phonelabel.place(x=470, y=200)

        self.phoneInput = Entry(self.window, width=22, bd=2, font=('Verdana', 13))
        self.phoneInput.place(x=400, y=230)

        self.addresslabel = Label(self.window, text='Quê quán', font=('Verdana', 13), bg='AliceBlue')

        self.addresslabel.place(x=480, y=260)

        self.comBobox = ttk.Combobox(self.window, width=20, font=('Verdana', 13))
        self.comBobox['values'] = ('Chọn quê quán', 'Bình Dương', 'Bình Phước', 'Tây Ninh', 'Đồng Nai')
        self.comBobox.current(0)
        self.comBobox.place(x=400, y=290)

        self.passwordlabel = Label(self.window, text='Mật khẩu', font=('Verdana', 13), bg='AliceBlue')
        self.passwordlabel.place(x=480, y=330)
        self.pwdInput = Entry(self.window, bd=2, width=22, font=('Verdana', 13), show="*")
        self.pwdInput.place(x=400, y=360)

        self.repasswordlabel = Label(self.window, text='Nhập lại mật khẩu', font=('Verdana', 13), bg='AliceBlue')
        self.repasswordlabel.place(x=450, y=390)
        self.repwdInput = Entry(self.window, bd=2, width=22, font=('Verdana', 13), show="*")
        self.repwdInput.place(x=400, y=420)

        self.buttonSignup = Button(self.window, text='Đăng ký', width=20, relief='solid', font=('Verdana', 13, 'bold'),
                                   fg='white', bg='MediumSeaGreen', height=1, bd=1, command=lambda: self.thongbao())
        self.buttonSignup.place(x=400, y=470)

        self.noacclabel = Label(self.window, text='Đã có tài khoản?', font=('Verdana', 13), bg='AliceBlue')
        self.noacclabel.place(x=450, y=510)
        self.signupbtn = Button(self.window, text='Đăng nhập', font=('Verdana', 13, 'bold'), width=20, relief='solid',
                                fg='SeaGreen', bg='AliceBlue', command=lambda: self.login())
        self.signupbtn.place(x=400, y=540)

        self.window.mainloop()

    def thongbao(self):
        len_pwd = len(self.pwdInput.get().strip())
        if self.userNameInput.get().strip() == '':
            messagebox.showinfo('Thông báo', 'Tên đăng nhập không được bỏ trống')
        elif self.emailNameInput.get().strip() == '':
            messagebox.showinfo('Thông báo', 'Địa chỉ email không được bỏ trống')
        elif self.comBobox.get().strip() == 'Chọn quê quán':
            messagebox.showinfo('Thông báo', 'Quê quán không được bỏ trống')
        elif self.pwdInput.get().strip() == '':
            messagebox.showinfo('Thông báo', 'Mật khẩu không được bỏ trống')
        elif self.phoneInput.get().strip() == '':
            messagebox.showinfo('Thông báo', 'Số điện thoại không được bỏ trống')
        elif len_pwd < 8:
            messagebox.showinfo('Thông báo', 'Mật khẩu phải có độ dài tối thiểu 8 ký tự')
        elif self.pwdInput.get().strip() != self.repwdInput.get().strip():
            messagebox.showinfo('Thông báo', 'Mật khẩu nhập lại không chính xác')
        else:
            f = open('user.txt', 'a+')
            strData = str(self.userNameInput.get().strip()) + ',' + str(self.emailNameInput.get().strip()) + ',' + str(
                self.comBobox.get().strip()) + ',' + str(self.phoneInput.get().strip()) + ',' + str(self.pwdInput.get().strip()) + '\n'
            f.write(strData)
            messagebox.showinfo('Thông báo', 'Đăng ký thành công')
            self.window.destroy()
            self.LoginWn.loginSc()

    def login(self):
        self.window.destroy()
        self.LoginWn.loginSc()
SignUp()