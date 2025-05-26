from tkinter import *
from PIL import Image, ImageTk



class Search():
    def __init__(self, window):
        self.window = window
        f = open('danhba.txt', 'r')
        listdata = f.readlines()
        self.datas = []
        for data in listdata:
            data = data.split(',')
            self.datas.append(data)
        self.img = Image.open('image\\search.png')
        self.img = self.img.resize((150, 160))

        self.photo = ImageTk.PhotoImage(self.img)

        self.label = Label(self.window, image=self.photo, background='#191931')
        self.label.image = self.photo
        self.label.place(x=360, y=20)


        self.searchLb = Label(self.window, text='NHẬP NỘI DUNG TÌM KIẾM', font='Calibri 20', width=25, height=1,
                            background='#191931',
                            foreground='white', justify=RIGHT)
        self.searchLb.place(x=270, y=200)

        self.nameEn = Entry(self.window, width=45)
        self.nameEn.config(highlightcolor='white', background='#191931', foreground='white', font='Calibri 14')
        self.nameEn.place(x=100, y=250, height=35)
        self.btn = Button(self.window, text='Tìm kiếm', width=15, font='Calibri 14', background='#191931',
                     foreground='white', height=1, command= lambda : self.search())
        self.btn.place(x=590, y=250)
        self.frame = Frame(self.window, width=50, height=10, background='#191931')
        self.frame.place(x=100, y=530)

    def search(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()
        text = self.nameEn.get()
        text = text.lower()
        row = 0
        result = []
        for data in self.datas:
            if data[0].lower() == text or data[1].lower() == text or data[2].lower() == text:
                result.append(data)
        if len(result) > 0:

            self.resultLb = Label(self.window, text='KẾT QUẢ TÌM KIẾM', font='Calibri 20', width=25, height=1,
                                  background='#191931',
                                  foreground='white', justify=RIGHT)
            self.resultLb.place(x=270, y=450)


            self.nameCol = Label(self.window, text='Tên danh bạ', width=20, font='Calibri 15 bold',
                                 background='#191931',
                                 foreground='white')
            self.nameCol.place(x=110, y=500)
            self.phoneCol = Label(self.window, text='Số điện thoại', width=20, font='Calibri 15 bold',
                                  background='#191931',
                                  foreground='white')
            self.phoneCol.place(x=325, y=500)
            self.addressCol = Label(self.window, text='Đia chỉ', width=20, font='Calibri 15 bold', background='#191931',
                                    foreground='white')
            self.addressCol.place(x=545, y=500)

            for widgets in self.frame.winfo_children():
                widgets.destroy()
            for x in range(3):
                for y in range(len(result)):
                    if x == 2:
                        text = result[y][x].split('\n')
                        text = text[0]
                    else:
                        text = result[y][x]
                    btn = Button(self.frame, text=text, width=20, font='Calibri 14', background='#191931',
                                 foreground='white', ).grid(row=y, column=x,padx=5, pady=5,sticky=N + S + E + W)
        else:
            self.resultLb = Label(self.window, text='không tìm thấy kết quả:((', font='Calibri 20', width=25, height=1,
                                  background='#191931',
                                  foreground='white', justify=RIGHT)
            self.resultLb.place(x=270, y=450)
