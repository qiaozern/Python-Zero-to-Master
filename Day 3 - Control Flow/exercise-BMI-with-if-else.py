height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

"""
Under 18.5 they are underweight.
Over 18.5 but below 25 they have a normal weight.
Over 25 buy below 30 they are over weight.
Over 30 but below 35 they are obese.
Above 35 they are clinically obese.
"""

bmi = weight/(height**2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")