'''
Team Activity 2 - discount.py
Abi Priebe
4/22/21
'''
'''
Write a Python program named discount.py that takes a customer's subtotal as input. 
If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must 
subtract 10% from the subtotal. Your program must then compute the total amount due by 
adding sales tax of 6% to the subtotal. Your program must print the discount amount if 
applicable, the sales tax amount, and the total amount due.

Your program must not ask the user to enter the day of the week. Instead, it must get 
the day of the week from your computer's clock. The standard Python datetime module contains 
functions that your program can call to get the current day of the week from your computer's 
clock. The following code example shows how to do that.
'''

# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
current = datetime.now()

# Call the isoweekday() method to get the day
# of the week from the current datetime object.
weekday = current.isoweekday()

# Prompt user for items
subtotal = 0
more_items = "yes"
while more_items.lower() == "yes":
    name = input("What is your item? ")    
    price = float(input(f"How much is {name}? "))
    amount = int(input(f"Enter the quantity of {name}? "))
    more_items = input("Would you like to enter more items? (yes/no) ")
    item_total = price * amount
    subtotal += item_total

#Calculations and print statements
if subtotal >= 50 and (weekday == 2 or weekday == 3):
    discount = subtotal*.1
    subtotal -= discount
    tax = subtotal * 0.06
    total = subtotal + tax
    print(f"Discount amount: {discount:.2f} ")
    print(f"Sales tax amount: {tax:.2f} ")
    print(f"Total: {total:.2f}")

elif subtotal < 50 and (weekday == 2 or weekday == 3):
    difference = 50 - subtotal
    tax = subtotal * 0.06
    total = subtotal + tax
    print(f"Spend ${difference:.2f} more to get a 10% discount!")
    print()
    print(f"Sales tax amount: {tax:.2f} ")
    print(f"Total: {total:.2f}")

else:
    tax = subtotal * 0.06
    total = tax + subtotal
    print(f"Sales tax amount: {tax:.2f} ")
    print(f"Total: {total:.2f}")