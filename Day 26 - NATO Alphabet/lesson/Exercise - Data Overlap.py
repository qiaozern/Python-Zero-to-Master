"""
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
You are going to create a list called result which contains the numbers that are common in both files.

e.g. if file1.txt contained:
1
2
3

and file2.txt contained:
2
3
4
result = [2, 3]

IMPORTANT: The result should be a list that contains Integers, not Strings. 
Try to use List Comprehension instead of a Loop.

Example Output
[3, 6, 5, 33, 12, 7, 42, 13]
"""

with open("file1.txt") as file_1:
    data_1 = file_1.readlines()
    
with open("file2.txt") as file_2:
    data_2 = file_2.readlines()
    
result = [int(i) for i in data_1 if i in data_2]

print(result)
