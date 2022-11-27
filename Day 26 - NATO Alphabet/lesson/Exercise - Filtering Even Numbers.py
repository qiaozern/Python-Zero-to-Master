"""
You are going to write a List Comprehension to create a new list called result. 
This new list should only contain the even numbers from the list numbers.

DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

Example Output
[2, 8, 34]
"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [i for i in numbers if i % 2 == 0]

print(result)