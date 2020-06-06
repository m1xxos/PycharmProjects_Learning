class Sphere:
    pi = 3.1415

    def __init__(self, r):
        self.PI = Sphere.pi
        self.radius = r
        self.volume = 4 / 3 * self.PI * self.radius ** 3
