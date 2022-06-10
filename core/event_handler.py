from __future__ import annotations

import pygame
import core



class EventHandler:
    _intance: EventHandler = None

    def __init__(self):
        if not EventHandler._intance:
            EventHandler._intance = self

    def hanlde_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                core.Game.get_instance().stop()

    @classmethod
    def get_instance(cls):
        return cls._intance
