from tkinter import *
import tkinter.font as font
import random
from PIL import Image, ImageTk

from LV3_TKINTER.DOANMAU.account import Account
from LV3_TKINTER.DOANMAU.guide import Guide
from LV3_TKINTER.DOANMAU.information import Information


class Main():
    def __init__(self, phone):
        self.phone = phone

        f = open('user.txt', 'r')
        listdata = f.readlines()
        self.datas = []
        for data in listdata:
            data = data.split(',')
            self.datas.append(data)

        self.currentuser = []
        for data in self.datas:
            if data[3] == self.phone:
                self.currentuser.append(data)
                break

        self.colors = ["Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink", "Magenta"]

        self.timer = 60
        self.score = 0
        self.displayed_word_color = ''

        self.my_window = Toplevel()
        self.my_window.title("Tinh mắt nhanh tay")
        self.my_window.geometry("700x700+100+100")

        self.app_font = font.Font(family='Helvetica', size=15)

        self.GuideBtn = Button(self.my_window, text='HƯỚNG DẪN', width=15, font='Calibri 14', background='#191931',
                                 foreground='white', height=1, command=lambda : Guide())
        self.GuideBtn.place(x=80, y=20)

        self.InfoBtn = Button(self.my_window, text='THÔNG TIN', width=15, font='Calibri 14', background='#191931',
                                 foreground='white', height=1, command=lambda : Information())
        self.InfoBtn.place(x=280, y=20)

        self.AccountBtn = Button(self.my_window, text='TÀI KHOẢN', width=15, font='Calibri 14', background='#191931',
                                 foreground='white', height=1, command=lambda : Account(self.currentuser))
        self.AccountBtn.place(x=480, y=20)


        self.game_desp = "Bạn có 60 giây cho mỗi màn chơi, nhấn bắt đầu khi đã sẵn sàng nhé"
        self.myFont = font.Font(family='Helvetica')

        self.game_description = Label(self.my_window, text=self.game_desp, font=self.app_font, fg="black")
        self.game_description.place(x=45, y=80)

        self.game_score = Label(self.my_window, text="Điểm số của bạn : " + str(self.score), font=(font.Font(size=16)), fg="green")
        self.game_score.place(x=280, y=120)

        self.display_words = Label(self.my_window, font=(font.Font(size=60)), pady=10, justify=CENTER)
        self.display_words.place(x=250, y=200)

        self.time_left = Label(self.my_window, text="Màn chơi kết thúc trong : -", font=(font.Font(size=14)), fg="orange")
        self.time_left.place(x=260, y=400)

        self.color_entry = Entry(self.my_window, width=30, font='Calibri 20')
        self.color_entry.place(x=150, y=450)

        self.btn_frame = Frame(self.my_window,width=80, height=40, bg='red')
        self.btn_frame.pack(side=BOTTOM)

        self.start_button = Button(self.btn_frame, font='Calibri 20', text="BẮT ĐẦU", width=20, fg="black", bg="pink", bd=0, padx=20, pady=10,
                              command=self.startGame)
        self.start_button.grid(row=0, column=0)

        self.reset_button = Button(self.btn_frame, font='Calibri 20', text="ĐẶT LẠI", width=20, fg="black", bg="light blue", bd=0, padx=20, pady=10,
                              command=self.resetGame)
        self.reset_button.grid(row=0, column=1)

        self.my_window.mainloop()

    #This fuction will be called when start button is clicked
    def startGame(self):
        if(self.timer == 60):
            self.startCountDown()
            self.displayed_word_color = random.choice(self.colors).lower()
            self.display_words.config(text=random.choice(self.colors), fg=self.displayed_word_color)
            self.color_entry.bind('<Return>', self.displayNextWord)

    #This function is to reset the game
    def resetGame(self):
        self.timer = 60
        self.score = 0
        self.displayed_word_color = ''
        self.game_score.config(text = "Điểm số của bạn : " + str(self.score))
        self.display_words.config(text = '')
        self.time_left.config(text="Màn chơi kết thúc trong : -")
        self.color_entry.delete(0, END)

    #This function will start count down
    def startCountDown(self):
        if(self.timer >= 0):
            self.time_left.config(text = "Màn chơi kết thúc trong : " + str(self.timer) + "s")
            self.timer -= 1
            self.time_left.after(1000,self.startCountDown)
            if (self.timer == -1):
                self.time_left.config(text="Ván chơi kết thúc!!!")

    #This function to display random words
    def displayNextWord(self, event):
        if(self.timer > 0):
            if(self.displayed_word_color == self.color_entry.get().lower()):
                self.score += 1
                self.game_score.config(text = "Điểm số của bạn : " + str(self.score))
            self.color_entry.delete(0, END)
            self.displayed_word_color = random.choice(self.colors).lower()
            self.display_words.config(text = random.choice(self.colors), fg = self.displayed_word_color)
