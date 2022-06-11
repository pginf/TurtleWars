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
    _sprite: pygame.sprite.Sprite

    def setup(self):
        self._sprite = pygame.sprite.Sprite()
        self._sprite.image = pygame.Surface([self._width, self._height]).convert()
        self._sprite.rect = self.sprite.image.get_rect()
        self._sprite.image.fill(self._DEFAULT_COLOR)

    def set_image(self, name_of_image: str):
        self._sprite.image = pygame.image.load(name_of_image).convert()
        self._sprite.rect = self.sprite.image.get_rect()

    def update(self):
        self._sprite.rect.center = [self.get_parent().get_position().x, self.get_parent().get_position().y]

    def is_visible(self):
        return self._visible

    def set_size(self, w: int, h: int):
        self._sprite.image = pygame.transform.scale(self._sprite.image, (w, h))
        self._sprite.rect = self.sprite.image.get_rect()

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def set_visible(self, visible_setting: bool):
        self._visible = visible_setting

    @property
    def sprite(self):
        return self._sprite


