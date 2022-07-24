from __future__ import annotations

from dataclasses import dataclass

import pygame
import core
from core.event import Event


class EventHandler:
    _instance: EventHandler = None

    _on_mouse_press: Event[OnMousePressArgs] = Event()
    _on_keyboard_press: Event[OnKeyboardPressArgs] = Event()

    def __init__(self):
        if not EventHandler._instance:
            EventHandler._instance = self

    @property
    def on_mouse_press(self):
        return self._on_mouse_press

    @property
    def on_keyboard_press(self):
        return self._on_keyboard_press

    @dataclass
    class OnMousePressArgs:
        x: int
        y: int

    @dataclass
    class OnKeyboardPressArgs:
        key_pressed: int

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                core.Game.instance().stop()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self.on_mouse_press.invoke(self.OnMousePressArgs(pos[0], pos[1]))
            elif event.type == pygame.KEYDOWN:
                self.on_keyboard_press.invoke(self.OnKeyboardPressArgs(event.key))

    @classmethod
    def get_instance(cls):
        return cls._instance
