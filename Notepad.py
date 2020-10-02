#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vaibhav account
#
# Created:     22/08/2020
# Copyright:   (c) vaibhav account 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter import messagebox

#-------------------------------------------------------------------------------

import os, sys
import sys
import time
import webbrowser as google

#-------------------------------------------------------------------------------

root = Tk()
root.title('Notepad')
root.geometry('750x509')
root.iconbitmap('C:\Vaibhav\CNotepad.ico')

#-------------------------------------------------------------------------------
global open_status_name
open_status_name = text_file = False

global selected
selected = False

#-------------------------------------------------------------------------------

def new_file():
    my_text.delete("1.0", END)

    root.title('New file - Notepad')
    status_bar.config(text = "New file  ")

    global open_status_name
    open_status_name = text_file = False


def open_file():
    my_text.delete("1.0", END)

    text_file = filedialog.askopenfilename(initialdir="C:", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files", "*.*")))

    if text_file:
        global open_status_name
        open_status_name = text_file

    name = text_file
    status_bar.config(text = f'{name}        ')
    name = name.replace("C:/Vaibhav/Coding/GUI interface with python/", "")
    root.title(f'{name} - notepad')

    text_file = open(text_file, 'r')
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()

def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension = ".*", initialdir = "C:", title = "Save file as", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files", "*.*")))
    if text_file:

        name = text_file
        status_bar.config(text = 'New file has been saved.')
        messagebox.showinfo("File saved.", "New file have been saved.")
        name = name.replace("C:/Vaibhav/Coding/GUI interface with python/", "")
        root.title(f'{name} - notepad')

        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))

        text_file.close()

def save_file():
    global open_status_name

    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

        status_bar.config(text = f'Existing file has been saved: {open_status_name}    ')
        messagebox. showinfo("File saved.", "Existing file have been saved.")

    else:
        save_as_file()

def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)

def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)


def bold_it():
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight = "bold")

    my_text.tag_configure("bold", font = bold_font)#

    current_tags = my_text.tag_names("sel.first")

    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")

    else:
        my_text.tag_add("bold", "sel.first", "sel.last")

def italics_it():
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant = "italic")

    my_text.tag_configure("italic", font = italics_font)

    current_tags = my_text.tag_names("sel.first")

    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")

    else:
        my_text.tag_add("italic", "sel.first", "sel.last")

def text_color():

    my_color = colorchooser.askcolor()[1]

    if my_color:

        color_font = font.Font(my_text, my_text.cget("font"))
        #color_font.configure(slant = "italic")

        my_text.tag_configure("colored", font = color_font, foreground = my_color)

        current_tags = my_text.tag_names("sel.first")

        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")

        else:
            my_text.tag_add("colored", "sel.first", "sel.last")

def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)

def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)

def about_help():
    messagebox.showwarning("Notepad Copyright", "The author of this is Vaibhav Dachavaram. Copyright Protected.")

#
def select_all():
    my_text.tag_add('sel', '1.0', 'end')

def clear_all():
    my_text.delete(1.0, END)

def dark_mode():
    dark_mode_color = "#373737"

    root.config(bg="black")
    my_text.config(bg=dark_mode_color, fg="white", selectbackground = "yellow", selectforeground = "black")
    color_menu.config(bg="black", fg="white")
    file_menu.config(bg="black", fg="white")
    edit_menu.config(bg="black", fg="white")
    font_menu.config(bg="black", fg="white")
    about_menu.config(bg="black", fg="white")
    mode_menu.config(bg="black", fg="white")
    status_bar.config(bg=dark_mode_color, fg="white")

def light_mode():
    main_color = "SystemButtonFace"
    second_color = "SystemButtonFace"
    text_color = "black"

    root.config(bg=main_color)
    my_text.config(bg="white", fg=text_color, selectbackground = "light grey", selectforeground = "black")
    color_menu.config(bg=main_color, fg="black")
    file_menu.config(bg=main_color, fg="black")
    edit_menu.config(bg=main_color, fg="black")
    font_menu.config(bg=main_color, fg="black")
    about_menu.config(bg=main_color, fg="black")
    mode_menu.config(bg=main_color, fg="black")
    status_bar.config(bg=main_color, fg="black")

