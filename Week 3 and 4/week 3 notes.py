# printing a string literal
print("hi there!")

# printing a variable whose value is a string
y = "hi there!"
print(y)

# more practice with functions
# volume function
def ComputeVolume(l,w,h):
    return l * w * h

def DisplaySomething(user_value):
    print(user_value) #lol

x=5
DisplaySomething(ComputeVolume(x,2,7))

#Changing a global variable within a function
a = 100
def ChangeGlobalVariableWithinFunction():
    global a
    a = 500
ChangeGlobalVariableWithinFunction()
print(a)

# Returning multiple things
def ReturnMultipleThings():
    b=1
    c=2
    return b,c

d,e = ReturnMultipleThings()
print(d)
print(e)