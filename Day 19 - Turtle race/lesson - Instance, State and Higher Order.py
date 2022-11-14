from turtle import Turtle, Screen

kanny = Turtle()
screen = Screen()

def move_forward():
    kanny.forward(10)

def move_backward():
    kanny.backward(10)
    
def turn_left():
    new_heading = kanny.heading() + 10
    kanny.setheading(new_heading)
    
def turn_right():
    new_heading = kanny.heading() - 10
    kanny.setheading(new_heading)
    
def clear_screen():
    kanny.clear()
    kanny.penup()
    kanny.home()
    kanny.pendown()
    
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()