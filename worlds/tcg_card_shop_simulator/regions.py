from BaseClasses import Region, Entrance
from .locations import *


def create_region(world, name: str, hint: str):
    region = Region(name, world.player, world.multiworld)
    create_locations(world, region)
    world.multiworld.regions.append(region)
    return region


def connect_regions(world, from_name: str, to_name: str, entrance_name: str) -> Entrance:
    entrance_region = world.get_region(from_name)
    exit_region = world.get_region(to_name)
    return entrance_region.connect(exit_region, entrance_name)


def create_regions(world):
    create_region(world, "Menu", "Menu Region")
    create_region(world, "Level 1-4", "Level 1-4")
    create_region(world, "Level 5-9", "Level 5-9")
    create_region(world, "Level 10-14", "Level 10-14")
    create_region(world, "Level 15-19", "Level 15-19")
    create_region(world, "Level 20-24", "Level 20-24")
    create_region(world, "Level 25-29", "Level 25-29")
    create_region(world, "Level 30-34", "Level 30-34")
    create_region(world, "Level 35-39", "Level 35-39")
    create_region(world, "Level 40-44", "Level 40-44")
    create_region(world, "Level 45-49", "Level 45-49")
    create_region(world, "Level 50-54", "Level 50-54")
    create_region(world, "Level 55-59", "Level 55-59")
    create_region(world, "Level 60-64", "Level 60-64")
    create_region(world, "Level 65-69", "Level 65-69")
    create_region(world, "Level 70-74", "Level 70-74")
    create_region(world, "Level 75-79", "Level 75-79")
    create_region(world, "Level 80-84", "Level 80-84")
    create_region(world, "Level 85-89", "Level 85-89")
    create_region(world, "Level 90-94", "Level 90-94")
    create_region(world, "Level 95-99", "Level 95-99")
    create_region(world, "Level 100-104", "Level 100-104")
    create_region(world, "Level 105-109", "Level 105-109")
    create_region(world, "Level 110-115", "Level 110-115")

    create_region(world, "Common Card Pack", "Common Card Pack")
    create_region(world, "Rare Card Pack", "Rare Card Pack")
    create_region(world, "Epic Card Pack", "Epic Card Pack")
    create_region(world, "Legendary Card Pack", "Legendary Card Pack")
    create_region(world, "Destiny Common Card Pack", "Common Card Pack")
    create_region(world, "Destiny Rare Card Pack", "Rare Card Pack")
    create_region(world, "Destiny Epic Card Pack", "Epic Card Pack")
    create_region(world, "Destiny Legendary Card Pack", "Legendary Card Pack")



def connect_entrances(world):
    connect_regions(world, "Menu", "Level 1-4", "Level 1")
    connect_regions(world, "Menu", "Common Card Pack", "Common Card Pack")
    connect_regions(world, "Level 1-4", "Level 5-9", "Level 5")
    connect_regions(world, "Menu", "Rare Card Pack", "Rare Card Pack")
    connect_regions(world, "Level 5-9", "Level 10-14", "Level 10")
    connect_regions(world, "Menu", "Epic Card Pack", "Epic Card Pack")
    connect_regions(world, "Level 10-14", "Level 15-19", "Level 15")
    connect_regions(world, "Level 15-19", "Level 20-24", "Level 20")
    connect_regions(world, "Menu", "Legendary Card Pack", "Legendary Card Pack")
    connect_regions(world, "Level 20-24", "Level 25-29", "Level 25")
    connect_regions(world, "Menu", "Destiny Common Card Pack", "Destiny Common Card Pack")
    connect_regions(world, "Level 25-29", "Level 30-34", "Level 30")
    connect_regions(world, "Menu", "Destiny Rare Card Pack", "Destiny Rare Card Pack")
    connect_regions(world, "Level 30-34", "Level 35-39", "Level 35")
    connect_regions(world, "Level 35-39", "Level 40-44", "Level 40")
    connect_regions(world, "Menu", "Destiny Epic Card Pack", "Destiny Epic Card Pack")
    connect_regions(world, "Level 40-44", "Level 45-49", "Level 45")
    connect_regions(world, "Level 45-49", "Level 50-54", "Level 50")
    connect_regions(world, "Menu", "Destiny Legendary Card Pack", "Destiny Legendary Card Pack")
    connect_regions(world, "Level 50-54", "Level 55-59", "Level 55")
    connect_regions(world, "Level 55-59", "Level 60-64", "Level 60")
    connect_regions(world, "Level 60-64", "Level 65-69", "Level 65")
    connect_regions(world, "Level 65-69", "Level 70-74", "Level 70")
    connect_regions(world, "Level 70-74", "Level 75-79", "Level 75")
    connect_regions(world, "Level 75-79", "Level 80-84", "Level 80")
    connect_regions(world, "Level 80-84", "Level 85-89", "Level 85")
    connect_regions(world, "Level 85-89", "Level 90-94", "Level 90")
    connect_regions(world, "Level 90-94", "Level 95-99", "Level 95")
    connect_regions(world, "Level 95-99", "Level 100-104", "Level 100")
    connect_regions(world, "Level 100-104", "Level 105-109", "Level 105")
    connect_regions(world, "Level 105-109", "Level 110-115", "Level 110")
