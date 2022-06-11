from __future__ import annotations

import pygame

from core import Component, GameObject
from core import MainWindow


class VisibleComponent(Component):

    _DEFAULT_COLOR = pygame.Color(0, 255, 0)
    _main_window = MainWindow.get_instance()
    _visible = True
    _width = 50
    _height = 50
    sprite: pygame.sprite.Sprite

    # sprite.image = pygame.Surface([_width, _height])
    # sprite.rect = sprite.image.get_rect()

    def setup(self):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.Surface([self._width, self._height])
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.image.fill(self._DEFAULT_COLOR)

    def set_image(self, name_of_image: str):
        self.sprite.image = pygame.image.load(name_of_image)
        self.sprite.rect = self.sprite.image.get_rect()

    def update(self):
        self.sprite.rect.center = [self.get_parent().get_position().x, self.get_parent().get_position().y]

    def is_visible(self):
        return self._visible

    def set_height(self, h: int):
        pass

    def get_height(self):
        return self._height

    def set_width(self, w: int):
        pass

    def get_width(self):
        return self._width

    def set_visible(self, visible_setting: bool):
        self._visible = visible_setting

