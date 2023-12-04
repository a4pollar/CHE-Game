from itertools import cycle     
from random import randrange
from tkinter import Canvas, Tk, messagebox, font
from tkinter import*
from PIL import Image,ImageTk

canvas_width = 800
canvas_height = 400

root = Tk()
root.title("Egg Catcher")
c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue")

c.pack(expand = YES, fill = BOTH)

color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"])
egg_width = 45
egg_height = 55
egg_score = 10
egg_score1 = 20
egg_score2 = -15
egg_speed = 200
egg_interval = 2000
difficulty = 0.95
catcher_color = "green"
catcher_width = 80
catcher_height = 80
catcher_startx = canvas_width / 2 - catcher_width / 2
catcher_starty = canvas_height - catcher_height - 20
catcher_startx2 = catcher_startx + catcher_width
catcher_starty2 = catcher_starty + catcher_height

catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=0)
c.lower(catcher)
game_font = font.nametofont("TkFixedFont")
game_font.config(size=18)


eggs = []

def create_egg():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
    c.lower(new_egg)
    eggs.append(new_egg)
    return x

def move_eggs():
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        c.move(egg,0, 10)
        if egg%20 == 6 or egg%20 == 16:
            c.move(bomb,0,10)
        elif egg%20 == 8 or egg%20 == 18:
            c.move(heart,0,10) 
        elif egg%20 == 10 or egg%20 == 0:
            c.move(apple_red,0,10)
        elif egg%20 == 12 or egg%20 == 2:
            c.move(apple_orange,0,10)
        elif egg%20 == 14 or egg%20 == 4:
            c.move(apple_golden,0,10)
        if eggy2 > canvas_height:
            egg_dropped(egg)
            if egg%20 == 6 or egg%20 == 16:
                gain_a_life()
                c.delete(bomb)
            elif egg%20 == 8 or egg%20 == 18:
                c.delete(heart)
            elif egg%20 == 14 or egg%20 == 4:
                c.delete(apple_golden)
            elif egg%20 == 12 or egg%20 == 2:
                c.delete(apple_orange)
            elif egg%20 == 10 or egg%20 == 0:
                c.delete(apple_red)
    root.after(egg_speed, move_eggs)

def egg_dropped(egg):
    lose_a_life()
    eggs.remove(egg)
    c.delete(egg)
    if lives_remaining == 0:
        messagebox.showinfo("Game Over!", "Final Score: "+ str(score))
        root.quit()

def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))

def gain_a_life():
    global lives_remaining
    lives_remaining += 1
    c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))

def check_catch():
    (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
            if egg%20 == 6 or egg%20 == 16:
                increase_score(egg_score2)
                lose_a_life()
                c.delete(bomb)
            elif egg%20 == 8 or egg%20 == 18:
                gain_a_life()
                c.delete(heart)
            if egg%20 == 14 or egg%20 == 4:
                c.delete(apple_golden)
                increase_score(egg_score1)
            elif egg%20 == 12 or egg%20 == 2:
                c.delete(apple_orange)
                increase_score(egg_score)
            elif egg%20 == 10 or egg%20 == 0:
                c.delete(apple_red)
                increase_score(egg_score)
            eggs.remove(egg)
            c.delete(egg)
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
        c.move(goose, -20, 0)

def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)
        c.move(goose, 20, 0)

#Displays the background picture on the window
background=Image.open("background1.gif")
background=background.resize((810,410))
background=ImageTk.PhotoImage(background)
c.create_image(0,0,anchor='nw',image=background)

#Sets score to zero and creates and displays the textbox that shows the user the score
score = 0
score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: "+ str(score))

#Sets the lives remaining to three and creates and displays the textbook that shows the user their lives remaining
lives_remaining = 3
lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text="Lives: "+ str(lives_remaining))

#Defining the various images
#Displaying Goose image to the useer
Goose=Image.open("crabapple.gif")
Goose=Goose.resize((200,200))
Goose=ImageTk.PhotoImage(Goose)
goose=c.create_image(310,250,anchor='nw',image=Goose)

#Initalizes the golden apple image
Apple_golden=Image.open("crappl (4).gif")
Apple_golden=Apple_golden.resize((300,300))
Apple_golden=ImageTk.PhotoImage(Apple_golden)

#Initalizes the bomb image
bomb=Image.open("Bomb.gif")
bomb=bomb.resize((180,180))
Bomb=ImageTk.PhotoImage(bomb)

#Initalizes the heart image
heart=Image.open("Heart.gif")
heart=heart.resize((250,250))
Heart=ImageTk.PhotoImage(heart)

#Initalizes the red apple image
Apple_red=Image.open("crappl.gif")
Apple_red=Apple_red.resize((300,300))
Apple_red=ImageTk.PhotoImage(Apple_red)

#Initalizes the orange apple image
Apple_orange=Image.open("crappl (3).gif")
Apple_orange=Apple_orange.resize((300,300))
Apple_orange=ImageTk.PhotoImage(Apple_orange)


def Images_based_on_eggs():
    global apple_golden, bomb, heart, apple_red, apple_orange
    x=create_egg()
    for egg in eggs:
        if eggs[-1]==egg:
            x+=25
            if egg%20 == 6 or egg%20 == 16:
                bomb=c.create_image(x,100,image=Bomb)
            elif egg%20 == 8 or egg%20 == 18:
                heart=c.create_image(x,100,image=Heart) 
            elif egg%20 == 10 or egg%20 == 0:
                apple_red=c.create_image(x,100,image=Apple_red)
            elif egg%20 == 12 or egg%20 == 2:
                apple_orange=c.create_image(x,100,image=Apple_orange)
            elif egg%20 == 14 or egg%20 == 4:
                apple_golden=c.create_image(x,100,image=Apple_golden)
    root.after(egg_interval, help)


c.bind("<Left>", move_left)
c.bind("<Right>", move_right)
c.focus_set()
root.after(1000, help)
root.after(1000, move_eggs)
root.after(1000, check_catch)
root.mainloop()

