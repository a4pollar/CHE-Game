# Import module  
from itertools import cycle     
from random import randrange
from tkinter import Canvas, Tk, messagebox, font
from tkinter import*
from PIL import Image,ImageTk

# Create object  
root = Tk() 
  
# Adjust size  
root.geometry("400x400") 
  
# Add image file 
bg=Image.open("\__pycache__\Bomb.gif")
bg=bg.resize((10,10),Image.LANCZOS)
bg = PhotoImage("\__pycache__\Bomb.gif") 

c:\Users\alexa\OneDrive\Documents\GitHub\CHE-Game\__pycache__\crabapple1.gif
  
# Create Canvas 
canvas1 = Canvas( root, width = 400, 
                 height = 400) 
  
canvas1.pack(fill = "both", expand = True) 
  
# Display image 
canvas1.create_image( 0, 0, image = bg,  
                     anchor = "nw") 
  
# Add Text 
canvas1.create_text( 200, 250, text = "Welcome") 
  
# Create Buttons 
button1 = Button( root, text = "Exit") 
button3 = Button( root, text = "Start") 
button2 = Button( root, text = "Reset") 
  
# Display Buttons 
button1_canvas = canvas1.create_window( 100, 10,  
                                       anchor = "nw", 
                                       window = button1) 
  
button2_canvas = canvas1.create_window( 100, 40, 
                                       anchor = "nw", 
                                       window = button2) 
  
button3_canvas = canvas1.create_window( 100, 70, anchor = "nw", 
                                       window = button3) 
  
# Execute tkinter 
root.mainloop()