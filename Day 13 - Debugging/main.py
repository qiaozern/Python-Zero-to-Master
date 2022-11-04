### Debugging ###

# # Describe Problem
# def my_function():
#     for i in range(1, 21): # range of 1, 20 is not include 20
#         if i == 20:
#             print("You got it")
# my_function() 

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) # list index begin with 0
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: # 1981 - 1993
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)

# mutate([1,2,3,5,8,13])

"""
Debugging Tips
1). Describe the problem
2). Reprodue the bug
3). Play Computer
4). Fix the errors
5). Print is your friend
6). Use a debugger
7). Take a break
8). Ask a friend
9). Run often
10). Ask StackOverflow
"""