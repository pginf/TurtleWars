from __future__ import annotations

import random

from core import Game
from core.game_object import GameObject
from utils.vector import Vector2D
from . import Component


class MovementComponent(Component):
    __ACCELERATION_MULTIPLIER = 10
    __velocity: Vector2D = Vector2D(0, 0)
    __acceleration: Vector2D = Vector2D(0, 0)
    __max_velocity: float = None
    __spin_acceleration: float = 0

    __force: Vector2D = Vector2D(0, 0)
    __spin: float = 0
    __mass: float = 1
    __movement_friction: float = 1
    __spinning_friction: float = 1

    def setup(self):
        pass

    def update(self):
        position: Vector2D = self._parent.get_position()
        rotation: float = self._parent.get_rotation()

        delta_time = Game.instance().delta_time

        if delta_time > 1:
            return

        self._parent.set_position(
            position + self.__velocity * delta_time + self.__acceleration * delta_time * delta_time / 2)
        self._parent.set_rotation(rotation + self.__spin * delta_time)

        self.__acceleration = ((
                                self.__force - self.__velocity * self.__mass * self.__movement_friction) *
                               self.__ACCELERATION_MULTIPLIER) / self.__mass

        self.__velocity += self.__acceleration * delta_time
        self.__spin -= self.__spin * self.__spinning_friction * delta_time

        if self.__max_velocity and self.__velocity.x > self.__max_velocity:
            self.__velocity.x = self.__max_velocity
        if self.__max_velocity and self.__velocity.y > self.__max_velocity:
            self.__velocity.y = self.__max_velocity

        if 1 > self.__velocity.x > - 1:
            self.__velocity.x = 0

        if 1 > self.__velocity.y > - 1:
            self.__velocity.y = 0

        if 1 > self.__spin > - 1:
            self.__spin = 0

    def force_blow(self, force_blow: Vector2D):
        self.__velocity += force_blow / self.__mass

    def spin_blow(self, spin: float):
        self.__spin = spin

    def get_velocity(self):
        return self.__velocity

    def get_spin(self):
        return self.__spin

    def get_movement_friction(self):
        return self.__movement_friction

    def get_spinning_friction(self):
        return self.__spinning_friction

    def get_mass(self):
        return self.__mass

    def get_max_velocity(self):
        return self.__max_velocity

    def get_force(self):
        return self.__force

    def set_velocity(self, new_velocity):
        self.__velocity = new_velocity

    def set_spin(self, new_spin):
        self.__spin = new_spin

    def set_movement_friction(self, friction):
        self.__movement_friction = friction

    def set_spinning_friction(self, friction):
        self.__spinning_friction = friction

    def set_mass(self, mass):
        self.__mass = mass

    def set_force(self, const_force):
        self.__force = const_force

    def set_max_velocity(self, max_velocity):
        self.__max_velocity = max_velocity
