from __future__ import annotations
from abc import ABC, abstractmethod

class DefaultListener(ABC):
    @abstractmethod
    def on_event(self, *args, **kwargs):
        pass