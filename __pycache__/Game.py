"""Pacman, classic arcade game"""

#AP: Importing required elements from various libraries in Python
from random import choice   #AP: Imports choice() method from the random library that randomly selects an item from a specifed sequence
from turtle import *    #AP: Imports all functions from turtle (a graphics interface)
from freegames import floor, vector #AP: Imports the function floor and class vector from feegames (a collection of free Python games)

#AP: Initilizing variables
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

    path.end_fill()     #AP: Fills in the square 


def offset(point): #AJ: Converts cartesian coodrinates(x,y) of a point to the index in a 1D list. Representing/Defining the tiles on the game grid.
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20 #AJ: In the x-direction: A point is a vector quantity in game and the floor function "grounds" the x-coordinate to the closest multiple of 20 (tiles are 20 units in length). Estimates this x-coordinate to the nearest horizontal gridline. This makes sure that Pacman moves to the nezt valid Horizontal tile. The +200, is used to make sure the resulting coordinate is positive.
    y = (180 - floor(point.y, 20)) / 20 #AJ: In the y-direction. Grounds the y-coordinate to the nearest multiple of 20, estimates the y-coordinate to the nearest vertical gridline. This ensures that Pacman moves to the next valid vertical tile. The +200, is used to make sure the resulting coordinate is positive.
    index = int(x + y * 20)     #AJ: Combines the x and y to get it overall in 1 Dimensional space
    return index    #AJ: Returns the index


def valid(point):   #AP: Returns True or False based on whether a point is within the tiles that 'Pacman' and other game characters are contained to
    """Return True if point is valid in tiles."""
    index = offset(point)   #AP: Obtains the coordinate of a point in terms of is index in a 1D list

    if tiles[index] == 0:   #AP: Finds if the point is a '1' or a '0' based off it's index in the list denoted as 'tiles' and checks to see if it equals zero
        return False        #AP: If the point is a '0', it is not in a valid tile (tiles that do not compose the path that 'Pacman' can take), and so False is returned 

    #AP: There are multiple points within a valid tile, however because 'Pacman'/Ghosts are shown to take up an entire tile to the user, it is possiable for 'Pacman'/Ghosts to be at a point in a valid tile when from the screen it looks like they are not in a valid tile
    #AP: To deal with this, the index of a point in tile above/to the right of the tile 'Pacman'/Ghosts are in is determined and then checked to see if it is in a valid tile
    index = offset(point + 19)  #AP: Adds 19 to the x and y values of the point. Each tile of 20 spaces apart, so adding 19 to a point in the tile (starting 1 unit in) gets to the coordinates of the next tile

    if tiles[index] == 0:   #AP: Checks to see if the point above/to the left of the ogrinal point is an invalid tile
        return False        #AP: If the point above/to the left is an invalid tile, False is returned

    return point.x % 20 == 0 or point.y % 20 == 0   #AP: Returns True if either the x or y value is a multiple of 20. Since there are no diagonal lines and the tiles/squares are in increments of 20, if either of these conditions are met and the other two 'if statements' are Tue, 'Pacman'/Ghosts will be be shown on the screen to be in a valid tile 


def world():    #AP: Draws background
    """Draw world using path."""
    bgcolor('black')    #AP: Makes the entire background colour black
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


def move():    #AJ: Move function responsible for moving Pacman and the ghosts
    """Move pacman and all ghosts."""
    writer.undo()     #AJ: Undos the last action done by the 'write' turtle. In this context, turtle is responsible for displaying the score on the screen so it clears out the old score and updates the new one.
    writer.write(state['score']) # AJ: Displays/Writes the updated score onto the user's screen

    clear()    #AJ: Clears the entire drawing before a new one appears on the screen

    if valid(pacman + aim): #AJ: Pacman + aim calculates the new position of Pacman by adding the original position plus the direction vector(aim). The valid function ensures that Pacman is within the boundaries of the game and in a clear position.
        pacman.move(aim)    #AJ: If the new position is valid, Pacman can move to the 'aim' direction vector

    index = offset(pacman)     #AJ: Locating the index of the position time that Pacman is on using the offset function

    if tiles[index] == 1:   #AJ: It is checking if the tile on this index has a value of one. This is used to indicate if there is a 'Pac-dot' on this tile
        tiles[index] = 2    #AJ: If condition above is true, this shows that Pacman has eaten this dot, since tiles[index] = 2 , most likely represents the point where a tile where a dot has been eaten.
        state['score'] += 1 #AJ: Adds 1 point to the scoreboard a Pac-dot is eaten
        x = (index % 20) * 20 - 200  #AJ: The remainder function is used to give the horizontal grid position of the dot. It is multiplied by 20 so it can scale this position in the x-direction across the pixel coordinates displayed on the screen. Lastly, subtracting 20 is used for alignment, aligning the leftmost point to the leftmost column on the grid. Overall, the x represents the horizontal coordinates on the screen where the dot should be.
        y = 180 - (index // 20) * 20 #AJ: The integer division gives vertical position of the dot on the grid (rows). When multiplying it by 20, it scales this position in the y-direction across the pixel coordinates displayed on screen. Subtracting scaled y-position by 180 flips the coordinates since typical graphical coordinates have positive y going down.   
        square(x, y) #AJ: Calls the square function where it will fill up a square in those coordinates to represent a consumed Pac-dot.
        
    up() #AJ: Lifts the pen off
    goto(pacman.x + 10, pacman.y + 10) #AJ: Shifts the turtle slightly offset from Pacman's original position
    dot(20, 'yellow')     #AJ: Draws Pacman as a yellow dot

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


def change(x, y):        #AAP: Change function responsible for changing the way the pacman faces, this function uses x and y to represent the change in x and y coordinates
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)):   #AAP: This function creates a vector using x and y coordinates, then adds the vector to the current position of the pacman
        aim.y = y       #AAP: if the new position is valid, the y component of the aim vector is set to the new y component


setup(420, 420, 370, 0)  #AAP: Using the turtle module, this sets up the turtle window with a width and height of 420 pixels, and the window is positioned at coordinates (370,0)
hideturtle()             #AAP: Hides the turtle cursor
tracer(False)            #AAP: Turns off the animation rendering
writer.goto(160, 160)    #AAP: Sets up a turtle and positions it at (160,160)
writer.color('white')    #AAP: Colours the turtle white
writer.write(state['score']) #AAP: States the score of the player
listen()                 #AAP: Makes the turtle window listen for keyboard events
onkey(lambda: change(5, 0), 'Right') #AAP: Uses the onkey function to bind pressing the right arrow key to the change(5, 0) function
onkey(lambda: change(-5, 0), 'Left') #AAP: Uses the onkey function to bind pressing the left arrow key to the change(-5, 0) function
onkey(lambda: change(0, 5), 'Up')    #AAP: Uses the onkey function to bind pressing the up arrow key to the change(0, 5) function
onkey(lambda: change(0, -5), 'Down') #AAP: Uses the onkey function to bind pressing the down arrow key to the change(0, -5) function
world()                 #AAP: Draws the background
move()                  #AAP: Function that moves Pacman and the ghosts
done()                  #AAP: Keeps the window open until the user closes it
