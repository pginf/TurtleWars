from __future__ import annotations

from core.game_object import GameObject
from utils.vector import Vector2D
from . import Component

class MovementComponent(Component):
    velocity: Vector2D = 0
    acceleration: Vector2D = 0
    spin_acceleration: float = 0

    force: Vector2D = Vector2D(0, 0)
    spin: float = 0
    mass: float = 1
    movement_friction: float = 1
    spinning_friction: float = 1

    def setup(self):
        pass

    def update(self):
        position: Vector2D = self.parent.get_position()
        rotation: float = self.parent.get_rotation()

        self.parent.set_position(position + self.velocity)
        self.parent.set_rotation(rotation + self.spin)
        self.velocity += self.acceleration
        self.acceleration = self.force / self.mass

        if self.velocity.x > 0:
            self.velocity.x -= self.movement_friction
        elif self.velocity.x < 0:
            self.velocity.x += self.movement_friction

        if self.velocity.y > 0:
            self.velocity.y -= self.movement_friction
        elif self.velocity.y < 0:
            self.velocity.y += self.movement_friction

        if self.spin > 0:
            self.spin -= self.spinning_friction
        elif self.spin < 0:
            self.spin += self.spinning_friction

    def force_blow(self, force: Vector2D):
        self.velocity = force / self.mass

    def spin_blow(self, spin: float):
        self.spin = spin
