from __future__ import annotations

import pygame

from core import GameObject

import components
from utils import Vector2D
from core import GameObjectGroup


class Wall(GameObject):

    def __init__(self):
        super(Wall, self).__init__()
        self.add_component(components.VisibleComponent)
        self.add_component(components.BoxCollider)
        self.set_group(GameObjectGroup.ENVIRONMENT)

    def update(self):
        self._components_handler.update()
        self._on_collide()

    # to change when listeners ready
    def _collide_with(self):
        collider: components.BoxCollider = self.get_component(components.BoxCollider)
        return collider.get_collisions()

    def _on_collide(self):
        collisions_list = self._collide_with()
        for obj in collisions_list:
            mv_c: components.MovementComponent = obj.get_component(components.MovementComponent)
            if mv_c:
                horizontal_velocity = 0
                vertical_velocity = 0
                s_bc: components.BoxCollider = self.get_component(components.BoxCollider)
                o_bc: components.BoxCollider = obj.get_component(components.BoxCollider)
                s_rect = s_bc.get_rect()
                o_rect = o_bc.get_rect()

                # if o_rect.top > s_rect.bottom ^ o_rect.bottom < s_rect.top:
                #     horizontal_velocity = -mv_c.velocity.y
                # if o_rect.left > s_rect.right ^ o_rect.right < s_rect.left:
                #     vertical_velocity = -mv_c.velocity.x
                #
                # mv_c.velocity += Vector2D(vertical_velocity, horizontal_velocity)

                if o_rect.top < s_rect.bottom < o_rect.bottom:
                    o_rect.top = s_rect.bottom
                elif o_rect.bottom > s_rect.top > o_rect.top:
                    o_rect.bottom = s_rect.top
                elif o_rect.left < s_rect.right < o_rect.right:
                    o_rect.left = s_rect.right
                elif o_rect.right > s_rect.left > o_rect.left:
                    o_rect.right = s_rect.left

                obj.set_position(Vector2D(o_rect.centerx, o_rect.centery))


if __name__ == "__main__":
    from core import Game
    from utils import Vector2D
    from components.movement_component import MovementComponent
    from components import BoxCollider
    from components import VisibleComponent
    from core import MainWindow

    game = Game()

    window = MainWindow.get_instance()

    a = GameObject()
    a.set_name("o1")
    a.set_position(Vector2D(300, 250))
    a.add_component(VisibleComponent)
    a.add_component(MovementComponent)
    a.add_component(BoxCollider)
    a.setup()

    game.game_objects.add_object_to_group(a)

    b = Wall()
    b.set_name("o2")
    b.set_position(Vector2D(400, 320))
    b.add_component(MovementComponent)
    b.setup()

    game.game_objects.add_object_to_group(b)

    vca: VisibleComponent = a.get_component(VisibleComponent)
    a_surface = pygame.Surface([vca.get_width(), vca.get_height()])
    a_surface.fill('RED')
    vca.set_image_surface(a_surface)

    mca: MovementComponent = a.get_component(MovementComponent)
    mca.force_blow(Vector2D(100, 100))
    mca.movement_friction = 0

    mcb: MovementComponent = b.get_component(MovementComponent)

    game.loop()
