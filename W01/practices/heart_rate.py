"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
# Get input from a user
age = int(input("Please enter your age: "))

# Maximum Heart Rate per minute
heart_rate = 220 - age

# Lower heart rate
lower = (heart_rate * 65) / 100

# Higher heart rate
higher = (heart_rate * 85) / 100

# Display the results
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {lower:.0f} and {higher:.0f} beats per minute.")