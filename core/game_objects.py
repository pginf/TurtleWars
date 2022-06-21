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
            for obj in self._mappings_of_groups[group]:
                if not obj.exist():
                    self._mappings_of_groups[group].remove(obj)
                    vs_comp: VisibleComponent = obj.get_component(VisibleComponent)
                    if vs_comp:
                        vs_comp.sprite.kill()

    def get_object(self, group: GameObjectGroup, index: int):
        return self._mappings_of_groups[group][index]

    def get_group_length(self, group: GameObjectGroup):
        return len(self._mappings_of_groups[group])

    def objects_update(self):
        for group in GameObjectGroup:
            for obj in self._mappings_of_groups[group]:
                if obj.exist():
                    obj.update()
        self.delete_objects()
        for group in reversed(GameObjectGroup):
            self._sprites_groups[group].draw(MainWindow.get_instance().get_surface())


if __name__ == "__main__":
    from core import Game
    from core import EventHandler
    from utils import Vector2D
    from components.movement_component import MovementComponent
    from components import BoxCollider

    game = Game()

    window = MainWindow.get_instance()

    a = GameObject()
    a.set_name("o1")
    a.set_position(Vector2D(window.WIDTH/2, 200))
    a.add_component(VisibleComponent)
    a.add_component(MovementComponent)
    a.add_component(BoxCollider)
    a.setup()

    game.game_objects.add_object_to_group(a)

    b = GameObject()
    b.set_name("o2")
    b.set_position(Vector2D(window.WIDTH / 2, 400))
    b.add_component(VisibleComponent)
    b.add_component(MovementComponent)
    b.add_component(BoxCollider)
    b.setup()

    game.game_objects.add_object_to_group(b)

    class AA:
        def on_click(self, result: EventHandler.OnMousePressArgs):
            print(result.x)
            print(result.y)

        def on_key_press(self, result: EventHandler.OnKeyboardPressArgs):
            print(result.key_pressed)

    EventHandler.get_instance().on_mouse_press.add(AA().on_click)
    EventHandler.get_instance().on_mouse_press.add(AA().on_click)
    EventHandler.get_instance().on_keyboard_press.add(AA().on_key_press)


    mca: MovementComponent = a.get_component(MovementComponent)
    mca.spin_blow(200)
    mca.spinning_friction = 300
    mca.force_blow(Vector2D(0, 200))
    mca.movement_friction = 1

    mcb: MovementComponent = b.get_component(MovementComponent)
    mcb.spin = -200



    game.loop()
