def area_of_rectangle(length,width):
    area = length * width
    return area

length = float(input("What is the length? "))
width = float(input("what is the width? "))
area = area_of_rectangle(length,width)
print(area)