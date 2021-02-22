from three_dimension_objects.point import Point


class Vector:
    a: float
    b: float
    c: float

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "({}, {}, {})".format(self.a, self.b, self.c)

    @staticmethod
    def get_vector_from_two_point(point1: Point, point2: Point):
        n1 = point2.x - point1.x
        n2 = point2.y - point1.y
        n3 = point2.z - point1.z
        return Vector(n1, n2, n3)

