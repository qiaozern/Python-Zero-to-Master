"""
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is x, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is y, you are alright together."

Otherwise, the message will just be their score e.g.:
"Your score is z."
"""


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
lower_name = combined_name.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u +e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l + o + v + e

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")