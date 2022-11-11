### Create Classes ###
"""
Class is a blueprint

Constructor
class Car:
    def __init__(self):
    #initialize attributes

Attribute
class Car:
    def __init__(self, seats):
    self.seats = seats

"""

class User:

    def __init__(self, user_id, username):
        print("new user being create...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
user_1 = User("001", "zern")
user_2 = User("002", "jack")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
