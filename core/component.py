from __future__ import annotations

from abc import ABC, abstractmethod

from core.game_object import GameObject


class Component(ABC):

    _active: bool = True
    _parent: GameObject

    def __init__(self, parent: GameObject):
        self.parent = parent

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def get_parent(self):
        return self._parent

    def is_active(self):
        return self._active

    def deactivate(self):
        self._active = False

    def activate(self):
        self._active = True


