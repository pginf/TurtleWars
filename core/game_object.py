from __future__ import annotations
from core import GameObjectGroup


class GameObject:
    _position: float
    _scale: float
    _rotation: float
    _group: GameObjectGroup = GameObjectGroup.NONE

    def __init__(self):
        pass

    def set_position(self, position):
        self._position = position

    def get_position(self):
        return self._position

    def set_scale(self, scale):
        self._scale = scale

    def get_scale(self):
        return self._scale

    def set_rotation(self, rotation):
        self._rotation = rotation

    def get_rotation(self):
        return self._rotation
