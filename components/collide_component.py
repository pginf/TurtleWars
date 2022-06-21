from __future__ import annotations

import pygame.rect

from core import Component
from components import VisibleComponent
from core import Game
from core import GameObjectGroup


class BoxCollider(Component):
    _height: int
    _width: int
    _rect: pygame.rect.Rect
    _call_counter: int

    def setup(self):
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
        self._call_counter += 1
        self._rect.x = self.get_parent().get_position().x
        self._rect.y = self.get_parent().get_position().y

        if self._call_counter % 5 == 0:
            self.check_collisions()
            self._call_counter = 0

    def check_collisions(self):
        game = Game.instance()

        for group in GameObjectGroup:
            for index in range(game.game_objects.get_group_length(group)):
                obj = game.game_objects.get_object(group, index)
                box_collider: BoxCollider = obj.get_component(BoxCollider)
                box_collider.get_rect()
                if box_collider._rect.colliderect(self._rect) and box_collider != self:
                    print(self.get_parent().get_name() + " collides with " + obj.get_name())
                    obj.set_exist(False)

    def get_rect(self):
        return self._rect
