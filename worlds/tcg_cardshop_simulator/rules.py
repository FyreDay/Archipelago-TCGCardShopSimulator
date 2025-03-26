from .items import *
from .locations import *

def get_rules(world):
    rules = {
        "locations": {
        }
    }
def license_sum(world, list_of_item_name_list: list, state) -> int:
    """
    Returns sum that increments by 1 if state.has_any
    """
    return sum(
            [1 for item_list in list_of_item_name_list if
             state.has_any(set(item_list), world.player)]
    )

def has_all_ghosts(world, state) -> bool:
    for ghost in ghostlist:
        if not state.has(ghost.itemName, world.player):
            return False
    return True


def set_rules(world):
    for i in range(114):
        try:
            world.get_location(f"Level {i+2}").access_rule = lambda state: (state.can_reach_location(f"Level {i+1}", world.player) and (license_sum(world,license_item_list, state) >= i+1))
        except KeyError:
            pass
    for loc in locs:
        world.get_location(loc).access_rule = lambda state: state.has()

    if world.options.goal.value == 0:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Progressive Shop Expansion A", world.player, world.options.shop_expansion_goal.value)
    if world.options.goal.value == 1:
        world.multiworld.completion_condition[world.player] = lambda state: state.can_reach_location(f"Level {world.options.level_goal.value}", world.player)
    if world.options.goal.value == 2:
        world.multiworld.completion_condition[world.player] = lambda state: has_all_ghosts(world, state)