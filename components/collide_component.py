from __future__ import annotations

import math
import numbers

import pygame.rect

from core import MainWindow
from core import Component
from core import Game
from core import GameObjectGroup
from core import GameObject
from typing import List, Tuple
from utils import Vector2D
from math import sin, cos, radians
from core.event import Event


class Collider(Component):
    _num_of_points = 4  # for testing
    _size: int = 50
    _points: List[Vector2D]
    _center: Vector2D
    _rotation: float
    _base_angle: float
    _auto_positioning = True
    _collider_visible = True
    _collision_list: List[Tuple[GameObject, float]]
    _on_collision_enter: Event[List[Tuple[GameObject, float]]]

    def setup(self):
        self._collision_list = []
        self._points = []
        self._base_angle = radians(360 / (self._num_of_points * 2))

        # Adding publishers
        self._on_collision_enter = Event()

        # Adding subscribers
        self.get_parent().on_position_change.add(self._set_position)
        self.get_parent().on_rotation_change.add(self._set_rotation)

        # Setting up in space
        self._center = self.get_parent().get_position()
        self.setup_points()
        self._rotation = 0
        self._set_rotation(self.get_parent().get_rotation())

    def setup_points(self):
        if self._points:
            self._points.clear()
        for i in range(self._num_of_points):
            rot = radians((i * 360/self._num_of_points) + self.get_parent().get_rotation())
            point_x = self._size/2 * math.sqrt(2) * sin(self._base_angle + rot) + self._center.x  # na potrzeby kwadratu
            point_y = self._size/2 * math.sqrt(2) * cos(self._base_angle + rot) + self._center.y  # na potrzeby kwadratu
            point = Vector2D(point_x, point_y)
            self._points.append(point)

    def update(self):
        self.check_collisions()
        if self._collider_visible:
            self._draw_collider()

    def _set_position(self, position: Vector2D):
        vector = position - self._center
        for i in range(0, self._num_of_points):
            self._points[i] = self._points[i] + vector
        self._center = self.get_center() + vector

    def _set_rotation(self, angle: float):
        self._rotation = angle
        for i in range(self._num_of_points):
            point = self._points[i]
            rot = radians((i * 360/self._num_of_points) + angle)
            length = point.distance(self._center)
            point.x = length * sin(self._base_angle + rot) + self._center.x
            point.y = length * cos(self._base_angle + rot) + self._center.y

    def _check_collision(self, col_a: Collider, col_b: Collider):
        if col_a != col_b:
            collider_a = col_a
            collider_b = col_b
            for j in range(2):
                if j == 1:
                    collider_a, collider_b = collider_b, collider_a
                for i in range(collider_a.num_of_points):
                    v1 = collider_a.get_points()[i]
                    v2 = collider_a.get_points()[(i+1) % collider_a.num_of_points]

                    edge = v2 - v1
                    axis = Vector2D(-edge.y, edge.x)
                    min_a, max_a = self._project_vertices(collider_a.get_points(), axis)
                    min_b, max_b = self._project_vertices(collider_b.get_points(), axis)

                    if min_a >= max_b or min_b >= max_a:
                        return False
            return True
        return False

    def _check_collision_static(self, col_a: Collider, col_b: Collider):
        if col_a != col_b:
            overlap = math.inf
            collider_a = col_a
            collider_b = col_b
            for j in range(2):
                if j == 1:
                    collider_a, collider_b = collider_b, collider_a
                for i in range(collider_a._num_of_points):
                    v1 = collider_a.get_points()[i]
                    v2 = collider_a.get_points()[(i+1) % collider_a._num_of_points]

                    edge = v2 - v1
                    axis = Vector2D(-edge.y, edge.x)
                    min_a, max_a = self._project_vertices(collider_a.get_points(), axis)
                    min_b, max_b = self._project_vertices(collider_b.get_points(), axis)
                    overlap = min((min(max_a, max_b) - max(min_a, min_b)), overlap)

                    if min_a >= max_b or min_b >= max_a:
                        return None
            return overlap
        return None

    def _draw_collider(self):
        for i in range(self._num_of_points):
            point_s = self._points[i]
            point_e = self._points[(i + 1) % self._num_of_points]
            surface = MainWindow.get_instance().get_surface()
            pygame.draw.line(surface, 'RED', [point_s.x, point_s.y], [point_e.x, point_e.y], 3)

    def _project_vertices(self, vertices: List[Vector2D], axis: Vector2D):
        min_proj = math.inf
        max_proj = -math.inf

        for ver in vertices:
            proj = (ver*axis).dot()

            min_proj = min(proj, min_proj)
            max_proj = max(proj, max_proj)

        return min_proj, max_proj

    def check_collisions(self):
        game = Game.instance()
        self._collision_list.clear()
        for group in GameObjectGroup:
            for index in range(game.game_objects.get_group_length(group)):
                other_collider = game.game_objects.get_object(group, index).get_component(Collider)
                self_collider = self
                collision_result = self._check_collision_static(self_collider, other_collider)
                if collision_result:
                    if isinstance(collision_result, numbers.Number):
                        self._collision_list.append((other_collider.get_parent(), collision_result))
                    else:
                        self._collision_list.append((other_collider.get_parent(), 0))
        if len(self._collision_list) > 0:
            self._on_collision_enter.invoke(self._collision_list)

    def get_collisions(self):
        return self._collision_list

    def enable_auto_positioning(self, setting: bool):
        self._auto_positioning = setting

    def show_collider(self, setting: bool):
        self._collider_visible = setting

    def get_size(self):
        return self._size

    def set_size(self, size: int):
        self._size = size
        self.setup_points()

    def get_center(self):
        return self._center

    def set_number_of_points(self, num_of_points: int):
        self._num_of_points = num_of_points
        self._base_angle = radians(360 / (self._num_of_points * 2))
        self.setup_points()

    def get_number_of_points(self):
        return self._num_of_points

    def get_points(self):
        return self._points


    @property
    def on_collision_enter(self):
        return self._on_collision_enter

