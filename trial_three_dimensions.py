from three_dimension_objects.point import Point
from three_dimension_objects.line import Line
from three_dimension_objects.vector import Vector
from three_dimension_objects.triangle import Triangle

point1 = Point(2, 1, 0)
vector1 = Vector(1, -4, -2)
l1 = Line(point1, vector1)
print(l1)

A = Point(1, 2, 1)
B = Point(0, -1, 0)
C = Point(3, -3, 3)
print(Triangle.triangle_verification(A, B, C))
tri1 = Triangle(A, B, C)
print(tri1.get_area())
