from typing import List, Dict, Optional, Callable
import math

from BaseClasses import Region, Entrance, MultiWorld
from .locations import *

def create_region(world, name: str, hint: str):
    region = Region(name, world.player, world.multiworld)
    create_locations(world, region)
    world.multiworld.regions.append(region)


def create_regions(world):
    create_region(world, "Menu", "This is Menu Region")

