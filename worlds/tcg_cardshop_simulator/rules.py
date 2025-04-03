from BaseClasses import LocationProgressType
from .items import *
from .locations import *


def has_level(world, state, level):
    return state.can_reach_location(f"Level {level}", world.player),


def get_rules(world):
    rules = {
        "locations": {
            "Rare Card Pack (32)":
                lambda state:
                state.has("Progressive Rare Card Pack", world.player, 1),
            "Rare Card Pack (64)":
                lambda state:
                state.has("Progressive Rare Card Pack", world.player, 2),
            "Rare Card Box (4)":
                lambda state:
                state.has("Progressive Rare Card Pack", world.player, 3),
            "Rare Card Box (8)":
                lambda state:
                state.has("Progressive Rare Card Pack", world.player, 4),
            "Epic Card Pack (32)":
                lambda state:
                state.has("Progressive Epic Card Pack", world.player, 1),
            "Epic Card Pack (64)":
                lambda state:
                state.has("Progressive Epic Card Pack", world.player, 2),
            "Epic Card Box (4)":
                lambda state:
                state.has("Progressive Epic Card Pack", world.player, 3),
            "Epic Card Box (8)":
                lambda state:
                state.has("Progressive Epic Card Pack", world.player, 4),
            "Legendary Card Pack (32)":
                lambda state:
                state.has("Progressive Legendary Card Pack", world.player, 1),
            "Legendary Card Pack (64)":
                lambda state:
                state.has("Progressive Legendary Card Pack", world.player, 2),
            "Legendary Card Box (4)":
                lambda state:
                state.has("Progressive Legendary Card Pack", world.player, 3),
            "Legendary Card Box (8)":
                lambda state:
                state.has("Progressive Legendary Card Pack", world.player, 4),
            "Fire Battle Deck (18)":
                lambda state:
                state.has("Fire Battle Deck (18)", world.player),
            "Earth Battle Deck (18)":
                lambda state:
                state.has("Earth Battle Deck (18)", world.player),
            "Water Battle Deck (18)":
                lambda state:
                state.has("Water Battle Deck (18)", world.player),
            "Wind Battle Deck (18)":
                lambda state:
                state.has("Wind Battle Deck (18)", world.player),
            "Basic Destiny Pack (32)":
                lambda state:
                state.has("Progressive Basic Destiny Pack", world.player, 1),
            "Basic Destiny Pack (64)":
                lambda state:
                state.has("Progressive Basic Destiny Pack", world.player, 2),
            "Basic Destiny Box (4)":
                lambda state:
                state.has("Progressive Basic Destiny Pack", world.player, 3),
            "Basic Destiny Box (8)":
                lambda state:
                state.has("Progressive Basic Destiny Pack", world.player, 4),
            "Rare Destiny Pack (32)":
                lambda state:
                state.has("Progressive Rare Destiny Pack", world.player, 1),
            "Rare Destiny Pack (64)":
                lambda state:
                state.has("Progressive Rare Destiny Pack", world.player, 2),
            "Rare Destiny Box (4)":
                lambda state:
                state.has("Progressive Rare Destiny Pack", world.player, 3),
            "Rare Destiny Box (8)":
                lambda state:
                state.has("Progressive Rare Destiny Pack", world.player, 4),
            "Epic Destiny Pack (32)":
                lambda state:
                state.has("Progressive Epic Destiny Pack", world.player, 1),
            "Epic Destiny Pack (64)":
                lambda state:
                state.has("Progressive Epic Destiny Pack", world.player, 2),
            "Epic Destiny Box (4)":
                lambda state:
                state.has("Progressive Epic Destiny Pack", world.player, 3),
            "Epic Destiny Box (8)":
                lambda state:
                state.has("Progressive Epic Destiny Pack", world.player, 4),
            "Legendary Destiny Pack (32)":
                lambda state:
                state.has("Progressive Legendary Destiny Pack", world.player, 1),
            "Legendary Destiny Pack (64)":
                lambda state:
                state.has("Progressive Legendary Destiny Pack", world.player, 2),
            "Legendary Destiny Box (4)":
                lambda state:
                state.has("Progressive Legendary Destiny Pack", world.player, 3),
            "Legendary Destiny Box (8)":
                lambda state:
                state.has("Progressive Legendary Destiny Pack", world.player, 4),
            "Fire Destiny Deck (18)":
                lambda state:
                state.has("Fire Destiny Deck (18)", world.player),
            "Earth Destiny Deck (18)":
                lambda state:
                state.has("Earth Destiny Deck (18)", world.player),
            "Water Destiny Deck (18)":
                lambda state:
                state.has("Water Destiny Deck (18)", world.player),
            "Wind Destiny Deck (18)":
                lambda state:
                state.has("Wind Destiny Deck (18)", world.player),
            "Cleanser (8)":
                lambda state:
                state.has("Progressive Cleanser", world.player, 1),
            "Cleanser (16)":
                lambda state:
                state.has("Progressive Cleanser", world.player, 2),
            "Card Sleeves (Clear)":
                lambda state:
                state.has("Card Sleeves (Clear)", world.player),
            "Card Sleeves (Tetramon)":
                lambda state:
                state.has("Card Sleeves (Tetramon)", world.player),
            "D20 Dice Red (16)":
                lambda state:
                state.has("D20 Dice Red (16)", world.player),
            "D20 Dice Blue (16)":
                lambda state:
                state.has("D20 Dice Blue (16)", world.player),
            "D20 Dice Black (16)":
                lambda state:
                state.has("D20 Dice Black (16)", world.player),
            "D20 Dice White (16)":
                lambda state:
                state.has("D20 Dice White (16)", world.player),
            "Card Sleeves (Fire)":
                lambda state:
                state.has("Card Sleeves (Fire)", world.player),
            "Card Sleeves (Earth)":
                lambda state:
                state.has("Card Sleeves (Earth)", world.player),
            "Card Sleeves (Water)":
                lambda state:
                state.has("Card Sleeves (Water)", world.player),
            "Card Sleeves (Wind)":
                lambda state:
                state.has("Card Sleeves (Wind)", world.player),
            "Deck Box Red (8)":
                lambda state:
                state.has("Progressive Deck Box Red", world.player, 1),
            "Deck Box Red (16)":
                lambda state:
                state.has("Progressive Deck Box Red", world.player, 2),
            "Deck Box Green (8)":
                lambda state:
                state.has("Progressive Deck Box Green", world.player, 1),
            "Deck Box Green (16)":
                lambda state:
                state.has("Progressive Deck Box Green", world.player, 2),
            "Deck Box Blue (8)":
                lambda state:
                state.has("Progressive Deck Box Blue", world.player, 1),
            "Deck Box Blue (16)":
                lambda state:
                state.has("Progressive Deck Box Blue", world.player, 2),
            "Deck Box Yellow (8)":
                lambda state:
                state.has("Progressive Deck Box Yellow", world.player, 1),
            "Deck Box Yellow (16)":
                lambda state:
                state.has("Progressive Deck Box Yellow", world.player, 2),
            "Collection Book (4)":
                lambda state:
                state.has("Collection Book (4)", world.player),
            "Premium Collection Book (4)":
                lambda state:
                state.has("Premium Collection Book (4)", world.player),
            "Playmat (Drilceros)":
                lambda state:
                state.has("Playmat (Drilceros)", world.player),
            "Playmat (Clamigo)":
                lambda state:
                state.has("Playmat (Clamigo)", world.player),
            "Playmat (Wispo)":
                lambda state:
                state.has("Playmat (Wispo)", world.player),
            "Playmat (Lunight)":
                lambda state:
                state.has("Playmat (Lunight)", world.player),
            "Playmat (Kyrone)":
                lambda state:
                state.has("Playmat (Kyrone)", world.player),
            "Playmat (Duel)":
                lambda state:
                state.has("Playmat (Duel)", world.player),
            "Playmat (Dracunix)":
                lambda state:
                state.has("Playmat (Dracunix)", world.player),
            "Playmat (The Four Dragons)":
                lambda state:
                state.has("Playmat (The Four Dragons)", world.player),
            "Playmat (Drakon)":
                lambda state:
                state.has("Playmat (Drakon)", world.player),
            "Playmat (GigatronX Evo)":
                lambda state:
                state.has("Playmat (GigatronX Evo)", world.player),
            "Playmat (Fire)":
                lambda state:
                state.has("Playmat (Fire)", world.player),
            "Playmat (Earth)":
                lambda state:
                state.has("Playmat (Earth)", world.player),
            "Playmat (Water)":
                lambda state:
                state.has("Playmat (Water)", world.player),
            "Playmat (Wind)":
                lambda state:
                state.has("Playmat (Wind)", world.player),
            "Playmat (Tetramon)":
                lambda state:
                state.has("Playmat (Tetramon)", world.player),
            "Pigni Plushie (12)":
                lambda state:
                state.has("Pigni Plushie (12)", world.player),
            "Nanomite Plushie (16)":
                lambda state:
                state.has("Nanomite Plushie (16)", world.player),
            "Minstar Plushie (24)":
                lambda state:
                state.has("Minstar Plushie (24)", world.player),
            "Nocti Plushie (6)":
                lambda state:
                state.has("Nocti Plushie (6)", world.player),
            "Burpig Figurine (12)":
                lambda state:
                state.has("Burpig Figurine (12)", world.player),
            "Decimite Figurine (8)":
                lambda state:
                state.has("Decimite Figurine (8)", world.player),
            "Trickstar Figurine (12)":
                lambda state:
                state.has("Trickstar Figurine (12)", world.player),
            "Lunight Figurine (8)":
                lambda state:
                state.has("Lunight Figurine (8)", world.player),
            "Inferhog Figurine (2)":
                lambda state:
                state.has("Inferhog Figurine (2)", world.player),
            "Meganite Figurine (2)":
                lambda state:
                state.has("Meganite Figurine (2)", world.player),
            "Princestar Figurine (2)":
                lambda state:
                state.has("Princestar Figurine (2)", world.player),
            "Vampicant Figurine (2)":
                lambda state:
                state.has("Vampicant Figurine (2)", world.player),
            "Blazoar Plushie (2)":
                lambda state:
                state.has("Blazoar Plushie (2)", world.player),
            "Giganite Statue (2)":
                lambda state:
                state.has("Giganite Statue (2)", world.player),
            "Kingstar Plushie (2)":
                lambda state:
                state.has("Kingstar Plushie (2)", world.player),
            "Dracunix Figurine (1)":
                lambda state:
                state.has("Dracunix Figurine (1)", world.player),
            "Bonfiox Plushie (8)":
                lambda state:
                state.has("Bonfiox Plushie (8)", world.player),
            "Drilceros Action Figure (4)":
                lambda state:
                state.has("Drilceros Action Figure (4)", world.player),
            "ToonZ Plushie (6)":
                lambda state:
                state.has("ToonZ Plushie (6)", world.player),
            "Small Cabinet":
                lambda state:
                state.has("Small Cabinet", world.player),
            "Small Metal Rack":
                lambda state:
                state.has("Small Metal Rack", world.player),
            "Single Sided Shelf":
                lambda state:
                state.has("Single Sided Shelf", world.player),
            "Double Sided Shelf":
                lambda state:
                state.has("Double Sided Shelf", world.player),
            "Wide Shelf":
                lambda state:
                state.has("Wide Shelf", world.player),
            "Card Table":
                lambda state:
                state.has("Progressive Card Table", world.player, 1),
            "Small Card Display":
                lambda state:
                state.has("Progressive Card Display", world.player, 1),
            "Card Display Table":
                lambda state:
                state.has("Progressive Card Display", world.player, 2),
            "Vintage Card Table":
                lambda state:
                state.has("Progressive Card Table", world.player, 2),
            "Big Card Display":
                lambda state:
                state.has("Progressive Card Display", world.player, 3),
            "Small Personal Shelf":
                lambda state:
                state.has("Progressive Personal Shelf", world.player, 1),
            "Big Personal Shelf":
                lambda state:
                state.has("Progressive Personal Shelf", world.player, 2),
            "Huge Personal Shelf":
                lambda state:
                state.has("Progressive Personal Shelf", world.player, 3),
            "Auto Scent M100":
                lambda state:
                state.has("Progressive Auto Scent", world.player, 1),
            "Auto Scent G500":
                lambda state:
                state.has("Progressive Auto Scent", world.player, 2),
            "Auto Scent T100":
                lambda state:
                state.has("Progressive Auto Scent", world.player, 3),
            "Small Warehouse Shelf":
                lambda state:
                state.has("Small Warehouse Shelf", world.player),
            "Big Warehouse Shelf":
                lambda state:
                state.has("Big Warehouse Shelf", world.player),
            "Play Table":
                lambda state:
                state.has("Play Table", world.player),
            "Workbench":
                lambda state:
                state.has("Workbench", world.player),
            "Trash Bin":
                lambda state:
                state.has("Trash Bin", world.player),
            "Checkout Counter":
                lambda state:
                state.has("Checkout Counter", world.player),
            "System Gate #1":
                lambda state:
                state.has("System Gate #1", world.player),
            "System Gate #2":
                lambda state:
                state.has("System Gate #2", world.player),
            "Mafia Works":
                lambda state:
                state.has("Mafia Works", world.player),
            "Necromonsters":
                lambda state:
                state.has("Necromonsters", world.player),
            "Claim!":
                lambda state:
                state.has("Claim!", world.player),
            "Penny Sleeves":
                lambda state:
                state.has("Penny Sleeves", world.player),
            "Tower Deckbox":
                lambda state:
                state.has("Tower Deckbox", world.player),
            "Magnetic Holder":
                lambda state:
                state.has("Magnetic Holder", world.player),
            "Toploader":
                lambda state:
                state.has("Toploader", world.player),
            "Card Preserver":
                lambda state:
                state.has("Card Preserver", world.player),
            "Playmat Gray":
                lambda state:
                state.has("Playmat Gray", world.player),
            "Playmat Green":
                lambda state:
                state.has("Playmat Green", world.player),
            "Playmat Purple":
                lambda state:
                state.has("Playmat Purple", world.player),
            "Playmat Yellow":
                lambda state:
                state.has("Pocket Pages", world.player),
            "Pocket Pages":
                lambda state:
                state.has("Pocket Pages", world.player),
            "Card Holder":
                lambda state:
                state.has("Card Holder", world.player),
            "Collectors Album":
                lambda state:
                state.has("Collectors Album", world.player),
        },
        "entrances": {
            "Level 5":
                lambda state:
                state.has("Progressive Card Table", world.player) and state.has("Small Cabinet", world.player) and state.has("Single Sided Shelf", world.player) and state.has("Progressive Shop Expansion A", world.player, 1),
            "Level 10":
                lambda state:
                state.has("Progressive Card Table", world.player) and state.has("Progressive Warehouse Shelf", world.player) and state.has("Progressive Shop Expansion A", world.player, 2),
            "Level 15":
                lambda state:
                state.has("Worker - Zachery", world.player) and state.has("Trash Bin", world.player) and state.has("Progressive Shop Expansion A", world.player, 4),
            "Level 20":
                lambda state:
                state.has("Progressive Cleanser", world.player) and state.has("Play Table", world.player) and state.has("Progressive Shop Expansion A", world.player, 6),
            "Level 25":
                lambda state:
                state.has("Progressive Basic Card Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 8),
            "Level 30":
                lambda state:
                state.has("Checkout Counter", world.player) and state.has("Progressive Shop Expansion A", world.player, 10),
            "Level 35":
                lambda state:
                state.has("Warehouse Unlock", world.player) and state.has("Progressive Shop Expansion A", world.player, 12),
            "Level 40":
                lambda state:
                state.has("Progressive Rare Card Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 14),
            "Level 45":
                lambda state:
                state.has("Progressive Epic Card Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 16),
            "Level 50":
                lambda state:
                state.has("Progressive Legendary Card Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 18),
            "Level 55":
                lambda state:
                state.has("Progressive Basic Destiny Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 20),
            "Level 60":
                lambda state:
                state.has("Progressive Rare Destiny Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 22),
            "Level 65":
                lambda state:
                state.has("Progressive Epic Destiny Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 24),
            "Level 70":
                lambda state:
                state.has("Progressive Shop Expansion B", world.player, 1),
            "Level 75":
                lambda state:
                state.has("Progressive Shop Expansion B", world.player, 2),
            "Level 80":
                lambda state:
                state.has("Progressive Shop Expansion B", world.player, 3),
            "Level 85":
                lambda state:
                state.has("Progressive Shop Expansion B", world.player, 4),
            "Level 90":
                lambda state:
                state.has("Progressive Shop Expansion B", world.player, 5),
            "Level 95":
                lambda state:
                state.has("Progressive Shop Expansion B", world.player, 6),
            "Level 100":
                lambda state:
                state.has("Progressive Shop Expansion B", world.player, 7),
            "Level 105":
                lambda state:
                state.has("Progressive Shop Expansion B", world.player, 8),
            "Level 110":
                lambda state:
                state.has("Progressive Shop Expansion B", world.player, 9),
        }
    }
    return rules


def set_rules(world):

    finish_level = 51

    if world.options.goal.value == 1:
        finish_level = world.options.level_goal.value + 1
    for i in range(finish_level, 116):
        world.get_location(f"Level {i}").progress_type = LocationProgressType.EXCLUDED

    rules_lookup = get_rules(world)

    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError:
            pass

    for location_name, rule in rules_lookup["locations"].items():
        try:
            world.get_location(location_name).access_rule = rule
        except KeyError:
            pass

    for pA in range(1, 31):
        world.get_location(f"Shop A Expansion {pA}").access_rule = lambda state: state.has("Progressive Shop Expansion A", world.player, pA)

    for pB in range(1, 15):
        world.get_location(f"Shop B Expansion {pB}").access_rule = lambda state: (state.has("Progressive Shop Expansion B", world.player, pB)
                                                                                  and state.has("Warehouse Unlock", world.player))

    if world.options.card_sanity.value > 0:
        for location_name, item_name in rarity_item_dict.items():
            world.multiworld.get_location(location_name, world.player).access_rule = lambda state: state.has(item_name, world.player)

    # victory conditions
    if world.options.goal.value == 0:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Progressive Shop Expansion A", world.player, world.options.shop_expansion_goal.value)

    if world.options.goal.value == 1:
        world.multiworld.get_location(f"Level {world.options.level_goal.value}", world.player).place_locked_item(TCGSimulatorItem("Victory", ItemClassification.progression, None, world.player))
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)

    if world.options.goal.value == 2:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Progressive Ghost Card", world.player, world.options.ghost_goal_amount.value)
