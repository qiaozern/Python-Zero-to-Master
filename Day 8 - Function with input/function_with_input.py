"""
# Functions with inputs
def my_function(something):
    #Do this with something
    #Then do this
    #Finally do this
    
my_function(123) #call function
"""

# Function

# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
        
# greet()


# Function that allows for input

# def greet_with_name(name):
#     print(f"Hello {name}!")
#     print("How do you do?")

# greet_with_name("Zern")


# Function with more than 1 input

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
    
# greet_with("Zern", "Bangkok")


"""
Positional Arguments

def my_function(a, b, c):
    #Do this with a
    #Then do this with b
    #Finally do this with c
    
my_function(3, 1, 2)

# Keyword arguments
my_function(c=3, b=1, a=2)
"""

# Functions with keywords Arguments
def greeting(name, location):
    print(f"Hello {name}!")
    print("What is it like in {location}")
    
greeting(location="Bangkok", name="Zern")