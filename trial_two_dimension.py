from two_dimension_objects.point import Point
from two_dimension_objects.triangle import Triangle
from two_dimension_objects.line import Line
from two_dimension_objects.point import Point
from three_dimension_objects.line import Line

p1 = Point(1, -2)
p2 = Point(2, 1)
p3 = Point(-1, 4)
p4 = Point(1, 1)
t1 = Triangle(p1, p2, p3)
print(t1.get_center())
