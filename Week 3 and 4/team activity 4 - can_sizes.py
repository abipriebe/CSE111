'''
Team Activity 3 - fitness.py
Abi Priebe
5/12/21
'''
'''
Write a Python program named can_sizes.py that computes and prints the storage efficiency for each of the 
following 12 steel can sizes. Then visually examine the output and answer this question, "Which can size 
has the highest storage efficiency?"
'''
# Initialize
from math import pi as pi
from os import supports_effective_ids
names_list = []
radius_list = []
height_list = []
cost_per_can_list = []
 
with open("team activity 4.txt", "r") as can_sizes:
    for line in can_sizes:
        current_line = line.split(",")
        names_list.append(current_line[0])
        radius_list.append(current_line[1])
        height_list.append(current_line[2])
        cost_per_can_list.append(current_line[3].strip())
 
# Write your functions here.
def main():
    
    for i, value in enumerate(radius_list):
        radius_list[i] = float(radius_list[i])
        height_list[i] = float(height_list[i])
        volume = cylinder_volume(radius_list[i], height_list[i])
        surface_area = cylinder_surface_area(radius_list[i], height_list[i])
        storage_efficiency = storage_efficiency_function(volume, surface_area)
        print(f"{names_list[i]}: {volume:.1f} and {surface_area:.1f} and {storage_efficiency:.1f}")
    
 
# Compute the volume of a cylinder
def cylinder_volume(radius, height):
    volume = pi * float(radius)**2 * float(height)
    return volume
 
# Compute the surface area of a cylinder
def cylinder_surface_area(radius, height):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area
 
# Compute the storage efficiency of a cylinder
def storage_efficiency_function(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

# Run functions here
main()