from __future__ import annotations
from core import GameObjectGroup
from utils import Vector2D


class GameObject:
    _position: Vector2D
    _scale: Vector2D
    _rotation: Vector2D
    _group: GameObjectGroup = GameObjectGroup.NONE
    _name: str = "New game object"
    _exist: bool

    def __init__(self):
        self._position = Vector2D(0, 0)
        self._scale = Vector2D(1, 1)
        self._rotation = Vector2D(0, 0)

    def set_position(self, position: Vector2D):
        self._position = position

    def get_position(self):
        return self._position

    def set_scale(self, scale: Vector2D):
        self._scale = scale

    def get_scale(self):
        return self._scale

    def set_rotation(self, rotation: Vector2D):
        self._rotation = rotation

    def get_rotation(self):
        return self._rotation

    def set_group(self, group: GameObjectGroup):
        self._group = group

    def get_group(self):
        return self._group

    def comepre_group(self, other_game_object: GameObject):
        return other_game_object._group == self._group

    def is_of_group(self, group: GameObjectGroup):
        return self._group == group

    def set_name(self, name: str):
        self._name = name

    def get_name(self):
        return self._name

    def exist(self):
        return self._exist

    def set_exist(self, existence: bool):
        self._exist = existence
