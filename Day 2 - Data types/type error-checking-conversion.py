# type error
#len(4567) # TypeError: object of type 'int' has no len()

# num_char = len(input("What is your name?\n"))
# print(f"Your name has {num_char} characters.")

# print(type(num_char)) # int

# new_num_char = str(num_char) # type casting
# print(f"Your name has {new_num_char} characters.")

a = float(123)
print(type(a)) # float

print(70 + float("100.5")) # 170.5
print(str(70) + str(100)) # 70100