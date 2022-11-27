# *args: Many Positional Arguments
### Unlimited Positional Arguments ###
def add(*args):
    return sum(args)
    
#     print(args[0])
    
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# add(1,2,3,4,5)


# **kwargs: Many Keyworded Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    

calculate(2, add=3, multiply=5)


class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seat = kw.get("seat")
        
my_car = Car(make="Tesla", model="Model 3", color="black", seat="4")
print(my_car.make)
print(my_car.model)