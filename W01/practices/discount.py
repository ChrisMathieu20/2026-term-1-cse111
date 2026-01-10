from datetime import datetime

# The current date and time
current = datetime.now()
day_of_week = current.weekday()
days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}
today = ""
if day_of_week == 0:
    today = days[day_of_week]
elif day_of_week == 1:
    today = days[day_of_week]
elif day_of_week == 2:
    today = days[day_of_week]
elif day_of_week == 3:
    today = days[day_of_week]
elif day_of_week == 4:
    today = days[day_of_week]
elif day_of_week == 5:
    today = days[day_of_week]
elif day_of_week == 6:
    today = days[day_of_week]
subtotal = 0
qty = 1

while qty != 0:
    price = float(input("Enter the price: "))
    qty = int(input("Enter the quantity: "))
    amount = price * qty
    subtotal += amount

print(f"\nToday is {today}")

print(f"Subtotal: ${subtotal:.2f}")

if today == "Tuesday" or today == "Wednesday":
    if subtotal >= 50:
        discount = (subtotal * 10) / 100
        print(f"Discount: ${discount:.2f}")
        subtotal -= discount
    elif subtotal < 50:
        difference = 50 - subtotal
        print(f"You are near than ${difference} to receive a discount.")

tax = (subtotal * 6) / 100
print(f"Taxes: ${tax:.2f}")

total_amount = subtotal + tax
print(f"Total amount: ${total_amount:.2f}")