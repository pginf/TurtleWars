from __future__ import annotations

import math
from math import sqrt


class Vector2D:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def angle_to(self, other: Vector2D):
        vector = self-other
        return math.atan2(vector.y, vector.x)

    def set_location(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other: Vector2D):
        x_dis = other.x - self.x
        y_dis = other.y - self.y
        return sqrt(pow(x_dis, 2) + pow(y_dis, 2))

    def length(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def dot(self):
        return self.x + self.y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            temp: Vector2D = Vector2D(self.x + other.x, self.y + other.y)
        else:
            temp: Vector2D = Vector2D(self.x + other, self.y + other)
        return temp

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            temp: Vector2D = Vector2D(self.x - other.x, self.y - other.y)
        else:
            temp: Vector2D = Vector2D(self.x - other, self.y - other)
        return temp

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            temp: Vector2D = Vector2D(self.x * other.x, self.y * other.y)
        else:
            temp: Vector2D = Vector2D(self.x * other, self.y * other)
        return temp

    def __truediv__(self, other):
        if isinstance(other, Vector2D):
            temp: Vector2D = Vector2D(self.x / other.x, self.y / other.y)
        else:
            temp: Vector2D = Vector2D(self.x / other, self.y / other)
        return temp

    def __neg__(self):
        temp: Vector2D = Vector2D(-self.x, -self.y)
        return temp

    def __pos__(self):
        temp: Vector2D = Vector2D(self.x, self.y)
        return temp

    def __str__(self):
        text = ("(" + str(self.x) + "," + str(self.y) + ")")
        return text


if __name__ == "__main__":
    point = Vector2D(2, 2)
    point2 = Vector2D(20, 21)

    print(point * point2)
    print(point + 1)
    print(point + point2)
