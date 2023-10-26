import math

def area_of_circle(radius):
    area = math.pi * radius * radius
    return area

radius = float(input("Enter radius: "))
area = area_of_circle(radius)
print(area)