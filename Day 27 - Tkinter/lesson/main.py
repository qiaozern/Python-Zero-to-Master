"""
Tkinter known as Graphical User Interface(GUI)

Advanced Python Arguments

Default Arguments
*Args
**Kwargs

## Keyword Arguments ##
def my_function(a,b,c):
    #Do this with a
    #Then do this with b
    #Finally do this with c
    
my_function(c=3,a=1,b=2)

## Arguments with Default Values ##
def my_function(a=1,b=2,c=3):
    #Do this with a
    #Then do this with b
    #Finally do this with c
    
my_function() # This will give the same value as above

*args: Many Positional Arguments
## Unlimited Arguments ##
def add(*args):
    for n in args:
        print(n)

add(3,5,7,8)

**kwargs: Many Keyworded Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
"""

from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0,row=0) # relative to the other components
my_label.config(padx=50, pady=50)

# Button

def button_click():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_click)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="Click Here")
new_button.grid(column=2,row=0)

# Entry component
input = Entry(width=10)
# input.pack()
print(input.get())
input.grid(column=3,row=2)



# Keep window on screen
window.mainloop()

