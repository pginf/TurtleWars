from __future__ import annotations

import pygame
import time

import core


class Game:
    _main_window: core.MainWindow
    event_handler: core.EventHandler
    _run = True
    _instance: Game = None

    _delta_time: float = 0
    _time_now: float = 0
    _time_prev: float = 0

    _FPS_LIMIT = 60
    _clock = pygame.time.Clock()

    game_objects: core.GameObjects

    def __init__(self):
        if not Game._instance:
            Game._instance = self
        self._main_window = core.MainWindow()
        self.event_handler = core.EventHandler()
        self.game_objects = core.GameObjects()

    def stop(self):
        self._run = False

    def loop(self):
        while self._run:
            # Limit framerate
            self._clock.tick(60)
            # Compute delta time
            self._time_now = time.time()
            self._delta_time = self._time_now - self._time_prev
            self._time_prev = self._time_now
            print(self._delta_time)

            self.event_handler.hanlde_events()
            self._main_window.update()
            self._main_window.draw()
            self.game_objects.objects_update()

    @classmethod
    def instance(cls) -> Game:
        return cls._instance

    @property
    def main_window(self):
        return self._main_window

    @property
    def delta_time(self):
        return self._delta_time
