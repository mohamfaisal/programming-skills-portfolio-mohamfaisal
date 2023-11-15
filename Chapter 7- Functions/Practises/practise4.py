# Write a Python program that defines a function to calculate the area of a circle, and then
# calls that function with a given radius.

import math

def area_of_circle(radius):
    area = math.pi * radius**2
    return area
radius = 5
area = area_of_circle(radius)

print(" Area of the circle ", radius, "is", area)

radius = 5
area = area_of_circle(radius)
print(" Area of the circle ", radius, "is", area)