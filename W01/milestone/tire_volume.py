import math

# Ask a tire width in mm
w = int(input("Enter the width of the tire in mm (ex 205): "))

# Ask the aspect ratio
a = int(input("Enter the aspect ratio of the tire (ex 60): "))

# Ask the diameter of the wheel in inches
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Tire's volume
v = (math.pi * (w**2) * a * ((w * a) + (2540 * d))) / 10000000000
print(f"The approximate volume is {v:.2f} liters")