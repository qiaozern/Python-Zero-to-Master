number_of_list = 0
sum_height = 0

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below 👇
for height in student_heights:
    sum_height += height
    number_of_list += 1
    
average_height = round(sum_height / number_of_list, 0)
print(average_height)
