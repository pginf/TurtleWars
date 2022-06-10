from __future__ import annotations
from core import GameObjectGroup
import core.components_handler
from utils import Vector2D


class GameObject:
    _position: Vector2D
    _scale: Vector2D
    _rotation: Vector2D
    _group: GameObjectGroup = GameObjectGroup.NONE

    _components_handler: core.components_handler.ComponentsHandler

    def __init__(self):
        self._components_handler = core.components_handler.ComponentsHandler(self)
        self._position = Vector2D(0, 0)
        self._scale = Vector2D(1, 1)
        self._rotation = Vector2D(0, 0)

    def setup(self):
        self._components_handler.setup()

    def update(self):
        self._components_handler.update()

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

    def comepre_group(self, other_game_object: GameObject):
        return other_game_object._group == self._group

    def is_of_group(self, group: GameObjectGroup):
        return self._group == group
