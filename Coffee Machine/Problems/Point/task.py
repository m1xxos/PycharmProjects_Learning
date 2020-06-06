class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return (((self.x - point.x) ** 2) + ((self.y - point.y) ** 2)) ** 0.5
