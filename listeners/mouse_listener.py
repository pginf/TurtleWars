from __future__ import annotations
from abc import ABC, abstractmethod

class MouseListener(ABC):
    def on_event(self, mouse_x: int, mouse_y: int):
        pass