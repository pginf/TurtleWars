from __future__ import annotations

from typing import List

from listeners import DefaultListener


class ListenersHandler:

    _listeners: List[DefaultListener]

    def __init__(self):
        self._listeners = []

    def on_event(self, *args, **kwargs):
        for listener in self._listeners:
            listener.on_event(*args, **kwargs)

