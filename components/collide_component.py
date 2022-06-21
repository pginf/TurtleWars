from __future__ import annotations

import pygame.rect

from core import Component
from components import VisibleComponent
from core import Game
from core import GameObjectGroup
from core import GameObject
from typing import List


class BoxCollider(Component):
    _height: int
    _width: int
    _rect: pygame.rect.Rect
    _call_counter: int
    _collision_list: List[GameObject]

    def setup(self):
        self._collision_list = []
        self._call_counter = 0
        parent = self.get_parent()
        vs_component: VisibleComponent = parent.get_component(VisibleComponent)

        if vs_component:
            self._height = vs_component.get_height() * parent.get_scale().y
            self._width = vs_component.get_width() * parent.get_scale().x
        else:
            self._height = 0
            self._width = 0
        self._rect = pygame.Rect((parent.get_position().x, parent.get_position().y), (self._width, self._height))

    def update(self):
        self._rect.centerx = self.get_parent().get_position().x
        self._rect.centery = self.get_parent().get_position().y
        self.check_collisions()

    def check_collisions(self):
        game = Game.instance()
        self._collision_list.clear()
        for group in GameObjectGroup:
            for index in range(game.game_objects.get_group_length(group)):
                obj = game.game_objects.get_object(group, index)
                box_collider: BoxCollider = obj.get_component(BoxCollider)
                box_collider.get_rect()
                if box_collider._rect.colliderect(self._rect) and box_collider != self:
                    self._collision_list.append(obj)

    def get_rect(self):
        return self._rect

    def get_collisions(self):
        return self._collision_list
