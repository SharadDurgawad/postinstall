#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sdurgawad
#
# Created:     23/03/2016
# Copyright:   (c) sdurgawad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Tkinter import *
from postinstall import *

root = Tk()

root.minsize(300, 300)
root.maxsize(300, 300)


label1 = Label( root, text="RPM List")
E1 = Entry(root, bd =5)

def getDate():
    rpmString = E1.get()
    removeEntry(rpmString)
    closeWindow()


def closeWindow():
    root.destroy()

submit = Button(root, text ="Submit", command = getDate)

label1.pack()
E1.pack()

submit.pack(side =BOTTOM)

root.mainloop()