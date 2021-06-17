'''
Prove 1 - tire_volume.py
Abi Priebe
4/24/21
'''
'''
Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes 
and outputs the volume of space inside that tire.
'''
import math as math

# prompt user for variables
width = int(input("Enter the width of the tire in mm (ex 205): "))
ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# compute the volume
volume = math.pi * width**2 * ratio * (width * ratio + 2540*diameter) / 10000000

# print the volume - round to one decimal place
print(f"The approximate volume is {volume:.1f} milliliters.")