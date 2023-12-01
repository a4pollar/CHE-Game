import turtle
from random import choice   #AP: Imports choice() method from the random library that randomly selects an item from a specifed sequence
from turtle import *    #AP: Imports all functions from turtle (a graphics interface)
from freegames import floor, vector

 
state = {'score': 0}    #AP: Creates a score visable to the user, and sets it equal to zero
path = Turtle(visible=False)    #AP: Creates an arrow that follows 'Paceman', and sets it to invisable so that the user can not see it
writer = Turtle(visible=False)  #AP: Creates an arrow at the score board, and sets it to invisable so that the user can not see it
aim = vector(5, 0)  #AP: Creates a direction vector and sets it to the dirction 'Pacman' will move in at intial location
pacman = vector(-40, -80)   #AP: Creates a vector for 'Pacman' and sets 'Pacman' to an intial location
ghosts = [  #AP: Creates Ghosts and sets the intial staring position of each ghost
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

def square(x, y):   #AP: Draws and fills in a square
    """Draw square using path at (x, y)."""
    path.up()   #AP: Pulls the pen up so that nothing is drawn
    path.goto(x, y) #AP: Moves the pen to the specifed location denoted by (x,y)
    path.down()     #AP: Puts the pen down, so that as pen moves, a line is drawn
    path.begin_fill()   #AP: Initlizies the square to be filled in once it is drawn

    for count in range(4):  #AP: Draws a line 4 times (4 lines in a square)
        path.forward(20)    #AP: Determines the length of the square (20) - moves the pen 20 units forward
        path.left(90)       #AP: Makes the pen turn at a 90 degree angle to create a squre shape

    path.end_fill()     #AP: Fills in the square 


def world():    #AP: Draws background
    """Draw world using path."""
    bgcolor('white')    #AP: Makes the entire background colour black
    path.color('blue')  #AP: Makes the path that 'Pacman' follows blue

    #AP: Goes through each tile, and either leaves the tile black or fills the tile in with a blue square
    for index in range(len(tiles)):     #AP: Goes through the index of each tile
        tile = tiles[index]     #AP: uses the index of each tile to determine if it is a 1 or 0 and then sets that value to the variable 'tile' 

        if tile > 0:    #AP: If the index of the tile is 1 draw a sqaure
            x = (index % 20) * 20 - 200     #AP: Determines the x-value of the square's inital position. This is done by moving the x value 20 units over for every square, since each square is 20 points in length. 
            #AP: 'index % 20 * 20' determines the size of the tile and all the coloured tiles that came before it (in terms of x starting at x=0), and because there are 200 points of game play to the left of the center, adding '-200' moves the x-value to the left side of the screen, instead of the middle of the screen  
            y = 180 - (index // 20) * 20    #AP: AP: Determines the y-value of the square's inital position. This is done by moving the y value 20 units down for every line of tiles created
            #AP: 'index//20' determines the line that the tile is on (the first tiles are on line 1). The '*20' then determines the size tile, plus any tile that comes before it (in terms of y starting at y=0). and because there are 180 units of game play above the cetner, the '180-' part makes the y values start from the top instead of the center
            square(x, y) #AP: Draws sqaures/tiles that start from the top left side of the screen and are 20 units apart from the start position of the pervious square/tile

            if tile == 1:   #AP: Draws a white dot if the index of the tile is 1 (areas that have been defined to be the path that pacman follows)
                path.up()   #AP: Pulls the pen up so that nothing is drawn
                path.goto(x + 10, y + 10)   #AP: Moves pen 10 units over/up from the point where the square started from
                path.dot(2, 'white')    #AP: Draws a white dot on the screen, with size of 2
    addshape('OneDrive\Documents\GitHub\CHE-Game\__pycache__\crabapple1.gif')
    shape('OneDrive\Documents\GitHub\CHE-Game\__pycache__\crabapple1.gif')


world()