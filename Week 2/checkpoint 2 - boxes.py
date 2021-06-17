'''
Checkpoint 2 - boxes.py
Abi Priebe
4/27/21
'''

'''
A manufacturing company needs a program that will help its employees pack manufactured 
items into boxes for shipping. Write a Python program named boxes.py that asks the user 
for two integers:  1) the number of manufactured items and 2) the number of items that 
the user will pack per box. Your program must compute and print the number of boxes 
necessary to hold the items. This must be a whole number. Note that the last box may be 
packed with fewer items than the other boxes.
'''

# import libraries
import math

# build a function that computes the number of boxes necessary
def numberOfBoxes(items, itemsPB):
    return math.ceil(items/itemsPB)

# prompt the user the number of items and number of items per box
items = int(input('Enter the number of items: '))
itemsPB = int(input('Enter the number of items per box: '))

# display the answer
print(f'For {items} items, packing {itemsPB} items in each box, you will need {numberOfBoxes(items,itemsPB)} boxes.')