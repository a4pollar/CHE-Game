mins = int(input("MINUTES?"))
secs = 0
print("TIMER HAS STARTED!")
import time

print("TIMER HAS STOPPED!")
from turtle import *
setup()
tl = Turtle()
tl.write(str(mins).zfill(2) + ":" + str(secs).zfill(2), font = ("arial", 160, "normal"))
while mins >= 0:
    tl.hideturtle()
    tl.clear()

from tkinter import *
import tkinter.messagebox
root=Tk()
tkinter.messagebox.showinfo('Timer','TIMER HAS STOPPED!')
root.mainloop()
