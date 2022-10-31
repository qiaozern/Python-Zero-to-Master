### Function with outputs
"""
def my_function():
    return 3 * 2
"""

def format_name(f_name, l_name):
    # Docstring => describe the function
    """Take a first and last name and format it 
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_fname = f_name.title()
    formated_lname = l_name.title()
    return f"{formated_fname} {formated_lname}"

print(format_name(input("What is your first name? "), 
                  input("What is your last name? ")))

format_name()
