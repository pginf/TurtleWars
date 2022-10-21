from __future__ import annotations

import pygame

from core import GameObject

import components
from core import GameObjectGroup
from typing import List, Tuple


class Wall(GameObject):

    def __init__(self, w: int, h: int, x: int, y: int):
        super(Wall, self).__init__()
        self.add_component(components.VisibleComponent)
        self.add_component(components.Collider)
        self.set_group(GameObjectGroup.ENVIRONMENT)
        self.once = True
        self.set_position(Vector2D(x, y))

        self.setup()

        # setting up components
        col_c: Collider = self.get_component(components.Collider)
        col_c.set_size(w)
        col_c.on_collision_enter.add(self._on_collide)

        vis_c: VisibleComponent = self.get_component(components.VisibleComponent)
        vis_c.set_size(Vector2D(w, h))

    def update(self):
        self._components_handler.update()

    def _on_collide(self, collisions_list: List[Tuple[GameObject, float]]):
        for i in range(len(collisions_list)):
            obj = collisions_list[i][0]
            if collisions_list[i][1] is not None:
                overlap_vector = obj.get_position() - self.get_position()
                overlap_vector /= overlap_vector.length()
                overlap_vector *= collisions_list[i][1]
                obj.set_position(obj.get_position() + (overlap_vector * Game.instance().delta_time))


if __name__ == "__main__":
    from core import Game
    from utils import Vector2D
    from components.movement_component import MovementComponent
    from components import Collider
    from components import VisibleComponent
    from core import MainWindow

    game = Game()

    window = MainWindow.get_instance()

    a = GameObject()
    a.set_name("o1")
    a.set_position(Vector2D(500, 100))
    a.add_component(VisibleComponent)
    a.add_component(MovementComponent)
    a.add_component(Collider)
    a.setup()
    a.set_rotation(45)

    game.game_objects.add_object_to_group(a)

    c = GameObject()
    c.set_name("o3")
    c.set_position(Vector2D(200, 330))
    c.add_component(VisibleComponent)
    c.add_component(MovementComponent)
    c.add_component(Collider)
    c.set_rotation(30)
    c.setup()

    game.game_objects.add_object_to_group(c)

    b = Wall(100, 100, 400, 300)
    b.set_name("o2")
    b.set_position(Vector2D(400, 300))

    game.game_objects.add_object_to_group(b)

    vca: VisibleComponent = a.get_component(VisibleComponent)
    a_surface = pygame.Surface([vca.get_width(), vca.get_height()])
    a_surface.fill('RED')
    vca.set_image_surface(a_surface)

    mca: MovementComponent = a.get_component(MovementComponent)
    mca.force_blow(Vector2D(-100, 100))
    mca.movement_friction = 0
    mca.spin_blow(30)

    mcc: MovementComponent = c.get_component(MovementComponent)
    mcc.force_blow(Vector2D(200, 0))
    mcc.movement_friction = 0
    ccc: Collider = c.get_component(Collider)
    ccc.set_size(50)
    ccc.set_number_of_points(4)

    game.loop()
