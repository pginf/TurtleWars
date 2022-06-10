from __future__ import annotations
from core import GameObjectGroup
from utils import Vector2D


class GameObject:
    _position: Vector2D
    _scale: Vector2D
    _rotation: float
    _group: GameObjectGroup = GameObjectGroup.NONE

    def __init__(self):
        self._position = Vector2D(0, 0)
        self._scale = Vector2D(1, 1)
        self._rotation = 0

    def set_position(self, position: Vector2D):
        self._position = position

    def get_position(self):
        return self._position

    def set_scale(self, scale: Vector2D):
        self._scale = scale

    def get_scale(self):
        return self._scale

    def set_rotation(self, rotation: float):
        self._rotation = rotation

    def get_rotation(self):
        return self._rotation

    def comepre_group(self, other_game_object: GameObject):
        return other_game_object._group == self._group

    def is_of_group(self, group: GameObjectGroup):
        return self._group == group
