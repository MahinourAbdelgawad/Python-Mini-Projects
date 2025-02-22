from tkinter import *

expression = ""

def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)

def equalpress():
    try:

        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set("ERROR")
        expression = ""

def clear():
    global expression
    equation.set("")
    expression = ""

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background = "gray")
    gui.title("Calculator")
    gui.geometry("270x150")

    equation = StringVar()
    textEntry = Entry(gui, textvariable = equation)
    textEntry.grid(columnspan = 4,ipadx = 70)

    button7 = Button(gui, text = "7", fg = "black", bg = "white",
                     command = lambda: press(7), height = 1, width = 7 )
    button7.grid(row = 2, column = 0)

    button8 = Button(gui, text = "8", fg = "black", bg = "white",
                     command = lambda: press(8), height = 1, width = 7 )
    button8.grid(row = 2, column = 1)

    button9 = Button(gui, text = "9", fg = "black", bg = "white",
                     command = lambda: press(9), height = 1, width = 7 )
    button9.grid(row = 2, column = 2)

    divide = Button(gui, text = "/", fg = "black", bg = "white",
                     command = lambda: press("/"), height = 1, width = 7 )
    divide.grid(row = 2, column = 3)

    button4 = Button(gui, text = "4", fg = "black", bg = "white",
                     command = lambda: press(4), height = 1, width = 7 )
    button4.grid(row = 3, column = 0)

    button5 = Button(gui, text = "5", fg = "black", bg = "white",
                     command = lambda: press(5), height = 1, width = 7 )
    button5.grid(row = 3, column = 1)

    button6 = Button(gui, text = "6", fg = "black", bg = "white",
                     command = lambda: press(6), height = 1, width = 7 )
    button6.grid(row = 3, column = 2)

    multiply = Button(gui, text = "*", fg = "black", bg = "white",
                     command = lambda: press("*"), height = 1, width = 7 )
    multiply.grid(row = 3, column = 3)

    button1 = Button(gui, text = "1", fg = "black", bg = "white",
                     command = lambda: press(1), height = 1, width = 7 )
    button1.grid(row = 4, column = 0)

    button2 = Button(gui, text = "2", fg = "black", bg = "white",
                     command = lambda: press(2), height = 1, width = 7 )
    button2.grid(row = 4, column = 1)

    button3 = Button(gui, text = "3", fg = "black", bg = "white",
                     command = lambda: press(3), height = 1, width = 7 )
    button3.grid(row = 4, column = 2)

    minus = Button(gui, text = "-", fg = "black", bg = "white",
                     command = lambda: press("-"), height = 1, width = 7 )
    minus.grid(row = 4, column = 3)

    button0 = Button(gui, text = "0", fg = "black", bg = "white",
                     command = lambda: press(0), height = 1, width = 7 )
    button0.grid(row = 5, column = 0)

    Decimal = Button(gui, text = ".", fg = "black", bg = "white",
                     command = lambda: press("."), height = 1, width = 7 )
    Decimal.grid(row = 5, column = 1)

    plus = Button(gui, text = "+", fg = "black", bg = "white",
                     command = lambda: press("+"), height = 1, width = 7 )
    plus.grid(row = 5, column = 2)

    equal = Button(gui, text = "=", fg = "black", bg = "orange",
                     command = equalpress, height = 1, width = 7 )
    equal.grid(row = 5, column = 3)

    clear = Button(gui, text = "CLR", fg = "black", bg = "orange",
                     command = clear, height = 1, width = 7 )
    clear.grid(row = 6, column = 1, columnspan = 2)

    gui.mainloop()
