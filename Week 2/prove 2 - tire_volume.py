'''
Prove 2 - tire_volume.py
Abi Priebe
5/1/21
'''
'''
The previous lesson's prove assignment required you to write a program named tire_volume.py that 
computes the approximate volume of air inside a tire. Add code near the end of that program that 
does the following:

1. Gets the current date from the computer's clock.
2. Opens a text file named volumes.txt for appending.
3. Appends to the end of the volumes.txt file one line of text that contains the following five values:
    a. current date
    b. width of the tire
    c. aspect ratio of the tire
    d. diameter of the wheel
    e. volume of the tire
'''

# Import necassary libraries
from datetime import date
import math as math

# prompt user for variables
width = int(input("Enter the width of the tire in mm (ex 205): "))
ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# compute the volume
volume = math.pi * width**2 * ratio * (width * ratio + 2540*diameter) / 10000000

# print the volume - round to one decimal place
print(f"The approximate volume is {volume:.1f} milliliters.")
purchase = input("Would you like to purchase tires with these dimensions? (yes/no) ")
if purchase.lower() == "yes":
    phone_number = input("Please enter your phone number: ")
    print("Someone will be in contact with you soon to help you conduct that purchase!")
else:
    print("Have a great day!")

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
current_date = date.today()

# Opens a text file named volumes.txt for appending.
with open("volumes.txt", "wt") as file:
    # Print the date and tire dimensions to the file.
    print(f"{current_date}, {width}, {ratio}, {diameter}, {volume:.1f}", file=file)
    if purchase.lower() == "yes":
        print(f"{phone_number}", file=file)