"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()

def to_the_moon():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def walking():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

### break an infinite loops
while front_is_clear():
    move()

### Maze
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

### Hurdle 4
#while not at_goal():
#    if wall_in_front():
#        walking()
#    else:
#        move()
        
### Hurdle 3        
#while not at_goal():
#    while front_is_clear():
#        move()
#    walking()

### Hurdle 2
#while at_goal() != True:
#    to_the_moon()

### Hurdle 1
#for i in range(6):
#    to_the_moon()
"""