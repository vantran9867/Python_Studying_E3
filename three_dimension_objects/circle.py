from geometric_objects.shape import AbstractShape
from three_dimension_objects.point import Point


class Circle(AbstractShape):
    center: Point
    radius: float

    def __init__(self, center: Point, radius: float):
        super().__init__()
        self.center = center
        self.radius = radius

    def __str__(self):
        return "(x - {})**2 + (y - {})**2 + (z - {})**2 = {}**2".format(self.center.x, self.center.y, self.center.z,
                                                                        self.radius)

    def get_area(self) -> float:
        return round((self.radius * 3.14), 2)
