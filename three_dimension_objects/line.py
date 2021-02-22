from geometric_objects.line import abstract_line
from three_dimension_objects.point import Point
from three_dimension_objects.vector import Vector


class Line(abstract_line):
    point1: Point
    vector1: Vector

    def __init__(self, point1: Point, vector1: Vector):
        super().__init__()
        self.point1 = point1
        self.vector1 = vector1

    def __str__(self):
        return " x = {} + {}t, y = {} + {}t, z = {} + {}t".format(self.point1.x, self.vector1.a, self.point1.y,
                                                                     self.vector1.b, self.point1.z, self.vector1.c)

