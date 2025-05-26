from tkinter import *
import tkinter.font as font
import random
from PIL import Image, ImageTk

from account import Account
from guide import Guide
from information import Information


class Main():
    def __init__(self, phone):
        self.phone = phone

        f = open(r'''D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\user.txt''')
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

        self.player_score = 0
        self.computer_score = 0
        self.options = [('Búa',0), ('Bao',1), ('Kéo',2)]

        self.game_window = Toplevel()
        self.game_window.title("Trò chơi Kéo Búa Bao")
        self.game_window.config(background='HoneyDew')

        self.app_font = font.Font(size=13)

        # Displaying Game Title
        self.game_title = Label(self.game_window, text='KÉO BÚA BAO', font=font.Font(size=20), fg='Black', background='HoneyDew')
        self.game_title.place(x=350, y=30)

        # Label to dispay, who wins each time
        self.winner_label = Label(self.game_window, text="Cùng bắt đầu game nào...!!", fg='green', font=font.Font(size=15), pady=8,
                             background='HoneyDew', width=40)
        self.winner_label.place(x=220, y=80)

        self.input_frame = Frame(self.game_window, background='HoneyDew')
        self.input_frame.place(x=50, y=130)

        # Displaying player options
        self.player_options = Label(self.input_frame, text="Lựa chọn của bạn : ", font=font.Font(size=15), fg='grey',
                               background='HoneyDew')
        self.player_options.grid(row=0, column=0, pady=8)

        self.rock_btn = Button(self.input_frame, text='Búa', width=15, bd=0, font=font.Font(size=15), bg='pink', pady=5,
                          command=lambda: self.player_choice(self.options[0]))
        self.rock_btn.grid(row=1, column=1, padx=8, pady=5)

        self.paper_btn = Button(self.input_frame, text='Bao', width=15, bd=0, font=font.Font(size=15), bg='silver', pady=5,
                           command=lambda: self.player_choice(self.options[1]))
        self.paper_btn.grid(row=1, column=2, padx=8, pady=5)

        self.scissors_btn = Button(self.input_frame, text='Kéo', width=15, bd=0, font=font.Font(size=15), bg='light blue', pady=5,
                              command=lambda: self.player_choice(self.options[2]))
        self.scissors_btn.grid(row=1, column=3, padx=8, pady=5)

        # Displaying Score and players choise
        self.score_label = Label(self.input_frame, text='Điểm số : ', font=font.Font(size=15), fg='grey', background='HoneyDew')
        self.score_label.grid(row=2, column=0)

        self.player_choice_label = Label(self.input_frame, text='Bạn đã chọn : ---', font=font.Font(size=15), background='HoneyDew')
        self.player_choice_label.grid(row=3, column=1, pady=5)

        self.player_score_label = Label(self.input_frame, text='Điểm của bạn : -', font=font.Font(size=15), background='HoneyDew')
        self.player_score_label.grid(row=3, column=2, pady=5)

        self.computer_choice_label = Label(self.input_frame, text='Máy tính đã chọn : ---', font=font.Font(size=15), fg='black',
                                      background='HoneyDew')
        self.computer_choice_label.grid(row=4, column=1, pady=5)

        self.computer_score_label = Label(self.input_frame, text='Điểm của máy : -', font=font.Font(size=15), fg='black',
                                     background='HoneyDew')
        self.computer_score_label.grid(row=4, column=2, padx=(10, 0), pady=5)

        self.img = Image.open(r"D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\image\keo.png")
        self.img = self.img.resize((90, 95))
        self.photo = ImageTk.PhotoImage(self.img)
        self.label = Label(self.game_window, image=self.photo, background='#191931', borderwidth=0)
        self.label.image = self.photo
        self.label.place(x=390, y=400)

        self.img = Image.open(r"D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\image\bua.png")
        self.img = self.img.resize((90, 95))
        self.photo = ImageTk.PhotoImage(self.img)
        self.label = Label(self.game_window, image=self.photo, background='#191931', borderwidth=0)
        self.label.image = self.photo
        self.label.place(x=280, y=400)

        self.img = Image.open(r"D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\KEOBUABAO\image\bao.png")
        self.img = self.img.resize((90, 95))
        self.photo = ImageTk.PhotoImage(self.img)
        self.label = Label(self.game_window, image=self.photo, background='#191931', borderwidth=0)
        self.label.image = self.photo
        self.label.place(x=500, y=400)

        self.GuideBtn = Button(self.game_window, text='HƯỚNG DẪN', width=15, font='Calibri 14', background='#191931',
                                 foreground='white', height=1, command=lambda : Guide())
        self.GuideBtn.place(x=150, y=600)

        self.InfoBtn = Button(self.game_window, text='THÔNG TIN', width=15, font='Calibri 14', background='#191931',
                                 foreground='white', height=1, command=lambda : Information())
        self.InfoBtn.place(x=350, y=600)

        self.AccountBtn = Button(self.game_window, text='TÀI KHOẢN', width=15, font='Calibri 14', background='#191931',
                                 foreground='white', height=1, command=lambda : Account(self.currentuser))
        self.AccountBtn.place(x=550, y=600)

        self.game_window.geometry('850x700')
        self.game_window.mainloop()

    def player_choice(self, player_input):

        self.computer_input = self.get_computer_choice()

        self.player_choice_label.config(text = 'Bạn đã chọn: ' + player_input[0])
        self.computer_choice_label.config(text = 'Máy đã chọn: ' + self.computer_input[0])

        if(player_input == self.computer_input):
            self.winner_label.config(text = "Hòa")
        elif((player_input[1] - self.computer_input[1]) % 3 == 1):
            self.player_score += 1
            self.winner_label.config(text="Bạn đã thắng!!!")
            self.player_score_label.config(text = 'Điểm của bạn : ' + str(self.player_score))
        else:
            self.computer_score += 1
            self.winner_label.config(text="Máy tính đã thắng!!!")
            self.computer_score_label.config(text='Điểm của máy : ' + str(self.computer_score))

    #Function to Randomly Select Computer Choice
    def get_computer_choice(self):
        return random.choice(self.options)
