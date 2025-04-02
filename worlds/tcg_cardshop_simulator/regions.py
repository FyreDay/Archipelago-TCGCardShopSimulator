from typing import List, Dict, Optional, Callable
import math

from BaseClasses import Region, Entrance, MultiWorld
from .locations import *

def create_region(world, name: str, hint: str):
    region = Region(name, world.player, world.multiworld)
    create_locations(world, region)
    world.multiworld.regions.append(region)
    return region

def connect_regions(world, from_name: str, to_name: str, entrance_name: str) -> Entrance:
    entrance_region = world.get_region(from_name, world.player)
    exit_region = world.get_region(to_name, world.player)
    return entrance_region.connect(exit_region, entrance_name)

def create_regions(world):
    menu = create_region(world, "Menu", "This is Menu Region")

    for i in range(5, 115,5):
        create_region(world, f"Level {i-4} to Level {i}", "Levels")

    for i in range(5, 115, 5):
        if i == 5:
            connect_regions(world, "Menu", f"Level {i-4} to Level {i}", f"Menu -> Level {i-4} to Level {i}")
        else:
            connect_regions(world, f"Level {i-9} to Level {i-5}", f"Level {i-4} to Level {i}", f"Level {i-9} to Level {i-5} -> Level {i-4} to Level {i}")

