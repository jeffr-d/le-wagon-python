import math

radius = 5
perimeter = round(2 * math.pi * radius, 1)
area = round(math.pi * radius ** 2, 1)

circle_data = f"The radius is set to {radius}\nPerimeter of the circle is {perimeter}\nArea of the disk is {area}"

print(circle_data)

from math import pi
# defining the function
def circle_math(radius):
    perimeter = 2 * pi * radius
    area = pi * radius * radius
    return [ perimeter, area ] # perimeter and area are called **local variables* 

# 2. calling the function
# for radius 5
values = circle_math(5)
print(f"Radius=5 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")

# for radius 6 - reusing "values"
values = circle_math(6)
print(f"Radius=6 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")


