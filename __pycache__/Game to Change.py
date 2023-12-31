"""Pacman, classic arcade game"""

#**********NOTE**********
#This is the code to make changes on, it does not need the comments and they can be deleted
#Changes Ideas: make a timer, have specical dots that give pacman an energy boost, have other things that can kill pacman
#We will then just add the files with the graphics in afterwords




#AP: Importing required elements from various libraries in Python
from random import choice   #AP: Imports choice() method from the random library that randomly selects an item from a specifed sequence
from turtle import *    #AP: Imports all functions from turtle (a graphics interface)
from freegames import floor, vector #AP: Imports the function floor and class vector from feegames (a collection of free Python games)

#AP: Initilizing variables
state = {'score': 0}    #AP: Sets the score visable to the user to zero
path = Turtle(visible=False)    #AP: Sets the arrow that follows 'Paceman' to invisable so that the user can not see it
writer = Turtle(visible=False)  #AP: Sets the arrow at the score board to invisable so that the user can not see it
#pacman1=Turtle
aim = vector(5, 0)  #AP: Determines the dirction 'Pacman' will move in at intial location
pacman = vector(-40, -80)   #AP: Sets 'Pacman' to an intial location
ghosts = [  #AP: Sets the intial staring position of each ghost
    [vector(-180, 160), vector(5, 0)],  #AP: Ghost in the top left
    [vector(-180, -160), vector(0, 5)], #AP: Ghost in the bottom left
    [vector(100, 160), vector(0, -5)],  #AP: Ghost in the top right
    [vector(100, -160), vector(-5, 0)], #AP: Ghost in the bottom right
]
# fmt: off
#AP: Creating size of background. The 0 corrosponds to areas on the game that are black, and the 1 corrosponds to areas on the game that are blue (path that pacman follows)
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on


def square(x, y):   #AP: Draws and fills in a square
    """Draw square using path at (x, y)."""
    path.up()   #AP: Pulls the pen up so that nothing is drawn
    path.goto(x, y) #AP: Moves the pen to the specifed location denoted by (x,y)
    path.down()     #AP: Puts the pen down, so that as pen moves, a line is drawn
    path.begin_fill()   #AP: Initlizies the square to be filled in once it is drawn

    for count in range(4):  #AP: Draws a line 4 times (4 lines in a square)
        path.forward(20)    #AP: Determines the length of the square (20) - moves the pen 20 units forward
        path.left(90)       #AP: Makes the pen turn at a 90 degree angle to create a squre shape

    path.end_fill()     #AP: Fills in the square (black is the defult colour)


def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():    #AP: Draws background
    """Draw world using path."""
    bgcolor('black')    #AP: Makes the entire background colour black
    path.color('blue')  #AP: Makes the path that 'Pacman' follows blue

    #AP: Goes through each tile, and either leaves the tile black or fills the tile in with a blue square
    for index in range(len(tiles)):     #AP: Goes through the index of each tile
        tile = tiles[index]     #AP: uses the index of each tile to determine if it is a 1 or 0 and then sets that value to the variable 'tile' 

        if tile > 0:    #AP: If the index of the tile is 1 draw a sqaure
            x = (index % 20) * 20 - 200     #AP: Determines the x-value of the square's inital position by moving the x value 20 points over for every square, since each square is 20 points in length. 
            #AP: 'index % 20 * 20' determines the size of the tile and all the coloured tiles that came before it (in terms of x starting at x=0), and because there are 200 points to the left and the right of the center, adding '-200' moves the x-value 20 points over from the pervious x value 
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:   #AP: Drwas a white dot if the index of the tile is 1 (areas that have been defined to be the path that pacman follows)
                path.up()   #AP: Pulls the pen up so that nothing is drawn
                path.goto(x + 10, y + 10)   #AP: Moves pen to 10 units over/up from the point where the square started from
                path.dot(2, 'white')    #AP: Draws a white dot on the screen, with size of 2


def move():
    """Move pacman and all ghosts."""
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)
    #pacman.speed(10)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)



    screen.register_shape('OneDrive\Documents\GitHub\CHE-Game\__pycache__\crabapple1.gif')
    turt = Turtle('turtle')
    turt.shape('OneDrive\Documents\GitHub\CHE-Game\__pycache__\crabapple1.gif')
    turt.penup()
    turt.goto(pacman.x + 10, pacman.y + 10)
    turt.pendown()


    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)


def change(x, y):
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

screen = Screen()
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
#bgpic("OneDrive\Documents\GitHub\CHE-Game\__pycache__\crabapple1.gif")
move()
done()
