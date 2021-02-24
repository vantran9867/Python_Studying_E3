from geometric_objects.point import AbstractPoint


class Point(AbstractPoint):
    x: float
    y: float

    def __init__(self, x: float, y: float):
        super().__init__()
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

