import sys
from tkinter import *
from tkinter import messagebox

root = Tk()
userInput = StringVar() #String variable that stores whatever the user types in the entry box

def mHello():
    xtext = userInput.get() #Gets the text user typed in box
    xlabel = Label(root, text=xtext) #Makes a label using the text
    xlabel.grid(row=0, column=4) #Place label
    return
    #xlabel = Label(text='hello world')
    #xlabel.grid(row=0, column=4)

def mNew():
    #mlabel3 = Label(root, text='You clicked New')
    #mlabel3.place(x=200, y=200)
    newWin = Toplevel()
    newWin.title("A new window")
    newWin.geometry("400x400")
    return

def mClose():
    exitBox = messagebox.askyesno(title="Exit", message="Do you want to quit?")
    if exitBox is True:
        root.quit()
    return

def mAbout():
    messagebox.showinfo(title="About", message="Just messing around with tkinter!")

"""Title at the top"""
root.title("Simple GUI")


"""Window size"""
root.geometry("720x480")


"""
Creating a label

text = what you want it to display
fg = foreground colour (hex)
bg = background colour (hex)
font = (Font type, size)
"""
mlabel = Label(text='blah, this is text', fg='#3aec61', bg='#07c7dd', font=("Calibri", 18))
#mlabel.pack() #Places label at the top middle
#mlabel.place(x=150, y=150) #Places label at custom co-ords


""".grid() command Think excel spreadsheets"""
mlabel.grid(row=0, column=0, sticky=W) #Align left

mlabel2 = Label(text='hello there', fg='green', bg='yellow')
mlabel2.grid(row=1, column=0)

mlabel3 = Label(text='potatoes', fg='purple',bg='cyan')
mlabel3.grid(row=0, column=1)


"""Button"""
mbutton = Button(text='OK', command = mHello)
#mbutton.place(x=300, y=300)
mbutton.grid(row=0, column=2)


"""Entry Box"""
mEntry = Entry(root, textvariable=userInput)
mEntry.grid(row=0, column=3)
#mEntry.place(x=400, y=450)


"""Menu Bar"""
menubar = Menu(root)

#File menu
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'New', command = mNew)
filemenu.add_command(label = 'Open')
filemenu.add_command(label = 'Save As...')
filemenu.add_command(label = 'Close', command = mClose)
menubar.add_cascade(label = 'File', menu = filemenu)
#filemenu.bind_all("<Control-n>", mNew()) #Doesn't work

#Help menu
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = 'Help Docs')
helpmenu.add_command(label = 'About', command = mAbout)
menubar.add_cascade(label = 'Help', menu = helpmenu)


root.config(menu = menubar)


"""Doesn't work..."""
#Scrollbar
#scrollbar = Scrollbar(root)
#scrollbar.pack(side = RIGHT, fill = Y)
#myList = Listbox(root, yscrollcommand = scrollbar.set)
#myList.pack(side = LEFT, fill = BOTH)
#scrollbar.config(command = myList.yview)




#For windows
root.mainloop()