def tiwme():
    status_bar.config(text=time.strftime("%H:%M"))

def Gmail(e):
    global selected
    warning = messagebox.askokcancel('Warning', "Select text if want to copy into gmail. Press OK to continue, or Cancel to stop")
    if warning == 1:
        try:
            google.open_new_tab('https://mail.google.com/mail/u/0/')
            if e:
                selected = root.clipboard_get()

            if my_text.selection_get():
                selected = my_text.selection_get()
                root.clipboard_clear()
                root.clipboard_append(selected)
        except:
            pass
#-------------------------------------------------------------------------------
def new_win():
    top = Toplevel()
    top.title('New Window - Notepad')
    top.iconbitmap('C:\Vaibhav\CNotepad.ico')
    my_frame = Frame(top)
    my_frame.pack(pady = 6)

    #---------------------------------------------------------------------------

    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    hor_scroll = Scrollbar(my_frame, orient = 'horizontal')
    hor_scroll.pack(side=BOTTOM, fill = X)

    #---------------------------------------------------------------------------

    my_text = Text(my_frame, font = ("Arial", 12), selectbackground = "light grey", selectforeground = "black", undo=True, yscrollcommand = text_scroll.set, wrap = "none", xscrollcommand=hor_scroll.set)
    my_text.pack()

    #---------------------------------------------------------------------------

    text_scroll.config(command=my_text.yview)
    hor_scroll.config(command=my_text.xview)

    #---------------------------------------------------------------------------

    my_menu = Menu(top)
    top.config(menu = my_menu)

    file_menu = Menu(my_menu, tearoff = FALSE)
    my_menu.add_cascade(label="File", menu = file_menu)
    file_menu.add_cascade(label="New", command = new_file)
    file_menu.add_cascade(label="Open", command = open_file)
    file_menu.add_cascade(label="Save", command = save_file)
    file_menu.add_cascade(label="Save As", command = save_as_file)
    file_menu.add_separator()
    file_menu.add_cascade(label="Exit", command=root.quit)

    edit_menu = Menu(my_menu, tearoff = FALSE)
    my_menu.add_cascade(label="Edit", menu = edit_menu)
    edit_menu.add_cascade(label="Cut                 Ctrl X", command = lambda: cut_text(False))
    edit_menu.add_cascade(label="Copy              Ctrl C", command = lambda: copy_text(False))
    edit_menu.add_cascade(label="Paste              Ctrl V", command = lambda: paste_text(False))
    edit_menu.add_separator()
    edit_menu.add_cascade(label="Undo              Ctrl Z", command=my_text.edit_undo)
    edit_menu.add_cascade(label="Redo              Ctrl Y", command=my_text.edit_redo)
    edit_menu.add_separator()
    edit_menu.add_cascade(label="Select all        Ctrl A", command=select_all)
    edit_menu.add_cascade(label="Clear all         Ctrl Y", command=clear_all)
    edit_menu.add_separator()
    edit_menu.add_cascade(label="Time        Ctrl T", command = tiwme)


    font_menu = Menu(my_menu, tearoff = FALSE)
    my_menu.add_cascade(label="Font", menu = font_menu)
    font_menu.add_cascade(label="Bold", command = bold_it)
    font_menu.add_cascade(label="Italics", command = italics_it)

    color_menu = Menu(my_menu, tearoff = FALSE)
    my_menu.add_cascade(label="Color", menu = color_menu)
    color_menu.add_cascade(label="Change Text ", command = text_color)
    color_menu.add_cascade(label="Change Selected Text", command = text_color)
    color_menu.add_cascade(label="Change All Text", command = all_text_color)
    color_menu.add_cascade(label="Change Background", command = bg_color)

    about_menu = Menu(my_menu, tearoff = FALSE)
    my_menu.add_cascade(label="Help", menu = about_menu)
    about_menu.add_cascade(label="About", command = about_help)

    mode_menu = Menu(my_menu, tearoff = FALSE)
    my_menu.add_cascade(label="Mode", menu = mode_menu)
    mode_menu.add_cascade(label="Dark mode", command=dark_mode)
    mode_menu.add_cascade(label="Normal mode", command=light_mode)

    #---------------------------------------------------------------------------

    status_bar = Label (top, text = 'Ready   ', anchor = E)
    status_bar.pack(fill = X, side = BOTTOM, ipady = 5)

    #---------------------------------------------------------------------------

    top.bind('<Control-Key-x>', cut_text)
    top.bind('<Control-Key-c>', copy_text)
    top.bind('<Control-Key-v>', paste_text)
    top.bind('<Control-Key-T>', tiwme)

