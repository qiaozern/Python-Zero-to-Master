import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# using random
chosen = random.choice(names)

"""# alternative way
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
chosen = names[random_choice]"""

print(f"{chosen} is going to buy the meal today!")