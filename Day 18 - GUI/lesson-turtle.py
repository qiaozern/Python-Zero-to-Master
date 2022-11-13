import turtle as t
from random import choice, randint

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

# # Draw Square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# # Dashed Line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# # Draw Polygon with random color
# colors = ["red", "green", "blue", "yellow", "black", "orange", "purple", "navy"]

# def draw_polygon(num_shape):
#     for i in range(3, num_shape+1):
#         tim.color(choice(colors))
#         angel = 360 / i
#         for _ in range(i):
#             tim.forward(100)
#             tim.right(angel)

# draw_polygon(10)

# # Random walk
# def random_walk(times):
#     tim.speed("fastest")
#     tim.pensize(10)
#     angels = [0, 90, 180, 270]
#     for _ in range(times):
#         rand_angel = choice(angels)
#         tim.color(random_color())
#         tim.forward(50)
#         tim.setheading(rand_angel)

# random_walk(200)

# Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
    
screen = t.Screen()
screen.exitonclick()