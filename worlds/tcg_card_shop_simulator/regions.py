from enum import IntEnum

from BaseClasses import Region, Entrance
from . import locations
from .locations import *

class CardRegion(IntEnum):
    BASIC = 0
    RARE = 1
    EPIC = 2
    LEGENDARY = 3
    DESTINY_BASIC = 4
    DESTINY_RARE = 5
    DESTINY_EPIC = 6
    DESTINY_LEGENDARY = 7

card_region_names = {
    CardRegion.BASIC: "Basic Card Pack",
    CardRegion.RARE: "Rare Card Pack",
    CardRegion.EPIC: "Epic Card Pack",
    CardRegion.LEGENDARY: "Legendary Card Pack",
    CardRegion.DESTINY_BASIC: "Destiny Basic Card Pack",
    CardRegion.DESTINY_RARE: "Destiny Rare Card Pack",
    CardRegion.DESTINY_EPIC: "Destiny Epic Card Pack",
    CardRegion.DESTINY_LEGENDARY: "Destiny Legendary Card Pack",
}

def create_location(world, region, name: str, code: int, excluded: bool = False):
    location = Location(world.player, name, code, region)
    if excluded:
        location.progress_type = LocationProgressType.EXCLUDED
    region.locations.append(location)

def add_locations(world, region, locations_dict):
    for (key, code) in locations_dict.items():
        create_location(world, region, key, code)

def create_card_locations(world, card_locs, region):
    for (key, data) in card_locs.items():
        if data.region != region.name:
            continue
        excluded = False
        if world.random.random() > 0.6:
            excluded = False
        create_location(world, region, key, data.code, excluded)

def create_region(world, name: str, hint: str, locations_dict):
    region = Region(name, world.player, world.multiworld)
    add_locations(world, region, locations_dict)
    world.multiworld.regions.append(region)
    return region

def assign_random_level_location(world, region, shop_locs, level_grouped_locs, shop_id, level):
    available_keys = list(shop_locs[shop_id].keys())
    if len(available_keys) == 0:
        return None, None
    random_key = random.choice(available_keys)
    loc:ShopLocation = shop_locs[shop_id].pop(random_key)
    level_grouped_locs[shop_id][loc.code] = level
    return random_key, loc

def create_level_region(world, name: str, hint: str, shop_locs, level_grouped_locs, starting_region:bool = False, final_region:bool = False):
    region = Region(name, world.player, world.multiworld)
    match = re.search(r'\d+', name)

    if not final_region:
        s1_key1, s1_loc1 = assign_random_level_location(world, region, shop_locs, level_grouped_locs, 0, int(match.group(0)))
        s1_key2, s1_loc2 = assign_random_level_location(world, region, shop_locs, level_grouped_locs, 0, int(match.group(0)))
        s2_key1, s2_loc1 = assign_random_level_location(world, region, shop_locs, level_grouped_locs, 1, int(match.group(0)))
        s2_key2, s2_loc2 = assign_random_level_location(world, region, shop_locs, level_grouped_locs, 1, int(match.group(0)))
        s3_key, s3_loc = assign_random_level_location(world, region, shop_locs, level_grouped_locs, 2, int(match.group(0)))
        tt_key, tt_loc = assign_random_level_location(world, region, shop_locs, level_grouped_locs, 3, int(match.group(0)))

        add_locations(world, region, locations.get_license_checks(world, s1_key1, s1_loc1, starting_region))
        add_locations(world, region, locations.get_license_checks(world, s1_key2, s1_loc2))
        add_locations(world, region, locations.get_license_checks(world, s2_key1, s2_loc1, starting_region))
        add_locations(world, region, locations.get_license_checks(world, s2_key2, s2_loc2))
        add_locations(world, region, locations.get_license_checks(world, s3_key, s3_loc, starting_region))
        add_locations(world, region, locations.get_license_checks(world, tt_key, tt_loc))

        if starting_region:
            world.starting_item_ids = [s1_loc1.code, s2_loc1.code, s3_loc.code]

    add_locations(world, region, locations.get_level_checks(world, int(match.group(0)), final_region))

    world.multiworld.regions.append(region)
    return region

def create_pack_region(world, card_region: CardRegion, hint: str, level):
    if level is None:
        print(f"{card_region_names[card_region]} is not in the world")
        # region = Region(card_region_names[card_region], world.player, world.multiworld)
        # world.multiworld.regions.append(region)
    else:
        create_region(world, card_region_names[card_region], hint, get_card_checks(world, card_region))


