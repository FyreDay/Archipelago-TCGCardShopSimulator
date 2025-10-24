from typing import cast

from .data.LocationData import *

PLAY_TABLE_START_ID = 300
LEVEL_START_ID = 200
CARD_OPEN_START_ID = 1000
CARD_SELL_START_ID = 500
CARD_GRADE_START_ID=2000
SELL_CHECK_START_ID=3000


def get_sell_loc(key):
    for d in (tt_locations, pg1_locations, pg2_locations, pg3_locations):
        if key in d:
            return d[key]
    return None

def get_shop_locations(world):
    return [pg1_locations.copy(), pg2_locations.copy(), pg3_locations.copy(), tt_locations.copy()]

def get_license_checks(world,item_key:str ,loc: ShopLocation, is_starting_item:bool = False):
    if item_key is None or loc is None:
        return {}
    return get_license_checks_internal(world.options.sell_check_amount.value,world.options.extra_starting_item_checks.value,
                                item_key, loc, is_starting_item)

def get_license_checks_internal(check_amount, starting_num, item_key:str ,loc: ShopLocation, is_starting_item:bool = False):
    sell_item_locs = {}
    for n in range(1, check_amount + (starting_num if is_starting_item else 0) + 1):
        sell_item_locs[f"Sell {n} {"Boxes" if n>1 else "Box"} of {item_key}"] = SELL_CHECK_START_ID + (loc.code * 16) + (n-1)
    return sell_item_locs

def is_sell_excluded(name,loc_id):
    if not loc_id:
        return False
    if loc_id < SELL_CHECK_START_ID:
        return False
    if name.startswith("Sell ") and " Boxes" in name:
        try:
            # Remove "Sell " prefix and " Boxes" suffix, then convert to int
            n_str = name[len("Sell "):name.index(" Boxes")]
            n = int(n_str)
            if n > 8:
                return True
        except ValueError:
            # If conversion fails, skip
            pass
    return False


def get_play_table_checks(world):
    return get_play_table_checks_internal(world.options.play_table_checks.value)

def get_play_table_checks_internal(game_check_count: int):
    play_table_locs = {}
    if game_check_count > 0:
        for i in range(game_check_count):
            name = f"Customer Play Games #{i + 1}"
            hex_id = PLAY_TABLE_START_ID + i
            play_table_locs[name] = hex_id

    return play_table_locs

def get_level_checks(world, region_level, final_region: bool = False):
    return get_level_checks_internal(region_level, final_region, world.options.goal.value)

def get_level_checks_internal( region_level, final_region: bool = False, goal = 3):
    level_locs = {}
    if final_region:
        if goal == 0:
            level_locs[f"Level {region_level}"] = None
        else:
            level_locs[f"Level {region_level}"] = LEVEL_START_ID+region_level-1
        return level_locs


    end_level = region_level+5
    if region_level == 1:
        end_level = 5

    if region_level == 100:
        end_level = 101
    for l in range(region_level, end_level):
        if l == 1:
            continue
        level_locs[f"Level {l}"] = LEVEL_START_ID+l-1
    return level_locs

def decode_card(num):
    if not num:
        return None
    if (num & 0x10000) == 0:
        return None

    # Extract values
    expansion = (num >> 12) & 0xF
    border = (num >> 8) & 0xF
    foil = (num >> 7) & 0x1
    index = (num & 0x7F) - 1

    return expansion, border, foil, index

def check_card_exclude(world, num):
    decoded = decode_card(num)
    if decoded:
        exp, bord, foil, idx = decoded
        if bord >= Border.Silver.value:
            return True
        if foil:
            return True
        if world.random.random() > 0.5:
            return True
    return False

def get_in_difficulty_achievements(achievement_list, counter, difficulty):
    achievement_card_locs = {}
    for achievement in achievement_list:
        if achievement.difficulty <= difficulty:
            name = achievement.name
            achievement_card_locs[name] = counter
        counter = counter + 1
    return achievement_card_locs

def generate_card(name, index, border, foil, expansion, rarity):
    return f"{name} {border.name} {'Foil' if foil else 'NonFoil'} {expansion.name}", 0x10000 | (expansion.value << 12) | (border.value << 8) | (foil << 7) | (index + 1)

