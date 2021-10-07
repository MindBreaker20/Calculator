from tkinter import *  # import tkinter library
import tkinter.ttk as ttk
import tkinter.messagebox as mbox  # import of message boxes

calculator = Tk()  # creating an object window
calculator.configure(background='grey16')  # background color
calculator.title('Calculator')  # window's name change
operator = ""
calculator.geometry('900x500')  # window's size change

# background
img1 = PhotoImage(file="tlo.png")  # background with gradient
labelimage = Label(
    calculator,
    image=img1,
    background="grey16",
)
labelimage.pack(pady=0)  # setting size of background as full size window

# pop-up windows
def exit_win():  # closing window function
    ans = mbox.askyesno('Close', 'Are you sure?')  # window with an answer "YES" or "NO"
    if ans:  
        calculator.destroy()  # destroy window

# subtitles
part_text = StringVar()
part_label = Label(calculator, text='Data', fg='gold', font=('bold', 14), bg='gray22')  # the first subtitle
part_label.place(x=120, y=50)  # placing subtitle on the window

part_label = Label(calculator, text='Score', fg='gold', font=('bold', 14), bg='gray22')  #the second subtitle
part_label.place(x=480, y=50)  

# display
text_Input = StringVar()
Total = StringVar()
e = Entry(calculator, font=('Digital-7', 20, 'bold'), fg='red', textvariable=text_Input, bd=10, insertwidth=2,
          bg="black", justify='left')  # justify is used to define where subtitle will appear
e.place(x=120, y=80)  # textvariable matches subtitle with proper function

e = Entry(calculator, font=('Digital-7', 20, 'bold'), fg='green', textvariable=Total, bd=10, insertwidth=2,
          bg="black", justify='left')
e.place(x=480, y=80)

# button functions
def btnClick(numbers):  # button operation function
    global operator  # allows you to modify a variable outside the function
    operator = operator + str(numbers)  # converts specific values to string
    text_Input.set(operator)  # places the numbers clicked on the display

def btnClearDisplay():  # display cleaning function
    global operator
    operator = ""
    text_Input.set("")
    Total.set("")  # in this case, set puts nothing and thus clears the display screen

def btnEqualsInput():  # function displaying the result
    global operator
    sumup = str(eval(operator))  # this function allows any strings to be executed as Python code
    Total.set(sumup)  # places the result Total is listed in the second display
    operator = ""

# graphics on buttons
img_0 = PhotoImage(file="przycisk0.png")  # import graphics from a folder
img_1 = PhotoImage(file="przycisk1.png")
img_2 = PhotoImage(file="przycisk2.png")
img_3 = PhotoImage(file="przycisk3.png")
img_4 = PhotoImage(file="przycisk4.png")
img_5 = PhotoImage(file="przycisk5.png")
img_6 = PhotoImage(file="przycisk6.png")
img_7 = PhotoImage(file="przycisk7.png")
img_8 = PhotoImage(file="przycisk8.png")
img_9 = PhotoImage(file="przycisk9.png")
img_10 = PhotoImage(file="przycisk_mnoz.png")
img_11 = PhotoImage(file="przycisk_plus.png")
img_12 = PhotoImage(file="przycisk_dziel.png")
img_13 = PhotoImage(file="przycisk_minus.png")
img_14 = PhotoImage(file="przycisk_kropka.png")
img_15 = PhotoImage(file="przycisk_rownasie.png")
img_16 = PhotoImage(file="przycisk_close.png")
img_17 = PhotoImage(file="przycisk_cofnij.png")

# buttons size, graphics and assigned functions
przycisk_0 = Button(calculator, image=img_0, border=0, command=lambda: btnClick(0))  # buttons representing numbers and symbols of mathematical equations
przycisk_1 = Button(calculator, image=img_1, border=0, command=lambda: btnClick(1))
przycisk_2 = Button(calculator, image=img_2, border=0, command=lambda: btnClick(2))
przycisk_3 = Button(calculator, image=img_3, border=0, command=lambda: btnClick(3))
przycisk_4 = Button(calculator, image=img_4, border=0, command=lambda: btnClick(4))
przycisk_5 = Button(calculator, image=img_5, border=0, command=lambda: btnClick(5))
przycisk_6 = Button(calculator, image=img_6, border=0, command=lambda: btnClick(6))
przycisk_7 = Button(calculator, image=img_7, border=0, command=lambda: btnClick(7))
przycisk_8 = Button(calculator, image=img_8, border=0, command=lambda: btnClick(8))
przycisk_9 = Button(calculator, image=img_9, border=0, command=lambda: btnClick(9))
przycisk_10 = Button(calculator, image=img_14, border=0, command=lambda: btnClick("."))
przycisk_11 = Button(calculator, image=img_12, border=0, command=lambda: btnClick("/"))
przycisk_12 = Button(calculator, image=img_11, border=0, command=lambda: btnClick("+"))
przycisk_13 = Button(calculator, image=img_13, border=0, command=lambda: btnClick("-"))
przycisk_14 = Button(calculator, image=img_10, border=0, command=lambda: btnClick("*"))
przycisk_15 = Button(calculator, image=img_15, border=0, command=btnEqualsInput)  # button used for "="
przycisk_16 = ttk.Button(calculator, image=img_16, command=exit_win)  # close button
przycisk_17 = Button(calculator, image=img_17, border=0, command=btnClearDisplay)  # cleaning button

# buttons arrangement
przycisk_0.place(x=50, y=390)  #button coordinates
przycisk_1.place(x=50, y=180)
przycisk_2.place(x=212, y=180)
przycisk_3.place(x=375, y=180)
przycisk_4.place(x=50, y=250)
przycisk_5.place(x=212, y=250)
przycisk_6.place(x=375, y=250)
przycisk_7.place(x=50, y=320)
przycisk_8.place(x=212, y=320)
przycisk_9.place(x=375, y=320)
przycisk_10.place(x=375, y=390)
przycisk_11.place(x=540, y=390)
przycisk_12.place(x=540, y=180)
przycisk_13.place(x=540, y=250)
przycisk_14.place(x=540, y=320)
przycisk_15.place(x=700, y=320)
przycisk_16.place(x=695, y=387)
przycisk_17.place(x=700, y=180)

calculator.resizable(0, 0)  # resizeable makes window's size unchangeable
calculator.mainloop()  # mainloop running all program