def create_regions(world):
    shop_locs: list[dict[int, ShopLocation]] = locations.get_shop_locations(world)
    level_grouped_locs: [list[dict[int, int]]] = [{},{},{},{}]

    create_region(world, "Menu", "Menu Region", {})
    for l in range(0,world.options.max_level.value+5, 5):
        if l == 0:
            create_level_region(world, "Level 1-4", "Level 1-4", shop_locs, level_grouped_locs, True)
            continue
        if world.options.max_level.value == l:
            if l == 100:
                create_level_region(world, "Level 100", "Level 100", shop_locs, level_grouped_locs, final_region=True)
            else:
                create_level_region(world, f"Level {l}-{l + 4}", f"Level {l}-{l + 4}", shop_locs, level_grouped_locs, final_region=True)
            continue
        create_level_region(world, f"Level {l}-{l+4}", f"Level {l}-{l+4}", shop_locs, level_grouped_locs)


    create_pack_region(world, CardRegion.BASIC, card_region_names[CardRegion.BASIC], min([level_grouped_locs[0][item_id] for item_id in [190,1] if item_id in level_grouped_locs[0]], default=None))
    create_pack_region(world, CardRegion.RARE, card_region_names[CardRegion.RARE], min([level_grouped_locs[0][item_id] for item_id in [2,3] if item_id in level_grouped_locs[0]], default=None))
    create_pack_region(world, CardRegion.EPIC, card_region_names[CardRegion.EPIC], min([level_grouped_locs[0][item_id] for item_id in [4,5] if item_id in level_grouped_locs[0]], default=None))
    create_pack_region(world, CardRegion.LEGENDARY, card_region_names[CardRegion.LEGENDARY], min([level_grouped_locs[0][item_id] for item_id in [6,7] if item_id in level_grouped_locs[0]], default=None))
    create_pack_region(world, CardRegion.DESTINY_BASIC, card_region_names[CardRegion.DESTINY_BASIC], min([level_grouped_locs[0][item_id] for item_id in [8,9] if item_id in level_grouped_locs[0]], default=None))
    create_pack_region(world, CardRegion.DESTINY_RARE, card_region_names[CardRegion.DESTINY_RARE], min([level_grouped_locs[0][item_id] for item_id in [10,11] if item_id in level_grouped_locs[0]], default=None))
    create_pack_region(world, CardRegion.DESTINY_EPIC, card_region_names[CardRegion.DESTINY_EPIC], min([level_grouped_locs[0][item_id] for item_id in [12,13] if item_id in level_grouped_locs[0]], default=None))
    create_pack_region(world, CardRegion.DESTINY_LEGENDARY, card_region_names[CardRegion.DESTINY_LEGENDARY], min([level_grouped_locs[0][item_id] for item_id in [14,15] if item_id in level_grouped_locs[0]], default=None))

    if world.options.play_table_checks.value > 0:
        create_region(world, "Play Tables", "Play Tables", locations.get_play_table_checks(world))
    if world.options.sell_card_check_count.value > 0:
        create_region(world, "Sell Tetramon", "Sell Tetramon", locations.get_sell_card_checks(world, False))
        create_region(world, "Sell Destiny", "Sell Destiny", locations.get_sell_card_checks(world, True))

    return level_grouped_locs








def connect_regions(world, from_name: str, to_name: str, entrance_name: str) -> Entrance:
    entrance_region = world.get_region(from_name)
    exit_region = world.get_region(to_name)
    return entrance_region.connect(exit_region, entrance_name)

def connect_pack_region(world, card_region, level):
    if level is None:
        return
    end_level = level+4 if level != 1 else 4

    connect_regions(world, f"Level {level}-{end_level}", card_region_names[card_region], card_region_names[card_region])


def connect_entrances(world):
    connect_pack_region(world, CardRegion.BASIC, min([world.pg1_licenses[item_id] for item_id in [190,1] if item_id in world.pg1_licenses], default=None))
    connect_pack_region(world, CardRegion.RARE, min([world.pg1_licenses[item_id] for item_id in [2,3] if item_id in world.pg1_licenses], default=None))
    connect_pack_region(world, CardRegion.EPIC, min([world.pg1_licenses[item_id] for item_id in [4,5] if item_id in world.pg1_licenses], default=None))
    connect_pack_region(world, CardRegion.LEGENDARY, min([world.pg1_licenses[item_id] for item_id in [6,7] if item_id in world.pg1_licenses], default=None))
    connect_pack_region(world, CardRegion.DESTINY_BASIC, min([world.pg1_licenses[item_id] for item_id in [8,9] if item_id in world.pg1_licenses], default=None))
    connect_pack_region(world, CardRegion.DESTINY_RARE, min([world.pg1_licenses[item_id] for item_id in [10,11] if item_id in world.pg1_licenses], default=None))
    connect_pack_region(world, CardRegion.DESTINY_EPIC, min([world.pg1_licenses[item_id] for item_id in [12,13] if item_id in world.pg1_licenses], default=None))
    connect_pack_region(world, CardRegion.DESTINY_LEGENDARY, min([world.pg1_licenses[item_id] for item_id in [14,15] if item_id in world.pg1_licenses], default=None))

    connect_regions(world, "Menu", "Level 1-4", "Level 1")
    if world.options.play_table_checks.value > 0:
        connect_regions(world, "Level 1-4", "Play Tables", "Play Table Found")
    if world.options.sell_card_check_count.value > 0:
        connect_regions(world, "Level 1-4", "Sell Tetramon", "Sell Tetramon")
        connect_regions(world, "Level 1-4", "Sell Destiny", "Sell Destiny")

    for l in range(0,world.options.max_level.value, 5):
        if l == 0:
            connect_regions(world, "Level 1-4", "Level 5-9", "Level 5")
            continue
        if l == 95:
            connect_regions(world, "Level 95-99", "Level 100", "Level 100")
            continue
        connect_regions(world, f"Level {l}-{l+4}", f"Level {l+5}-{l+5+4}", f"Level {l+5}")

