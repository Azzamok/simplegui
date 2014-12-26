import sys
from tkinter import *

root = Tk()
herp = StringVar()


def mHello():
    xtext = herp.get() #Gets the text user typed in box
    xlabel = Label(root, text=xtext) #Makes a label using the text
    xlabel.grid(row=0, column=4) #Place label
    return
    #xlabel = Label(text='hello world')
    #xlabel.grid(row=0, column=4)

def mNew():
    mlabel3 = Label(root, text='You clicked New')
    mlabel3.place(x=200, y=200)
    return


#Title at the top
root.title("Simple GUI")
#Window size
root.geometry("640x480")

mlabel = Label(text='blah', fg='#3aec61', bg='#07c7dd')
#mlabel.pack() #Places label at the top middle
#mlabel.place(x=150, y=150) #Places label at custom co-ords

#.grid() Think excel spreadsheets
mlabel.grid(row=0, column=0, sticky=W) #Align left

mlabel2 = Label(text='hello there', fg='green', bg='yellow')
mlabel2.grid(row=1, column=0)

mlabel3 = Label(text='potatoes', fg='purple',bg='cyan')
mlabel3.grid(row=0, column=1)

mbutton = Button(text='OK', command = mHello)
#mbutton.place(x=300, y=300)
mbutton.grid(row=0, column=2)

#Entry Box
mEntry = Entry(root, textvariable=herp)
mEntry.grid(row=0, column=3)
#mEntry.place(x=400, y=450)

#Menu Bar
menubar = Menu(root)

#File menu
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'New', command = mNew)
filemenu.add_command(label = 'Open')
filemenu.add_command(label = 'Save As...')
filemenu.add_command(label = 'Close')
menubar.add_cascade(label = 'File', menu = filemenu)

#Help menu
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = 'Help Docs')
helpmenu.add_command(label = 'About')
menubar.add_cascade(label = 'Help', menu = helpmenu)


#Scrollbar
#scrollbar = Scrollbar(root)
#scrollbar.pack(side = RIGHT, fill = Y)
#myList = Listbox(root, yscrollcommand = scrollbar.set)
#myList.pack(side = LEFT, fill = BOTH)
#scrollbar.config(command = myList.yview)

root.config(menu = menubar)






#For windows
root.mainloop()
