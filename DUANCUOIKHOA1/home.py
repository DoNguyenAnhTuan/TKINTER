from tkinter import *


class Home():
    def __init__(self, window):
        self.window = window
        f = open(r'''D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\DUANCUOIKHOA1\danhba.txt''')
        listdata = f.readlines()
        self.datas = []
        for data in listdata:
            data = data.split(',')
            self.datas.append(data)

        index = 0

        self.frame = Frame(self.window, width=50, height=10, background='#191931')
        self.frame.place(x=100, y=420)

        self.Name = StringVar()
        self.Number = StringVar()

        self.nameLb = Label(self.window, text='Tên danh bạ', font='Calibri 14', width=20, height=1, background='#191931',
                            foreground='white', justify=RIGHT)
        self.nameLb.place(x=50, y=50)

        self.nameEn = Entry(self.window, textvariable=self.Name, width=50)
        self.nameEn.config(highlightcolor='white', background='#191931', foreground='white', font='Calibri 14')
        self.nameEn.place(x=250, y=45, height=35)

        self.phoneLb = Label(self.window, text='Số điện thoại', font='Calibri 14', width=20, height=1, background='#191931',
                             foreground='white', justify=RIGHT)
        self.phoneLb.place(x=50, y=120)
        self.phoneEn = Entry(self.window, textvariable=self.Number, width=50)
        self.phoneEn.config(highlightcolor='white', background='#191931', foreground='white', font='Calibri 14')
        self.phoneEn.place(x=250, y=115, height=35)

        self.addressLb = Label(self.window, text='Address', font='Calibri 14', width=20, height=1, background='#191931',
                               foreground='white', justify=RIGHT)
        self.addressLb.place(x=50, y=180)

        self.address = Text(self.window, width=50, height=5, font='Calibri 14', background='#191931', foreground='white')
        self.address.place(x=250, y=180)

        self.addBtn = Button(self.window, text="Thêm mới", font="arial 12 bold", width=18, command=lambda: self.add())
        self.addBtn.place(x=110, y=320)
        self.deleteBtn = Button(self.window, text="Xóa", font="arial 12 bold", width=18, command=lambda: self.delete())
        self.deleteBtn.place(x=335, y=320)
        self.resetBtn = Button(self.window, text="Làm mới", font="arial 12 bold", width=18, command=lambda: self.reset())
        self.resetBtn.place(x=555, y=320)

        self.nameCol = Label(self.window, text='Tên danh bạ', width=20, font='Calibri 15 bold', background='#191931',
                             foreground='white')
        self.nameCol.place(x=110, y=370)
        self.phoneCol = Label(self.window, text='Số điện thoại', width=20, font='Calibri 15 bold', background='#191931',
                              foreground='white')
        self.phoneCol.place(x=325, y=370)
        self.addressCol = Label(self.window, text='Đia chỉ', width=20, font='Calibri 15 bold', background='#191931',
                                foreground='white')
        self.addressCol.place(x=545, y=370)



        self.update_book()

    # Add Information
    def add(self):
        self.datas.append([self.Name.get(), self.Number.get(), self.address.get(1.0, "end-1c")])
        f = open('danhba.txt', 'a+')
        f.write(self.Name.get() + ',' + self.Number.get() + ',' + self.address.get(1.0, "end-1c") + '\n')
        f.close()
        self.update_book()

    # View Information

    # Delete Information
    def delete(self):
        print("Đây")
        self.phone = self.phoneEn.get()
        print(self.phone)
        row = 0
        currentdata = -1
        for data in self.datas:
            print("data", data[1])
            if data[1] == self.phone:
                currentdata = row
                break
            row += 1
        del self.datas[currentdata]
        print(self.datas)
        print(currentdata)
        f = open("danhba.txt", "r+")
        data = f.readlines()
        f.seek(0)
        dem = 0
        for line in data:
            if int(currentdata) != dem:
                f.write(line)
            dem += 1
        f.truncate()
        f.close()
        self.update_book()

    def reset(self):
        self.Name.set('')
        self.Number.set('')
        self.address.delete(1.0, "end")

    def which_button(self, button_press):
        # Printing the text when a button is clicked
        index = button_press[1]
        self.Name.set(self.datas[index][0])
        self.Number.set(self.datas[index][1])
        self.address.delete(1.0, "end")
        self.address.insert(1.0, self.datas[index][2])

    # Update Information
    def update_book(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()
        for x in range(3):
            for y in range(len(self.datas)):
                if x == 2:
                    text = self.datas[y][x].split('\n')
                    text = text[0]
                else:
                    text = self.datas[y][x]
                btn = Button(self.frame, text=text, width=20, font='Calibri 14', background='#191931',
                             foreground='white', command=lambda m=[x, y]: self.which_button(m)).grid(row=y, column=x,
                                                                                                     padx=5, pady=5,
                                                                                                     sticky=N + S + E + W)



