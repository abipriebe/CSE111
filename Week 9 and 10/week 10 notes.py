import math

def main():
    circleCount = getNumberOfCircles()
    areas = circleLoop(int(circleCount))
    displayAreas(areas)

def getNumberOfCircles():
    while True:
        try:
            return float(input('How many circles are you working with? '))
        except:
            print('Something went wrong.')

def circleLoop(circleCount):
    areas = []
    for _ in range(circleCount):
        radius = getRadius()
        areas.append(computeCircleArea(radius))
    return areas

def displayAreas(areas):
    zeros = '.2f'
    roundedAreaList = [f"{a:,{zeros}}" for a in areas]
    print(roundedAreaList)

def getRadius():
    while True:
        try:
            return float(input('Please enter a radius: '))
        except:
            print('Something went wrong.')

def computeCircleArea(radius):
    return math.pi * radius**2

main()