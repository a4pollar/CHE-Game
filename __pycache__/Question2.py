import turtle
 
def generate_pacman():
    """Generates a pacman using turtle graphics.
 
    Args:
        None
 
    Returns:
        None
    """
    # Create a turtle object
    pacman = turtle.Turtle()
 
    # Set the speed of the turtle
    pacman.speed(10)
 
    # Set the shape of the turtle
    pacman.shape("circle")
 
    # Set the color of the turtle
    pacman.color("yellow")
 
    # Set the starting position of the turtle
    pacman.penup()
    pacman.setpos(0, 0)
 
    # Draw the pacman
    pacman.pendown()
    pacman.begin_fill()
    pacman.circle(50, steps=30)
    pacman.end_fill()
 
    # Hide the turtle
    pacman.hideturtle()
 
if __name__ == "__main__":
    generate_pacman()



#import classroom

#print(classroom.get_example_data())


