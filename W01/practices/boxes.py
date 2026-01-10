import math

# The number of manufactured items
items = int(input("Enter the number of items: "))

# The number of items that the user will pack per box
per_box = int(input("Enter the number of items per box: "))

# Number of boxes needed
boxes = math.ceil(items / per_box)

# Display
print(f"For {items} items, packing {per_box} items in each box, you will need {boxes} boxes.")