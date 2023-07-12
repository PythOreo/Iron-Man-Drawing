# Importing the turtle & sleep modules
import turtle
from time import sleep

# Defining the coordinates of the face parts
face_one = [[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170,10), (-150, -10), (-140, 10), (-40, -20),
(0, -20)], [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120),
(0, 120)]]

face_two = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230),
(-64, -210), (0, -210)], [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),
(100, -46), (50, -40), (40, -30), (0, -30)]]

face_three = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],
[(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220), (0, -220)]]

# Hide the turtle cursor
turtle.hideturtle()

# Choose the title of the window
turtle.title("Iron Man Draw")

# Set the background color
turtle.bgcolor("#ba161e") # Red

# Set the window size(Height & Width)
turtle.setup(500, 600)

# Define the starting coordinates of the face parts
face_one_start = (0, 120)
face_two_start = (0, -30)
face_three_start = (0, -220)

# Drawing speed
turtle.speed(1)

# Function to draw the face parts
def draw_face(face_details, start):

    # Stop drawing
    turtle.penup()
    
    # Go to the start postions
    turtle.goto(start)
    
    # Start drawing
    turtle.pendown()
    
    # The pen color
    turtle.color("#fab104") #Yellow
    
    # Actually I can't describe this function, Go check the documentations 
    turtle.begin_fill()

    # Creating a for loop to Make the pen moves
    for i in range(len(face_details[0])):
        x, y = face_details[0][i]
        turtle.goto(x, y)

    for i in range(len(face_details[1])):
        x, y = face_details[1][i]
        turtle.goto(x, y)

    # Actually I can't describe this function too, Go check the documentations
    turtle.end_fill()

# Calling the function to draw face parts
draw_face(face_one, face_one_start)
draw_face(face_two, face_two_start)
draw_face(face_three, face_three_start)

# Sleep for 10 seconds to see the face after drawing before the window closes
sleep(10)
