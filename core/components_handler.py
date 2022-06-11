from __future__ import annotations

import core
import core.game_object

from typing import Type, Optional, List


class ComponentsHandler:
    _parent: core.game_object.GameObject

    _components: List[core.Component]

    def __init__(self, parent: core.game_object.GameObject):
        self._components = []
        self._parent = parent

    def add_component(self, component: Type[core.Component]):
        new_component: core.Component = component(self._parent)
        self._components.append(new_component)

    def get_component(self, component: Type[core.Component]) -> Optional[core.Component]:
        for c in self._components:
            if type(c) == component:
                return c

        return None

    def setup(self):
        for c in self._components:
            c.setup()

    def update(self):
        for c in self._components:
            c.update()