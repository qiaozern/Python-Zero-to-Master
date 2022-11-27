### List comprehension ###
numbers = [1,2,3]
name = "Qiaozern"

# # For loop
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)


# This is list comprehension
### new_list = [new_item for item in list] ###
### new_list = [letter for letter in name] ###
new_list = [n + 1 for n in numbers]
letter_list = [letter for letter in name]

range_list = [i*2 for i in range(1,5)]

# Conditional list comprehension
### new_list = [new_item for item in list if test] ###
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [n for n in names if len(n) < 5]

long_names = [n.upper() for n in names if len(n) > 5]


### Dictionary Comprehension ###
### new_dict = {new_key:new_value for (key,value) in dict.items() if condition} ###
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student:random.randint(1,100) for student in names}
# passed_student = {student:student_scores[studen] for student in student_scores if student_scores[student] >= 60}
passed_student = {student:score for (student,score) in student_scores.items() if score >= 60}

# print(student_scores)
# print(passed_student)

######################################################################################################################################################

### Loop through pandas ###

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key,value) in student_dict.items():
#     print(key)
#     print(value)

import pandas as pd

student_df = pd.DataFrame(student_dict)
# print(student_df)

# # Loop through a data frame
# for (key,value) in student_df.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_df.iterrows():
    # print(row.student)
    # print(row.score)
    if row.student == 'Angela':
        print(row.score)
        