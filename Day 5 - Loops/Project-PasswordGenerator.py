#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

### Easy level ###
# password_gen = ""

# for i in range(1, nr_letters + 1):
#     password_gen += random.choice(letters)
# for j in range(1, nr_symbols + 1):
#     password_gen += random.choice(symbols)
# for k in range(1, nr_numbers + 1):
#     password_gen += random.choice(numbers)

# print(password_gen)

### Hard level ###
password_list = []

for i in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for j in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for k in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
shuffle_password = random.shuffle(password_list)
print(password_list)

shuffle_pass = ""
for char in password_list:
    shuffle_pass += char
    
print(shuffle_pass)


"""
or there is another way
password_list = []

for i in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for j in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for k in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
new_pass = "".join(password_list)
print(new_pass)
"""

