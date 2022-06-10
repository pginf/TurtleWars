from __future__ import annotations

from math import sqrt


class Vector2D:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def set_location(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other: Vector2D):
        return sqrt(pow(other.x - self.x, 2) + pow(other.y - self.y, 2))
