#if statements
x = 5
y = 6
print(x < y)

favoriteNumbersList = [3,4,5,6,7,8]

if (4 in favoriteNumbersList):
    print("this was true")

if (10 not in favoriteNumbersList):
    print("this was true")

name = "Joey"
if("j" in name):
    print("J is in the name")
else:
    print("j is not in the name")

print(x < y and y < 3)
print(x < y or y < 3)

#error checking - repeating commands/traversing data
userWantsMore = True
while(userWantsMore):
    userInput = input("Do you have another tire? (y/n)")
    if(userInput == "n"):
        userWantsMore = False #you could also use break here

#functions
import math

def computeCircumference(radius):
    return 2 * math.pi * radius

userRadius = float(input("Please enter a radius: "))
print(computeCircumference(userRadius))