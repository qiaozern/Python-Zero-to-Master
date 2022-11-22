# Absolute file path is always relative to the root of the computer.
# Relative file path is relative to current directory.

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# mode "r" (default) read, "w" write, "a" append
# if there is no file name, it will create a new file from scratch.

# with open("my_file.txt", mode="a") as file:
#     file.write("New text.")

with open("../../../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)