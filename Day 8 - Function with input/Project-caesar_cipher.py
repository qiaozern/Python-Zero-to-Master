alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}.")


#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

        

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

    shift %= 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    # input Yes or No to continue or stop the function
    result = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    # condition to continue or stop
    if result == 'no':
        should_continue = False
        print("Goodbye.")






"""
def encrypt(plain_text, shift_amount):
    # create cipher_text to contain encoded text
    cipher_text = ""
    # loop through the plain_text to find an index of each letter in alphabet and plus the shift amount to encode and return cipher_text
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

def decode(cipher_text, shift_amount):
    # create plain_text variable to contain decoded text
    plain_text = ""
    # loop through the cipher_text to find an index of each letter in alphabet and minus the shift amount to decode and return the plain_text
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decode(cipher_text=text, shift_amount=shift)
else:
    print("Please choose encode or decode.")
    """