import math
from datetime import datetime

# Datetime now
current = datetime.now(tz=None)

# Ask a tire width in mm
w = int(input("Enter the width of the tire in mm (ex 205): "))

# Ask the aspect ratio
a = int(input("Enter the aspect ratio of the tire (ex 60): "))

# Ask the diameter of the wheel in inches
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Tire's volume
v = (math.pi * (w**2) * a * ((w * a) + (2540 * d))) / 10000000000

price = 0
out_of_range = False

# Determine the price based on tire size
if w == 195:
    if a == 55:
        if d == 15:
            price = 95.00
        else:
            out_of_range = True
    else:
        out_of_range = True
elif w == 205:
    if a == 50:
        if d == 17:
            price = 125.00
        else:
            out_of_range = True
    elif a == 55:
        if d == 16:
            price = 110.00
        else:
            out_of_range = True
    elif a == 60:
        if d == 16:
            price = 118.00
        else:
            out_of_range = True
elif w == 215:
    if a == 55:
        if d == 16:
            price = 120.00
        else:
            out_of_range = True
    else:
        out_of_range = True
elif w == 225:
    if a == 35:
        if d == 18:
            price = 185.00
        else:
            out_of_range = True
    elif a == 40:
        if d == 18:
            price = 150.00
        else:
            out_of_range = True
    elif a == 55:
        if d == 17:
            price = 145.00
        else:
            out_of_range = True
    else:
        out_of_range = True
else:
    out_of_range = True

if not out_of_range:
    print(f"Tire size: {w}/{a}R{d}\tApproximate Volume: {v:.2f} liters\tPrice: ${price}")

    user_answer = input("Would you like to buy this tire size? (yes/no): ").lower()

    if user_answer == "yes":
        phone_number = input("Please enter your phone number: ")
        # Log the information in a text file
        with open("volume.txt", mode="at") as volumes_file:
            print(f"{current:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {phone_number}", file=volumes_file)
        print("Thank you for your purchase!")
    else:
        print("No problem, have a great day!")
else:
    print("Sorry, we don't have that tire size.")    
