### Class Inheritance ###

# This is a main class
class Animal:
    
    def __init__(self):
        self.num_eyes = 2
        
    def breath(self):
        print("Inhale, exhale.")
        
        
# This is an inheritance class
class Fish(Animal):
    
    # super().__init__() to inherit from the main class
    def __init__(self):
        super().__init__()
    
    def breath(self):
        super().breath()
        print("doing this under water.")
    
    def swim(self):
        print("moving in water.")
        
        
nemo = Fish()
nemo.swim()
nemo.breath()

print(nemo.num_eyes)