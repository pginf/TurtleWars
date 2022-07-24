from __future__ import annotations

from typing import Type, Optional

from core import GameObjectGroup
import core.components_handler
from core.event import Event
from utils import Vector2D


class GameObject:
    _position: Vector2D
    _scale: Vector2D
    _rotation: float
    _group: GameObjectGroup = GameObjectGroup.NONE
    _name: str = "New game object"
    _exist: bool
    _on_scale_change: Event[Vector2D]
    _on_rotation_change: Event[float]
    _on_position_change: Event[Vector2D]

    _components_handler: core.components_handler.ComponentsHandler

    def __init__(self):
        self._components_handler = core.components_handler.ComponentsHandler(self)
        self._position = Vector2D(0, 0)
        self._scale = Vector2D(1, 1)
        self._rotation = 0
        self._exist = True
        self._on_scale_change = Event()
        self._on_rotation_change = Event()
        self._on_position_change = Event()

    def add_component(self, component: Type[core.Component]):
        self._components_handler.add_component(component)

    def get_component(self, component: Type[core.Component]) -> Optional[core.Component]:
        return self._components_handler.get_component(component)

    def setup(self):
        self._components_handler.setup()

    def update(self):
        self._components_handler.update()

    def set_position(self, position: Vector2D):
        self._position = position
        self._on_position_change.invoke(position)

    def get_position(self):
        return self._position

    def set_scale(self, scale: Vector2D):
        self._scale = scale
        self._on_scale_change.invoke(scale)

    def get_scale(self):
        return self._scale

    def set_rotation(self, rotation: float):
        self._rotation = rotation
        self._on_rotation_change.invoke(rotation)

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

    def destroy(self):
        self.set_exist(False)

    @property
    def on_scale_change(self):
        return self._on_scale_change

    @property
    def on_rotation_change(self):
        return self._on_rotation_change

    @property
    def on_position_change(self):
        return self._on_position_change
