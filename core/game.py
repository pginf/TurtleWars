from __future__ import annotations

import pygame
import time

import core


class Game:
    _main_window: core.MainWindow
    event_handler: core.EventHandler
    _run = True
    _instance: Game = None

    _delta_time: float
    _time_now: float
    _time_prev: float
    _time_game: float

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
        self._time_now = time.time()
        self._time_prev = time.time()
        self._time_game = 0
        while self._run:
            # Compute delta time
            self._time_now = time.time()
            self._delta_time = self._time_now - self._time_prev
            self._time_prev = self._time_now
            # Compute time
            self._time_game += self._delta_time

            self.event_handler.handle_events()
            self._main_window.update()
            self._main_window.draw()
            self.game_objects.objects_update()

            # Limit framerate
            self._clock.tick(60)

    @classmethod
    def instance(cls) -> Game:
        return cls._instance

    @property
    def main_window(self):
        return self._main_window

    @property
    def delta_time(self):
        return self._delta_time

    @property
    def time(self):
        return self._time_game
