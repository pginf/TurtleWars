from __future__ import annotations


import pygame.sprite

from core import MainWindow
from core import GameObjectGroup
from core import GameObject
from typing import Dict, List
from components import VisibleComponent


class GameObjects:
    _mappings_of_groups: Dict[GameObjectGroup, List[GameObject]] = {}
    _sprites_groups: Dict[GameObjectGroup, pygame.sprite.Group] = {}

    def __init__(self):
        for group in GameObjectGroup:
            self._mappings_of_groups[group] = []
            self._sprites_groups[group] = pygame.sprite.Group()

    def add_object_to_group(self, game_object: GameObject):
        self._mappings_of_groups[game_object.get_group()].append(game_object)
        # If object contains visible component then add sprite of this component to sprite group of object group
        obj_visible_comp = game_object.get_component(VisibleComponent)
        if isinstance(obj_visible_comp, VisibleComponent):
            self._sprites_groups[game_object.get_group()].add(obj_visible_comp.sprite)

    def delete_objects(self):
        for group in GameObjectGroup:
            self._mappings_of_groups[group] = list(
                filter(lambda game_object: game_object.exist(), self._mappings_of_groups[group]))

    def get_object_from_group(self, group: GameObjectGroup, index: int):
        return self._mappings_of_groups[group][index]

    def objects_update(self):
        for group in GameObjectGroup:
            for obj in self._mappings_of_groups[group]:
                obj.update()
            self._sprites_groups[group].draw(MainWindow.get_instance().get_surface())


if __name__ == "__main__":
    from core import Game
    from utils import Vector2D
    from components.movement_component import MovementComponent

    game = Game()

    window = MainWindow.get_instance()

    a = GameObject()
    a.set_position(Vector2D(window.WIDTH/2, 200))
    a.add_component(VisibleComponent)
    a.add_component(MovementComponent)
    a.setup()

    a.set_scale(Vector2D(2, 2))
    a.set_scale(Vector2D(3, 3))

    game.game_objects.add_object_to_group(a)

    b = GameObject()
    b.set_position(Vector2D(window.WIDTH / 2, 400))
    b.add_component(VisibleComponent)
    b.add_component(MovementComponent)
    b.setup()

    b.set_scale(Vector2D(3, 3))
    b.set_scale(Vector2D(2, 2))

    game.game_objects.add_object_to_group(b)

    mca: MovementComponent = a.get_component(MovementComponent)
    mca.spin_blow(200)
    mca.spinning_friction = 300
    mca.force_blow(Vector2D(300, 0))
    mca.movement_friction = 1

    mcb: MovementComponent = b.get_component(MovementComponent)
    mcb.spin = -200



    game.loop()
