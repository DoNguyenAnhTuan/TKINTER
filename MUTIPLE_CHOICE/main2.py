from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.config(bg="Blue")
window.title("CHƯƠNG TRÌNH TRẮC NGHIỆM")
window.geometry("500x500")

img = Image.open("D:\SẢN PHẨM SNLTW\SNLTW_HP3_SP\MUTIPLE_CHOICE\image.png")
bg = img.resize((500, 500))
bg = ImageTk.PhotoImage(bg)

labelbg = Label(window, image=bg)
labelbg.image = bg
labelbg.place(x=0, y=0)
labeltitle = Label(window, text="CHƯƠNG TRÌNH TRẮC NGHIỆM", background='#bee6cb', font=('Verdana', 13),  width=39, height=2)
labeltitle.place(x=30, y=10)
# Sử dụng phương thức ghi đè file để cập nhật điểm số về 0 trước khi ng dùng bắt đầu vòng chs mới
f = open("scores.txt", "w")
f.write("0")
f.close()


def newin(data):
    global resultlb, labelscores
    window2 = Toplevel()
    window2.title(data[0])
    window2.geometry('500x500')
    f = open("scores.txt")
    currentscore = f.readline()
    f.close()
    labelscores = Label(window2, text="ĐIỂM SỐ: " + str(currentscore), background='#e6bebe', font=('Verdana', 13), width=12, height=2)
    labelscores.place(x=10, y=400)
    window2.config(bg='AliceBlue')

    text = Text(window2, padx= 15, pady=15, wrap=WORD, height=2, width=44, font=('Verdana', 13),
                background="#badae0")
    text.insert(INSERT,
                data[1])
    text.place(x=0, y=10)
    R1 = Label(window2, font=('Verdana', 13), text=data[2], bg='AliceBlue')
    R1.place(x=10, y=100)
    R2 = Label(window2, font=('Verdana', 13), text=data[3], bg='AliceBlue')
    R2.place(x=10, y=150)
    R3 = Label(window2, font=('Verdana', 13), text=data[4], bg='AliceBlue')
    R3.place(x=10, y=200)
    lb = Label(window2, font=('Verdana', 13), text="Nhập đáp án", background="Aliceblue")
    lb.place(x=10, y= 250)
    entry = Entry(window2, font=('Verdana', 13))
    entry.place(x=160, y=250)
    resultlb = Label(window2, text="", background="Aliceblue", font=('Verdana', 16))
    resultlb.place(x=10, y=350)
    btn = Button(window2, text="Xác nhận", font=('Verdana', 13), bg="#eddaa6", command=lambda: result(entry.get(), data[5], currentscore))
    btn.place(x=200, y=300)


def result(text, result, curscores):
    global resultlb, labelscores
    if str(text).lower() == str(result).lower():
        resultlb.configure(text="Chính xác")
        f = open("scores.txt", "w")
        f.write(str(int(curscores)+10))
        f.close()
        labelscores.configure(text="ĐIỂM SỐ: "+ str(int(curscores)+10))

    else:
        resultlb.configure(text="Sai rồi")


# Tạo liên kết của Button ở window thứ nhất vs window thứ hai
questions = [
    ['Câu 1', 'Kì World Cup đầu tiên tổ chức vào năm nào ?', 'A.1940', 'B.1934', 'C.1930', 'C'],
    ['Câu 2', 'Kì World Cup đầu tiên được tổ chức ở đâu ? ', 'A.France', 'B.Spain', 'C.Uruguay', 'C'],
    ['Câu 3', 'Vì sao kì World Cup ở Quatar lại được tổ chức vào mùa đông thay vì mùa hè ? ', 'A.Vì trời nắng nóng',
     'B.Vì nước chủ nhà muốn tạo đặc biệt ', 'C.Vì bị hoãn do nhiều sự cố', 'A'],
    ["Câu 4 ", "Manchester United được thành lập vào năm bao nhiêu ?", "A.1875", "B.1878", "C.1880", "B"],
    ["Câu 5 ", "Huấn luyện viên vĩ đại nhất của Manchester United tên gì ?", "A.Sir Alex Ferguson", "B.Arsène Wenger",
     "D.Fernando Santos", "A"],
    ["Câu 6 ", "Messi sinh ngày tháng năm nào ?", "A.25/6/1988", "B.24/4/1985", "C.24/6/1987", "C"],
    ["Câu 7 ", "Manchester City được thành lập vào năm nào ?", "A.1879", "B.1880", "C.1881", "B"],
    ["Câu 8 ", "World Cup 2026 có bao nhiêu đội ?", "A.36", "B.41", "C.48", "C"],
    ["câu 9", "Euro được tổ chức định kì mấy năm một lần ?", "A.3 năm", "B.4 năm", "C.2 năm", "B"],
    ["Câu 10", "David Beckham sinh năm bao nhiêu ? ", "A.1980", "B.1969", "C.1975", "C"]]
  # bd = độ dày của viền

btn1 = Button(window, text='Câu 1', font=('Verdana', 13), bg="#eddaa6", command=lambda: newin(questions[0]), width=12, height=2)
btn1.place(x=30, y=80)

btn2 = Button(window, text='Câu 2', font=('Verdana', 13), bg="#eddaa6", command=lambda: newin(questions[1]), width=12, height=2)
btn2.place(x=30, y=160)

btn3 = Button(window, text='Câu 3', font=('Verdana', 13), bg="#eddaa6", command=lambda: newin(questions[2]), width=12, height=2)
btn3.place(x=30, y=240)

btn4 = Button(window, text='Câu 4', font=('Verdana', 13), bg="#eddaa6", command=lambda: newin(questions[3]), width=12, height=2)
btn4.place(x=30, y=320)

btn5 = Button(window, text='Câu 5', font=('Verdana', 13), bg="#eddaa6", command=lambda: newin(questions[4]), width=12, height=2)
btn5.place(x=30, y=400)

btn6 = Button(window, text='Câu 6', font=('Verdana', 13), bg="#eddaa6", command=lambda: newin(questions[5]), width=12, height=2)
btn6.place(x=320, y=80)

btn7 = Button(window, text='Câu 7', font=('Verdana', 13), bg="#eddaa6", command=lambda: newin(questions[6]), width=12, height=2)
btn7.place(x=320, y=160)

btn8 = Button(window, text='Câu 8', font=('Verdana', 13), bg="#eddaa6", command=lambda: newin(questions[7]), width=12, height=2)
btn8.place(x=320, y=240)

btn9 = Button(window, text='Câu 9', font=('Verdana', 13), bg="#eddaa6", command=lambda: newin(questions[8]), width=12, height=2)
btn9.place(x=320, y=320)

btn10 = Button(window, text='Câu 10', font=('Verdana', 13), bg="#eddaa6", command=lambda: newin(questions[9]), width=12, height=2)
btn10.place(x=320, y=400)

window.mainloop()