#-------------------------------------------------------------------------------

my_frame = Frame(root)
my_frame.pack(pady = 6)

#-------------------------------------------------------------------------------

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

hor_scroll = Scrollbar(my_frame, orient = 'horizontal')
hor_scroll.pack(side=BOTTOM, fill = X)

#-------------------------------------------------------------------------------

my_text = Text(my_frame, font = ("Arial", 12), selectbackground = "light grey", selectforeground = "black", undo=True, yscrollcommand = text_scroll.set, wrap = "none", xscrollcommand=hor_scroll.set)
my_text.pack()

#-------------------------------------------------------------------------------

text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

#-------------------------------------------------------------------------------

my_menu = Menu(root)
root.config(menu = my_menu)

file_menu = Menu(my_menu, tearoff = FALSE)
my_menu.add_cascade(label="File", menu = file_menu)
file_menu.add_cascade(label="New", command = new_file)
file_menu.add_cascade(label="Open", command = open_file)
file_menu.add_cascade(label="Save", command = save_file)
file_menu.add_cascade(label="Save As", command = save_as_file)
file_menu.add_separator()
file_menu.add_cascade(label="Exit", command=root.quit)
file_menu.add_separator()
file_menu.add_cascade(label="Open up Gmail", command = lambda: Gmail(False))

edit_menu = Menu(my_menu, tearoff = FALSE)
my_menu.add_cascade(label="Edit", menu = edit_menu)
edit_menu.add_cascade(label="Cut                 Ctrl X", command = lambda: cut_text(False))
edit_menu.add_cascade(label="Copy              Ctrl C", command = lambda: copy_text(False))
edit_menu.add_cascade(label="Paste              Ctrl V", command = lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_cascade(label="Undo              Ctrl Z", command=my_text.edit_undo)
edit_menu.add_cascade(label="Redo              Ctrl Y", command=my_text.edit_redo)
edit_menu.add_separator()
edit_menu.add_cascade(label="Select all        Ctrl A", command=select_all)
edit_menu.add_cascade(label="Clear all         Ctrl Y", command=clear_all)
edit_menu.add_separator()
edit_menu.add_cascade(label="Time        Ctrl T", command = tiwme)
edit_menu.add_separator()
edit_menu.add_cascade(label = "New Window", command = new_win)


font_menu = Menu(my_menu, tearoff = FALSE)
my_menu.add_cascade(label="Font", menu = font_menu)
font_menu.add_cascade(label="Bold",command = bold_it)
font_menu.add_cascade(label="Italics", command = italics_it)

color_menu = Menu(my_menu, tearoff = FALSE)
my_menu.add_cascade(label="Color", menu = color_menu)
color_menu.add_cascade(label="Change Text ", command = text_color)
color_menu.add_cascade(label="Change Selected Text", command = text_color)
color_menu.add_cascade(label="Change All Text", command = all_text_color)
color_menu.add_cascade(label="Change Background", command = bg_color)

about_menu = Menu(my_menu, tearoff = FALSE)
my_menu.add_cascade(label="Help", menu = about_menu)
about_menu.add_cascade(label="About", command = about_help)

mode_menu = Menu(my_menu, tearoff = FALSE)
my_menu.add_cascade(label="Mode", menu = mode_menu)
mode_menu.add_cascade(label="Dark mode", command=dark_mode)
mode_menu.add_cascade(label="Normal mode", command=light_mode)

#-------------------------------------------------------------------------------

status_bar = Label (root, text = 'Ready   ', anchor = E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 5)

#-------------------------------------------------------------------------------

root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-Key-T>', tiwme)
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------

mainloop()
