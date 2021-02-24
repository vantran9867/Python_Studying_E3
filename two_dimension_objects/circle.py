from two_dimension_objects.point import Point
from geometric_objects.shape import AbstractShape
import numpy as np


class Circle(AbstractShape):
    point: Point
    radius: float

    def __init__(self, point1: Point, radius: float):
        super().__init__()
        self.point = point1
        self.radius = radius

    def __str__(self):
        return '(' + 'x' + ' ' + '-' + ' ' + str(self.point.x) + ')' + '**2' + ' ' + '+' + ' ' + '(' + 'y' + ' ' + '-' \
               + ' ' + str(self.point.y) + ')' + '**2' + ' ' + '=' + ' ' + str((self.radius ** 2))

    def get_area(self) -> float:
        return round((self.radius ** 2) * np.pi, 2)
