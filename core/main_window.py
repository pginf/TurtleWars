from __future__ import annotations
import pygame




class MainWindow:

    WIDTH, HEIGHT = 900, 600
    surface: pygame.Surface
    _intance: MainWindow = None

    def __init__(self):
        if not MainWindow._intance:
            MainWindow._intance = self
        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def draw(self):
        self.surface.fill((140, 100, 200))

    def update(self):
        pygame.display.update()

    @classmethod
    def get_instance(cls):
        return cls._intance