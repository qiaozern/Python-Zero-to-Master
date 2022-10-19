# if-elif-else/nested-if-else statement
print("Welcome to the rollercoasteer!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child ticket are $5.")
        bill = 5
    elif age <=18:
        print("Youth ticket are $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult ticket are $12.")
        bill = 12
    
    want_photo = input("Do you want a photo taken? Y or N")
    if want_photo == "Y":
        # Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")

