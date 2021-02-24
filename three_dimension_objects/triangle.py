import math
from geometric_objects.shape import AbstractShape
from three_dimension_objects.point import Point
from three_dimension_objects.vector import Vector


class Triangle(AbstractShape):
    point1: Point
    point2: Point
    point3: Point

    def __init__(self, point1: Point, point2: Point, point3: Point):
        super().__init__()
        if Triangle.triangle_verification(point1, point2, point3):
            self.point1 = point1
            self.point2 = point2
            self.point3 = point3
        else:
            raise RuntimeError('Not Triangle')

    @staticmethod
    def triangle_verification(point1: Point, point2: Point, point3: Point) -> bool:
        v1 = Vector.get_vector_from_two_point(point1, point2)
        v2 = Vector.get_vector_from_two_point(point2, point3)
        if v2.a != 0 and v2.b != 0 and v2.c != 0 and v1.a/v2.a == v1.b/v2.b == v1.c/v2.c:
            return False
        else:
            return True

    def get_center(self) -> Point:
        xG = (self.point1.x + self.point2.x + self.point3.x)/3
        yG = (self.point1.y + self.point2.y + self.point3.y)/3
        zG = (self.point1.z + self.point2.z + self.point3.z)/3
        return Point(xG, yG, zG)

    def get_area(self) -> float:
        v1 = Vector.get_vector_from_two_point(self.point1, self.point2)
        v2 = Vector.get_vector_from_two_point(self.point2, self.point3)
        d1 = v1.b*v2.c - v2.b*v1.c
        d2 = v2.a*v1.c - v1.a*v1.c
        d3 = v1.a*v2.b - v2.a*v2.b
        return round(1/2 * math.sqrt(d1**2 + d2**2 + d3**2), 2)



