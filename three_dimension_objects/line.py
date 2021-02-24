from geometric_objects.line import AbstractLine
from three_dimension_objects.point import Point
from three_dimension_objects.vector import Vector


class Line(AbstractLine):
    point: Point
    vector: Vector

    def __init__(self, point: Point, vector: Vector):
        super().__init__()
        self.point = point
        self.vector = vector

    def __str__(self):
        return " x = {} + {}t, y = {} + {}t, z = {} + {}t".format(self.point.x, self.vector.a, self.point.y,
                                                                  self.vector.b, self.point.z, self.vector.c)
