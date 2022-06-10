from __future__ import annotations
from core import GameObjectGroup
from core import GameObject
from typing import Dict, List

class GameObjects:

    _mappings_of_groups: Dict[GameObjectGroup, List[GameObject]] = {}

    def __init__(self):
        for group in GameObjectGroup:
            self._mappings_of_groups[group] = []

    def add_object_to_group(self, game_object: GameObject):
        self._mappings_of_groups[game_object.get_group()].append(game_object)

    def delete_objects(self):
        for group in self._mappings_of_groups:
            self._mappings_of_groups[group] = list(filter(lambda game_object: game_object.exist(), self._mappings_of_groups[group]))

    def get_object_from_group(self, group: GameObjectGroup, index: int):
        return self._mappings_of_groups[group][index]

if __name__ == "__main__":
    groupp = GameObjectGroup.NONE
    game_objects = GameObjects()
    simple_game_object = GameObject()
    game_objects.add_object_to_group(simple_game_object)
    print(game_objects.get_object_from_group(groupp, 0).get_name())
    simple_game_object.set_exist(False)
    game_objects.delete_objects()