from __future__ import annotations

import random

from core import Game
from core.game_object import GameObject
from utils.vector import Vector2D
from . import Component


class MovementComponent(Component):
    velocity: Vector2D = Vector2D(0, 0)
    acceleration: Vector2D = Vector2D(0, 0)
    spin_acceleration: float = 0

    force: Vector2D = Vector2D(0, 0)
    spin: float = 0
    mass: float = 1
    movement_friction: float = 1
    spinning_friction: float = 1

    def setup(self):
        pass

    def update(self):
        position: Vector2D = self._parent.get_position()
        rotation: float = self._parent.get_rotation()

        time = Game.instance().delta_time

        if time > 1:
            return
        self._parent.set_position(position + self.velocity * time)
        self._parent.set_rotation(rotation + self.spin * time)

        self.velocity += self.acceleration
        self.acceleration = self.force / self.mass

        self.velocity -= self.velocity * self.mass * self.movement_friction * time

        if 1 > self.velocity.x > - 1:
            self.velocity.x = 0

        if 1 > self.velocity.y > - 1:
            self.velocity.y = 0

    def force_blow(self, force: Vector2D):
        self.velocity = force / self.mass

    def spin_blow(self, spin: float):
        self.spin = spin
