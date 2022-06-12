from __future__ import annotations

import pygame

from core import Component, GameObject
from core import MainWindow
from utils import Vector2D


class VisibleComponent(Component):

    _DEFAULT_COLOR = pygame.Color(0, 255, 0)
    _main_window = MainWindow.get_instance()
    _visible = True
    _width = 50
    _height = 50
    _sprite: pygame.sprite.Sprite
    _image: pygame.image
    _scale: Vector2D
    _rotation: float

    def setup(self):
        self._scale = self.get_parent().get_scale()
        self._rotation = self.get_parent().get_rotation()
        self._image = pygame.Surface([self._width, self._height]).convert()
        self._image.set_colorkey((0, 0, 0))
        self._sprite = pygame.sprite.Sprite()
        self._sprite.image = self._image
        self._sprite.rect = self.sprite.image.get_rect()
        self._sprite.image.fill(self._DEFAULT_COLOR)

    def set_image(self, name_of_image: str):
        self._image = pygame.image.load(name_of_image).convert()
        self._height = self._image.get_height()
        self._width = self._image.get_width()
        self._sprite.image = self._image
        self._sprite.rect = self.sprite.image.get_rect()

    def update(self):
        if self._rotation != self.get_parent().get_rotation():
            self.set_rotation(self.get_parent().get_rotation())
        if self._scale != self.get_parent().get_scale():
            self.set_scale(self.get_parent().get_scale())
        self._sprite.rect.center = [self.get_parent().get_position().x, self.get_parent().get_position().y]

    def set_size(self, v: Vector2D):
        self._sprite.image = pygame.transform.scale(self._sprite.image, (v.x, v.y))
        self._height = v.y
        self._width = v.x
        self._sprite.rect = self.sprite.image.get_rect()

    def set_scale(self, scale: Vector2D):
        self._scale = scale
        self._image = pygame.transform.scale(self._image, (self._width * scale.x, self._height * scale.y))
        self._sprite.image = self._image
        self._sprite.rect = self.sprite.image.get_rect()

    def set_rotation(self, angle: float):
        self._rotation = angle
        self._sprite.image = pygame.transform.rotate(self._image, angle)
        self._sprite.rect = self._sprite.image.get_rect()

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    @property
    def sprite(self):
        return self._sprite


