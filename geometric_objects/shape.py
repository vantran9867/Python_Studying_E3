from geometric_objects.point import AbstractPoint


class AbstractShape:
    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def shape_verification():
        pass

    def get_area(self) -> float:
        pass

    def get_center(self) -> AbstractPoint:
        pass
