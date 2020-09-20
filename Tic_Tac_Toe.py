#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vaibhav account
#
# Created:     27/08/2020
# Copyright:   (c) vaibhav account 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
#root.geometry("650x500")

clicked = True
count = 0

def reset():
    pass

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkifwon():
    global winner
    winner = False
    finala = e1.get()
    finalb = e2.get()

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg = "red")
        b2.config(bg = "red")
        b3.config(bg = "red")
        winner = True
        messagebox.showinfo('', finala + ' has won')
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg = "red")
        b5.config(bg = "red")
        b6.config(bg = "red")
        winner = True
        messagebox.showinfo('', finala + ' has won')
        disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b9.config(bg = "red")
        b8.config(bg = "red")
        b7.config(bg = "red")
        winner = True
        messagebox.showinfo('', finala + ' has won')
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg = "red")
        b4.config(bg = "red")
        b7.config(bg = "red")
        winner = True
        messagebox.showinfo('', finala + ' has won')
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg = "red")
        b5.config(bg = "red")
        b8.config(bg = "red")
        winner = True
        messagebox.showinfo('', finala + ' has won')
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg = "red")
        b6.config(bg = "red")
        b9.config(bg = "red")
        winner = True
        messagebox.showinfo('', finala + ' has won')
        disable_all_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg = "red")
        b5.config(bg = "red")
        b7.config(bg = "red")
        winner = True
        messagebox.showinfo('', finala + ' has won')
        disable_all_buttons()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg = "red")
        b5.config(bg = "red")
        b9.config(bg = "red")
        winner = True
        messagebox.showinfo('', finala + ' has won')
        disable_all_buttons()
#-------------------------------------------------------------------------------
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg = "red")
        b2.config(bg = "red")
        b3.config(bg = "red")
        winner = True
        messagebox.showinfo('', finalb + ' has won')
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg = "red")
        b5.config(bg = "red")
        b6.config(bg = "red")
        winner = True
        messagebox.showinfo('', finalb + ' has won')
        disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b9.config(bg = "red")
        b8.config(bg = "red")
        b7.config(bg = "red")
        winner = True
        messagebox.showinfo('', finalb + ' has won')
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg = "red")
        b4.config(bg = "red")
        b7.config(bg = "red")
        winner = True
        messagebox.showinfo('', finalb + ' has won')
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg = "red")
        b5.config(bg = "red")
        b8.config(bg = "red")
        winner = True
        messagebox.showinfo('', finalb + ' has won')
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg = "red")
        b6.config(bg = "red")
        b9.config(bg = "red")
        winner = True
        messagebox.showinfo('', finalb + ' has won')
        disable_all_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg = "red")
        b5.config(bg = "red")
        b7.config(bg = "red")
        winner = True
        messagebox.showinfo('', finalb + ' has won')
        disable_all_buttons()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg = "red")
        b5.config(bg = "red")
        b9.config(bg = "red")
        winner = True
        messagebox.showinfo('', finalb + ' has won')
        disable_all_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("Tied", finala + " and " + finalb +" tie!!")
        disable_all_buttons()


def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()

    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()

    else:
        messagebox.showerror('Bad boii', 'Hey, spot already been selected. \n Pick another box boii')

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global e1, e2
    global clicked, count
    clicked = True
    count = 0

    e1 = Entry(root, width=30, bg="black", fg="White", borderwidth=2)
    e1.grid(row = 0, column=0, columnspan=3)
    e1.insert(1, "Enter your name: ")

    e2 = Entry(root, width=30, borderwidth=2)
    e2.grid(row = 1, column=0, columnspan=3)
    e2.insert(1, "Enter your name: ")

    b1 = Button(root, text=" ", font=('Helvetica', 20), height=3, width=6, bg="SystemButtonFace", command=lambda:b_click(b1))
    b2 = Button(root, text=" ", font=('Helvetica', 20), height=3, width=6, bg="SystemButtonFace", command=lambda:b_click(b2))
    b3 = Button(root, text=" ", font=('Helvetica', 20), height=3, width=6, bg="SystemButtonFace", command=lambda:b_click(b3))

    b4 = Button(root, text=" ", font=('Helvetica', 20), height=3, width=6, bg="SystemButtonFace", command=lambda:b_click(b4))
    b5 = Button(root, text=" ", font=('Helvetica', 20), height=3, width=6, bg="SystemButtonFace", command=lambda:b_click(b5))
    b6 = Button(root, text=" ", font=('Helvetica', 20), height=3, width=6, bg="SystemButtonFace", command=lambda:b_click(b6))

    b7 = Button(root, text=" ", font=('Helvetica', 20), height=3, width=6, bg="SystemButtonFace", command=lambda:b_click(b7))
    b8 = Button(root, text=" ", font=('Helvetica', 20), height=3, width=6, bg="SystemButtonFace", command=lambda:b_click(b8))
    b9 = Button(root, text=" ", font=('Helvetica', 20), height=3, width=6, bg="SystemButtonFace", command=lambda:b_click(b9))

    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)
    b3.grid(row=2, column=2)

    b4.grid(row=3, column=0)
    b5.grid(row=3, column=1)
    b6.grid(row=3, column=2)

    b7.grid(row=4, column=0)
    b8.grid(row=4, column=1)
    b9.grid(row=4, column=2)

def helper():
    messagebox.showinfo("Help", "X is black and O is white")

def about():
    top = Toplevel()
    top.title("Copyright is protected")
    label = Label(top, text="Author: Vaibhav Dachavaram")
    label2 = Label(top, text="All copyright protected")

    label.pack(pady=5)
    label2.pack(pady=3)

my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=FALSE)
my_menu.add_cascade(label="Options", menu=options_menu)

options_menu.add_command(label="Reset game", command=reset)

ins_menu = Menu(my_menu, tearoff = FALSE)
my_menu.add_cascade(label="Instructions", menu=ins_menu)

ins_menu.add_command(label="Who is X and Who is O?", command=helper)

about_menu = Menu(my_menu, tearoff = FALSE)
my_menu.add_cascade(label="About", menu=about_menu)

about_menu.add_command(label="Copyright", command=about)


reset()

root.mainloop()