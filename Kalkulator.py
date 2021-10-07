from tkinter import *  # import tkinter library
import tkinter.ttk as ttk
import tkinter.messagebox as mbox  # import okienek z komunikatami

calculator = Tk()  # tworzenie okna obiektu
calculator.configure(background='grey16')  # kolor tla
calculator.title('Kalkulator')  # zmiana nazwy okna
operator = ""
calculator.geometry('900x500')  # zmiana rozmiaru okna

# tlo
img1 = PhotoImage(file="tlo.png")  # tlo z gradientem
labelimage = Label(
    calculator,
    image=img1,
    background="grey16",
)
labelimage.pack(pady=0)  # tlo zajmuje rowno cale okno


# wyskakujace okienka
def exit_win():  # funkcja okienka zamykajacego
    ans = mbox.askyesno('Zamknij', 'Czy jesteś pewien?')  # tworzenie okna z odpowiedzia tak lub nie
    if ans:  # warunek
        calculator.destroy()  # zamkniecie okna


# napisy
part_text = StringVar()
part_label = Label(calculator, text='Dane', fg='gold', font=('bold', 14), bg='gray22')  # tresc pierwszego napisu
part_label.place(x=120, y=50)  # umiejscowienie napisu w oknie z uzyciem place

part_label = Label(calculator, text='Wynik', fg='gold', font=('bold', 14), bg='gray22')  # tresc drugiego napisu
part_label.place(x=480, y=50)  # umiejscowienie napisu w oknie z uzyciem place

# wyswietlacz
text_Input = StringVar()
Total = StringVar()
e = Entry(calculator, font=('Digital-7', 20, 'bold'), fg='red', textvariable=text_Input, bd=10, insertwidth=2,
          # czcionka Digital-7
          bg="black", justify='left')  # justify okresla od ktorej strony wyswietli sie napis
e.place(x=120, y=80)  # textvariable laczy wyswietlacz z odpowiednia funkcja

e = Entry(calculator, font=('Digital-7', 20, 'bold'), fg='green', textvariable=Total, bd=10, insertwidth=2,
          # czcionka Digital-7
          bg="black", justify='left')
e.place(x=480, y=80)


# funkcje przyciskow
def btnClick(numbers):  # funkcja dzialania przyciskow
    global operator  # pozwala modyfikowac zmienna na zewnatrz funkcji
    operator = operator + str(numbers)  # zamienia specyficzne wartosci na string
    text_Input.set(operator)  # umieszcza klikniete liczby na wyswietlaczu


def btnClearDisplay():  # funkcja czyszczenia wyswietlacza
    global operator
    operator = ""
    text_Input.set("")
    Total.set("")  # w tym przypadku set nie umieszcza nic i w ten sposob czysci ekran wyswietlacza


def btnEqualsInput():  # funcja wyswietlajaca wynik
    global operator
    sumup = str(eval(operator))  # funkcja pozwala wykonywac dowolne ciagi znakow jako kod Pythona
    Total.set(sumup)  # umieszcza wynik Total jest umieszczone w drugim wyswietlaczu
    operator = ""


# grafika na przyciski
img_0 = PhotoImage(file="przycisk0.png")  # import grafiki z folderu
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

# przyciski wielkosc, grafika i przypisane funkcje
przycisk_0 = Button(calculator, image=img_0, border=0, command=lambda: btnClick(0))  # przyciski z liczbami i dzialaniami
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
przycisk_15 = Button(calculator, image=img_15, border=0, command=btnEqualsInput)  # przycisk rowna sie
przycisk_16 = ttk.Button(calculator, image=img_16, command=exit_win)  # przycisk zamykajacy
przycisk_17 = Button(calculator, image=img_17, border=0, command=btnClearDisplay)  # przycisk czyszczacy

# przyciski rozmieszczenie
przycisk_0.place(x=50, y=390)  # wspolrzedna przyciskow
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

calculator.resizable(0, 0)  # uniemozliwia zmiane rozmiaru okna i zapobiega nieczytelnosci
calculator.mainloop()  # glowna petla napedzajaca caly program
