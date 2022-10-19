"""
Year 2000
2000 / 4 = 500 (Leap Year)
2000 / 100 = 20 (Not Leap)
2000 / 400 = 5 (Leap Year)
"""

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap")
    else:
        print("Leap year")
else:
    print("Not Leap")