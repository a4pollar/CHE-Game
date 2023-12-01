from itertools import cycle #AAP: import cycle to create a colour cycle
from random import randrange #AAP: import randrange for generating random numbers
from tkinter import Canvas, Tk, messagebox, font #AAP: import Canvas, Tk and messagebox module

canvas_width = 800  #AAP: set up canvas width
canvas_height = 400 #AAP: set up canvas height

root = Tk() #AAP: creating the main Tinkter window
root.title("Egg Catcher") #giving the window a title
c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue") #AAP: creating a canvas with a given background colour and given dimensions
c.create_rectangle(-5, canvas_height-100, canvas_width+5, canvas_height+5, fill="sea green", width=0) #AAP: draws a sea green rectangle 
c.create_oval(-80, -80, 120, 120, fill='orange', width=0) #AAP: draws an orange oval
c.pack() #AAP: packs the canvas into the Tinkter window

color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"]) #AAP: colour cycle for the eggs
egg_width = 45 #AAP: width of the eggs
egg_height = 55 #AAP: height of the eggs
egg_score = 10 #AAP: score value if you catch an egg
egg_speed = 500 #AAP: speed of which the eggs fall
egg_interval = 4000 #AAP: interval between egg drops
difficulty = 0.95 #AAP: level of difficulty
catcher_color = "blue" #AAP: colour of the catcher
catcher_width = 100 #AAP: width of the catcher
catcher_height = 100 #AAP: height of the catcher
catcher_startx = canvas_width / 2 - catcher_width / 2 #AAP: starting x-coordinate of the catcher
catcher_starty = canvas_height - catcher_height - 20  #AAP: starting y-coordinate of the catcher
catcher_startx2 = catcher_startx + catcher_width      #AAP: ending x-coordinate of the catcher
catcher_starty2 = catcher_starty + catcher_height     #AAP: ending y-coordinate of the catcher

catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=3) #AAP: draws the catcher on the canvas
game_font = font.nametofont("TkFixedFont") #AAP: retrieves the Tinkter font
game_font.config(size=18) AAP: sets font size


score = 0 #AAP: starting score
score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: "+ str(score)) #AAP: displays score on canvas

lives_remaining = 3 #AAP: starting lives
lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text="Lives: "+ str(lives_remaining)) #AAP: displays remaining lives on canvas

eggs = []

def create_egg():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)

def move_eggs():
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        #print(c.coords(egg))
        c.move(egg,0, 10)
        if eggy2 > canvas_height:
            egg_dropped(egg)
    root.after(egg_speed, move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo("Game Over!", "Final Score: "+ str(score))
        root.destroy()

def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))

def check_catch():
    (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    root.after(100, check_catch)

def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty)
    egg_interval = int(egg_interval * difficulty)
    c.itemconfigure(score_text, text="Score: "+ str(score))

def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)

def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)

c.bind("<Left>", move_left)
c.bind("<Right>", move_right)
c.focus_set()
root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch)
root.mainloop()

#Coded with 💙 by Mr. Unity Buddy
