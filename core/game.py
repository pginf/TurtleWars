from __future__ import annotations

import core


class Game:
    main_window: core.MainWindow
    event_handler: core.EventHandler
    _run = True
    _intance: Game = None

    def __init__(self):
        if not Game._intance:
            Game._intance = self
        self.main_window = core.MainWindow()
        self.event_handler = core.EventHandler()


    def stop(self):
        self._run = False

    def loop(self):
        while self._run:
            self.event_handler.hanlde_events()
            self.main_window.update()
            self.main_window.draw()

    @classmethod
    def get_instance(cls):
        return cls._intance
