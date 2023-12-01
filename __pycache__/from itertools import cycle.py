from itertools import cycle     #AAP: importing cycle from itertools to create a colour cycle
from random import randrange  #AAP: importing randrange from random to generate random numbers
from tkinter import Canvas, Tk, messagebox, font #AAP: importing Tinkter modules

canvas_width = 800  #AAP: setting up canvas width
canvas_height = 400 #AAP: setting up canvas height

root = Tk() #AAP: creates Tinkter window
root.title("Egg Catcher") #AAP: titles the window
c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue") #AAP: creates a canvas with a specified width, height, and background colour
c.create_rectangle(-5, canvas_height-100, canvas_width+5, canvas_height+5, fill="sea green", width=0) #AAP: creates a sea green rectangle to represent the grass
c.create_oval(-80, -80, 120, 120, fill='orange', width=0) #AAP: creates an orange oval to represent the sun
c.pack() #AAP: packs the canvas into the Tinkter window

color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"]) #AAP: defines a colour cycle for the eggs
egg_width = 45 #AAP: width of the eggs
egg_height = 55 #AAP: height of the eggs
egg_score = 10 #AAP: score per egg collected
egg_speed = 500 #AAP: speed that eggs fall at
egg_interval = 4000 #AAP: interval between egg drops
difficulty = 0.95 #AAP: level of difficulty
catcher_color = "blue" #AAP: colour of the catcher
catcher_width = 100 #AAP: width of the catcher
catcher_height = 100 #AAP: height of the catcher
catcher_startx = canvas_width / 2 - catcher_width / 2 #AAP: starting x coordinate of the catcher
catcher_starty = canvas_height - catcher_height - 20 #AAP: starting y coordinate of the catcher
catcher_startx2 = catcher_startx + catcher_width #AAP: ending x coordinate of the catcher
catcher_starty2 = catcher_starty + catcher_height #AAP: ending y coordinate of the catcher

catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=3) #AAP: creating the catcher on the canvas
game_font = font.nametofont("TkFixedFont") #AAP: retrieving the Tinkter fixed font
game_font.config(size=18) #AAP: setting a size for the font


score = 0 #AAP: sets intial score
score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: "+ str(score)) #AAP: displays score on canvas

lives_remaining = 3 #AAP: sets initial number of lives
lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text="Lives: "+ str(lives_remaining)) #AAP: displays number of lives on canvas

eggs = []

def create_egg():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)

def move_eggs(): #AJ: Function moves eggs down the screen
    for egg in eggs: #AJ: Creates a loop that will go through every egg in the list 'eggs'
        (eggx, eggy, eggx2, eggy2) = c.coords(egg) #AJ: Retrieves the coordinates off the boundaries of the eggs. It gets the x and y coordinates of the top-left and bottom-right corner.
        #print(c.coords(egg)) #AJ: 
        c.move(egg,0, 10)  #AJ: This moves the egg down the canvas. The first item is what needs to be moved down, the second is the x-coordinate, which should remain the same, and lastly, the y-coordinate will move down by 10 pixels.
        if eggy2 > canvas_height: #AJ: Checks if the bottom corner of the egg has gone greater than/beyond the height of the canvas. This checks if the egg has reached the bottom.
            egg_dropped(egg) #When the egg has reached the bottom, the egg drop function will be called. This will get rid of the egg, take away a life from the player and check if the game is done. (The player has ran out of lives)
    root.after(egg_speed, move_eggs) #After a specific time, this function is called again to move another egg, creating a loop.

def egg_dropped(egg): #AJ: Defines the parameter for the egg that has reached the bottom
    eggs.remove(egg) #AJ: Removes the eggs the egg list, which is used to track all the eggs on the canvas at the time.
    c.delete(egg) #AJ: Removes the egg from the canvas (the graphical representation of the egg)
    lose_a_life() #Calls the lose_a_life function to indicate that the player has lost a life.
    if lives_remaining == 0:    #AJ: Sets a condition for when the player runs out of lives (If the lives_remaining is = 0, then they have ran out)
        messagebox.showinfo("Game Over!", "Final Score: "+ str(score)) #AJ: A message will appear on the screen telling the player that the game is over, including their final score. To do this, the score will be converted into a string so it can be displayed with the other text.
        root.destroy() #AJ: Closes the game window since the game is over

def lose_a_life(): #Takes a life away by  an increment of 1 whenever the egg doesnt fall in the basket
    global lives_remaining #AJ: Changes the lives_remaining variable from a local to a global variable, so we can call on it throughout the code
    lives_remaining -= 1 #Reduces the lives_remaining value by 1, showing that a player has lost a life.
    c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining)) #Updates the value of lives remaining on the screen. It updates the displayed text on the canvas where it says 'Lives' and it does this by converting the numerical value of remaining lives into a string.

def check_catch(): # VK This function checks for when collisions occur between the lists 'catcher' and 'egg'
    (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher) #VK assigns the top left and bottom right coordinates of the catcher on the canvas ????
    for egg in eggs: # VK Checks each index in the this list 
        (eggx, eggy, eggx2, eggy2) = c.coords(egg) #VK simalary to the catcher coords, this assigns the coords of the egg on the canvas ???
        if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40: # VK checks whether if the eggs width falls within the catchers width and checks if the vertical range is close enough
            eggs.remove(egg) # VK if this is true then it removes the egg from the screen ??
            c.delete(egg) # VK Deletes from history
            increase_score(egg_score) # VK Increases the score
    root.after(100, check_catch) # VK Schedules function to reoccur this function after 100ms 

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
