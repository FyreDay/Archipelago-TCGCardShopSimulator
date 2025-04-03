from BaseClasses import LocationProgressType
from .items import *
from .locations import *


def has_card_pack(world, state, rarity):
    return state.has(f"{rarity} Pack (32)", world.player) or state.has(f"{rarity} Pack (64)", world.player) or state.has(f"{rarity} Box (4)", world.player) or state.has(f"{rarity} Box (8)", world.player)


def get_rules(world):
    rules = {
        "locations": {
            "Basic Card Pack (32)":
                lambda state:
                state.has("Basic Card Pack (32)", world.player),
            "Basic Card Pack (64)":
                lambda state:
                state.has("Basic Card Pack (32)", world.player),
            "Basic Card Box (4)":
                lambda state:
                state.has("Basic Card Box (4)", world.player),
            "Basic Card Box (8)":
                lambda state:
                state.has("Basic Card Box (8)", world.player),
            "Rare Card Pack (32)":
                lambda state:
                state.has("Rare Card Pack (32)", world.player),
            "Rare Card Pack (64)":
                lambda state:
                state.has("Rare Card Pack (64)", world.player),
            "Rare Card Box (4)":
                lambda state:
                state.has("Rare Card Box (4)", world.player),
            "Rare Card Box (8)":
                lambda state:
                state.has("Rare Card Box (8)", world.player),
            "Epic Card Pack (32)":
                lambda state:
                state.has("Epic Card Pack (32)", world.player),
            "Epic Card Pack (64)":
                lambda state:
                state.has("Epic Card Pack (64)", world.player),
            "Epic Card Box (4)":
                lambda state:
                state.has("Epic Card Box (4)", world.player),
            "Epic Card Box (8)":
                lambda state:
                state.has("Epic Card Box (8)", world.player),
            "Legendary Card Pack (32)":
                lambda state:
                state.has("Legendary Card Pack (32)", world.player),
            "Legendary Card Pack (64)":
                lambda state:
                state.has("Legendary Card Pack (64)", world.player),
            "Legendary Card Box (4)":
                lambda state:
                state.has("Legendary Card Box (4)", world.player),
            "Legendary Card Box (8)":
                lambda state:
                state.has("Legendary Card Box (8)", world.player),
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
                state.has("Basic Destiny Pack (32)", world.player),
            "Basic Destiny Pack (64)":
                lambda state:
                state.has("Basic Destiny Pack (64)", world.player),
            "Basic Destiny Box (4)":
                lambda state:
                state.has("Basic Destiny Box (4)", world.player),
            "Basic Destiny Box (8)":
                lambda state:
                state.has("Basic Destiny Box (8)", world.player),
            "Rare Destiny Pack (32)":
                lambda state:
                state.has("Rare Destiny Pack (32)", world.player),
            "Rare Destiny Pack (64)":
                lambda state:
                state.has("Rare Destiny Pack (64)", world.player),
            "Rare Destiny Box (4)":
                lambda state:
                state.has("Rare Destiny Box (4)", world.player),
            "Rare Destiny Box (8)":
                lambda state:
                state.has("Rare Destiny Box (8)", world.player),
            "Epic Destiny Pack (32)":
                lambda state:
                state.has("Epic Destiny Pack (32)", world.player),
            "Epic Destiny Pack (64)":
                lambda state:
                state.has("Epic Destiny Pack (64)", world.player),
            "Epic Destiny Box (4)":
                lambda state:
                state.has("Epic Destiny Box (4)", world.player),
            "Epic Destiny Box (8)":
                lambda state:
                state.has("Epic Destiny Box (8)", world.player),
            "Legendary Destiny Pack (32)":
                lambda state:
                state.has("Legendary Destiny Pack (32)", world.player),
            "Legendary Destiny Pack (64)":
                lambda state:
                state.has("Legendary Destiny Pack (64)", world.player),
            "Legendary Destiny Box (4)":
                lambda state:
                state.has("Legendary Destiny Box (4)", world.player),
            "Legendary Destiny Box (8)":
                lambda state:
                state.has("Legendary Destiny Box (8)", world.player),
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
                state.has("Cleanser (8)", world.player),
            "Cleanser (16)":
                lambda state:
                state.has("Cleanser (16)", world.player),
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
                state.has("Deck Box Red (8)", world.player),
            "Deck Box Red (16)":
                lambda state:
                state.has("Deck Box Red (16)", world.player),
            "Deck Box Green (8)":
                lambda state:
                state.has("Deck Box Green (8)", world.player),
            "Deck Box Green (16)":
                lambda state:
                state.has("Deck Box Green (16)", world.player),
            "Deck Box Blue (8)":
                lambda state:
                state.has("Deck Box Blue (8)", world.player),
            "Deck Box Blue (16)":
                lambda state:
                state.has("Deck Box Blue (16)", world.player),
            "Deck Box Yellow (8)":
                lambda state:
                state.has("Deck Box Yellow (8)", world.player),
            "Deck Box Yellow (16)":
                lambda state:
                state.has("Deck Box Yellow (16)", world.player),
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
            "Playmat (Dracunix1)":
                lambda state:
                state.has("Playmat (Dracunix1)", world.player),
            "Playmat (Dracunix2)":
                lambda state:
                state.has("Playmat (Dracunix2)", world.player),
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
                (state.has("Cleanser (8)", world.player) or state.has("Cleanser (16)", world.player)) and state.has("Play Table", world.player) and state.has("Progressive Shop Expansion A", world.player, 6),
            "Level 25":
                lambda state:
                state.can_reach_region("Common Card Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 8),
            "Level 30":
                lambda state:
                state.has("Checkout Counter", world.player) and state.has("Progressive Shop Expansion A", world.player, 10),
            "Level 35":
                lambda state:
                state.has("Warehouse Unlock", world.player) and state.has("Progressive Shop Expansion A", world.player, 12),
            "Level 40":
                lambda state:
                state.can_reach_region("Rare Card Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 14),
            "Level 45":
                lambda state:
                state.can_reach_region("Epic Card Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 16),
            "Level 50":
                lambda state:
                state.can_reach_region("Legendary Card Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 18),
            "Level 55":
                lambda state:
                state.can_reach_region("Destiny Common Card Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 20),
            "Level 60":
                lambda state:
                state.can_reach_region("Destiny Rare Card Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 22),
            "Level 65":
                lambda state:
                state.can_reach_region("Destiny Epic Card Pack", world.player) and state.has("Progressive Shop Expansion A", world.player, 24),
            "Level 70":
                lambda state:
                state.can_reach_region("Destiny Legendary Card Pack", world.player) and state.has("Progressive Shop Expansion B", world.player, 1),
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
            "Common Card Pack":
                lambda state:
                has_card_pack(world, state, "Basic Card"),
            "Rare Card Pack":
                lambda state:
                has_card_pack(world, state, "Rare Card"),
            "Epic Card Pack":
                lambda state:
                has_card_pack(world, state, "Epic Card"),
            "Legendary Card Pack":
                lambda state:
                has_card_pack(world, state, "Legendary Card"),
            "Destiny Common Card Pack":
                lambda state:
                has_card_pack(world, state, "Basic Destiny"),
            "Destiny Rare Card Pack":
                lambda state:
                has_card_pack(world, state, "Rare Destiny"),
            "Destiny Epic Card Pack":
                lambda state:
                has_card_pack(world, state, "Epic Destiny"),
            "Destiny Legendary Card Pack":
                lambda state:
                has_card_pack(world, state, "Legendary Destiny"),
            "Warehouse Door":
                lambda state:
                state.has("Warehouse Unlock", world.player),
        }
    }
    return rules


def set_rules(world):



    if world.options.goal.value != 1:
        finish_level = 72  # 72
        for i in range(finish_level, 116):
            world.get_location(f"Level {i}").progress_type = LocationProgressType.EXCLUDED

    rules_lookup = get_rules(world)

    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError as e:
            print(f"Key error, {e}")
            pass

    for location_name, rule in rules_lookup["locations"].items():
        try:
            world.get_location(location_name).access_rule = rule
        except KeyError as e:
            print(f"Key error, {e}")
            pass

    world.multiworld.register_indirect_condition("Level 25", "Common Card Pack",)
    world.multiworld.register_indirect_condition("Level 40", "Rare Card Pack",)
    world.multiworld.register_indirect_condition("Level 45", "Epic Card Pack",)
    world.multiworld.register_indirect_condition("Level 50", "Legendary Card Pack",)
    world.multiworld.register_indirect_condition("Level 55", "Destiny Common Card Pack")
    world.multiworld.register_indirect_condition("Level 60", "Destiny Rare Card Pack")
    world.multiworld.register_indirect_condition("Level 65", "Destiny Epic Card Pack")
    world.multiworld.register_indirect_condition("Level 70", "Destiny Legendary Card Pack")

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
