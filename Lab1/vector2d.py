# Vector2D class for operating with vector objects
import math
class Vector2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001

    def __add__(self, other):
        return Vector2D((self.x + other.x), (self.y + other.y))

    def __sub__(self, other):
        return Vector2D((self.x - other.x), (self.y - other.y))

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector2D(scalar * self.x, scalar * self.y)

    def __div__(self, scalar):
        if scalar != 0:
            return Vector2D(self.x/scalar, self.y/scalar)
        else:
            return None

    def __truediv__(self, scalar):
        return self.__div__(scalar)

    def __eq__(self, other):
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                    return True
        return False

    def __ge__(self, other):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2)) >= math.sqrt(pow(other.x, 2) + pow(other.y, 2))

    def __lt__(self, other):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2)) < math.sqrt(pow(other.x, 2) + pow(other.y, 2))

    def __hash__(self):
        return id(self)

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def magnitudeSquared(self):
        return math.pow(self.x, 2) + math.pow(self.y, 2)

    def magnitude(self):
        return math.sqrt(self.magnitudeSquared())

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return Vector2D(self.x/mag, self.y/mag)
        return None

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def copy(self):
        return Vector2D(self.x, self.y)


if __name__ == '__main__':
    v1 = Vector2D(2, 3)
    v2 = Vector2D(0.5, -1.5)
    print(f'The sum of {v1} and {v2} is {v1+v2}')
    print(f'The dot product of {v1} and {v2} is {v1.dot(v2)}')
