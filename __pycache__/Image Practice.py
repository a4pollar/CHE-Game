from random import choice   #AP: Imports choice() method from the random library that randomly selects an item from a specifed sequence
from turtle import *    #AP: Imports all functions from turtle (a graphics interface)
from freegames import floor, vector
writer = Turtle(visible=False)

import turtle
tr = turtle.Turtle()
wn = turtle.Screen()
wn.register_shape("OneDrive\Documents\GitHub\CHE-Game\__pycache__\crabapple1.gif")
tr.shape("OneDrive\Documents\GitHub\CHE-Game\__pycache__\crabapple1.gif")
wn.mainloop()

def move():
    """Move pacman and all ghosts."""

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        #square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    register_shape('OneDrive\Documents\GitHub\CHE-Game\__pycache__\crabapple1.gif')
    shape('OneDrive\Documents\GitHub\CHE-Game\__pycache__\crabapple1.gif')
    #dot(20, 'yellow')

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
