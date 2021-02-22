from geometric_objects.point import abstract_point


class Point(abstract_point):
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "{}, {}, {}".format(self.x, self.y, self.z)

