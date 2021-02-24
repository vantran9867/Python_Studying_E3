from geometric_objects.line import AbstractLine


class Line(AbstractLine):
    a: float
    b: float
    c: float

    def __init__(self, a: float, b: float, c: float) -> None:
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return str(self.a) + 'x' + ' ' + '+' + ' ' + str(self.b) + 'y' + ' ' + str(self.c) + ' ' + '=' + ' ' + '0'