def get_card_checks(world, card_region: int):
    return get_card_checks_internal(world.options.card_sanity.value, world.options.border_sanity.value, world.options.foil_sanity.value,
                                    world.options.checks_opening_difficulty.value, card_region, True, world)

def get_card_checks_internal(card_sanity, border_sanity, foil_sanity, difficulty, card_region: int, create_hints:bool = False, world = None):
    card_locs = {}
    expansion = Expansion(1 if card_region >= 4 else 0)
    rarity = Rarity((card_region % 4) + 1)

    if card_sanity > 0:
        if card_sanity > card_region:
            for index, data in enumerate(card_rarity):
                data = cast(MonsterData, data)
                if data.rarity != rarity:
                    continue
                for border in Border:
                    if border_sanity < border.value:
                        continue

                    name, code = generate_card(data.name, index, border, 0, expansion, rarity)
                    card_locs[name] = code
                    if create_hints and world:
                        world.hints[code] = f"Card is in {expansion.name} {rarity.name} Packs"
                    if foil_sanity:
                        name, code = generate_card(data.name, index, border, 1, expansion, rarity)
                        card_locs[name] = code
                        if create_hints and world:
                            world.hints[code] = f"Card is in {expansion.name} {rarity.name} Packs"
    else:
        counter = CARD_OPEN_START_ID + rarity.value * 50 + expansion.value * 500
        card_locs = card_locs | get_in_difficulty_achievements(get_region_open_achievements(rarity, expansion), counter, difficulty)

    return card_locs

def get_sell_card_checks(difficulty: int, card_region: int):
    expansion = Expansion(1 if card_region >= 4 else 0)
    rarity = Rarity((card_region % 4) + 1)

    counter = CARD_SELL_START_ID + rarity.value * 50 + expansion.value * 250
    return get_in_difficulty_achievements(get_region_Sell_achievements(rarity, expansion), counter,
                                                           difficulty)

def get_generic_sell_card_checks(difficulty: int):
    return get_in_difficulty_achievements(generic_sell_achievements, CARD_GRADE_START_ID, difficulty)

def get_grading_card_checks(difficulty: int, card_region: int):
    expansion = Expansion(1 if card_region >= 4 else 0)
    rarity = Rarity((card_region % 4) + 1)

    counter = CARD_GRADE_START_ID + rarity.value * 50 + expansion.value * 250
    return get_in_difficulty_achievements(get_region_grading_achievements(rarity, expansion), counter,
                                          difficulty)

def get_generic_grading_card_checks(difficulty: int):
    return get_in_difficulty_achievements(generic_grading_achievements, CARD_GRADE_START_ID, difficulty)

def get_all_locations():
    all_locations = {}

    for card_region_id in range(8):
        all_locations.update(get_card_checks_internal(8, 5, True, 0, card_region_id))
        all_locations.update(get_card_checks_internal(0, 0, False, 30, card_region_id))
        all_locations.update(get_sell_card_checks(4, card_region_id))
        all_locations.update(get_grading_card_checks(4, card_region_id))

    all_locations.update(get_generic_sell_card_checks(4))
    all_locations.update(get_generic_grading_card_checks(4))

    for l in range(0, 105, 5):
        if l == 0:
            all_locations.update(get_level_checks_internal(True, 1))
            continue
        all_locations.update(get_level_checks_internal(True, l))

    all_locations.update(get_play_table_checks_internal(50))


    for item_key, item_data in pg1_locations.items():
        license_checks = get_license_checks_internal(16, 2, item_key, item_data)
        all_locations.update(license_checks)

    for item_key, item_data in pg2_locations.items():
        license_checks = get_license_checks_internal(16, 2, item_key, item_data)
        all_locations.update(license_checks)

    for item_key, item_data in pg3_locations.items():
        license_checks = get_license_checks_internal(16, 2, item_key, item_data)
        all_locations.update(license_checks)

    for item_key, item_data in tt_locations.items():
        license_checks = get_license_checks_internal(16, 2, item_key, item_data)
        all_locations.update(license_checks)

    return all_locations