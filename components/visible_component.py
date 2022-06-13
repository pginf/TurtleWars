from __future__ import annotations

import pygame

from core import Component
from core import MainWindow
from utils import Vector2D


class VisibleComponent(Component):

    _CENTRE_COLOR = pygame.Color(255, 0, 0)
    _CENTRE_SIZE = 1
    _DEFAULT_COLOR = pygame.Color(0, 255, 0)
    _main_window = MainWindow.get_instance()
    _width = 50
    _height = 50
    _sprite: pygame.sprite.Sprite
    _image: pygame.image
    _scale: Vector2D
    _rotation: float
    _auto_update = True
    _auto_pos = True
    _centre_show = False

    def setup(self):
        self._scale = self.get_parent().get_scale()
        self._rotation = self.get_parent().get_rotation()
        self._image = pygame.Surface([self._width, self._height]).convert()
        self._image.set_colorkey((0, 0, 0))
        self._sprite = pygame.sprite.Sprite()
        self._sprite.image = self._image
        self._sprite.rect = self.sprite.image.get_rect()
        self._sprite.image.fill(self._DEFAULT_COLOR)

    def set_image_name(self, name_of_image: str):
        self._image = pygame.image.load(name_of_image).convert()
        self.__image_setup()

    def set_image_surface(self, image: pygame.Surface):
        self._image = image.convert()
        self.__image_setup()

    def __image_setup(self):
        self._image.set_colorkey((0, 0, 0))
        self._height = self._image.get_height()
        self._width = self._image.get_width()
        self._sprite.image = self._image
        self._sprite.rect = self.sprite.image.get_rect()

    def update(self):
        if self._auto_update:
            if self._rotation != self.get_parent().get_rotation():
                self.set_rotation(self.get_parent().get_rotation())
            if self._scale != self.get_parent().get_scale():
                self.set_scale(self.get_parent().get_scale())
        if self._auto_pos:
            self._sprite.rect.center = [self.get_parent().get_position().x, self.get_parent().get_position().y]
        if self._centre_show:
            pygame.draw.circle(self._sprite.image, self._CENTRE_COLOR, self._sprite.rect.center, self._CENTRE_SIZE)

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

    def set_auto_update(self, value: bool):
        self._auto_update = value

    def set_auto_positioning(self, value: bool):
        self._auto_pos = value

    def set_centre_visible(self, value: bool):
        self._centre_show = value

    @property
    def sprite(self):
        return self._sprite
