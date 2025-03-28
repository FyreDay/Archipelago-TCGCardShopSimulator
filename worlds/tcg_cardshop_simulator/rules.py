from .items import *
from .locations import *

def license_sum(world, license_list, state, amount) -> int:
    """
    Returns sum that increments by 1 if state.has_any
    """
    # s = 0;
    # for code, name, classification, amount in list_of_item_name_list:
    #     if state.has(name, world.player):
    #         s = s+1
    #         print(s)

    # return sum(
    #     [1 for code, item_name, c,item_amount in
    #      list_of_item_name_list if state.count(item_name, world.player) >= item_amount]
    # )
    v = sum([state.count(item_name, world.player) for code,item_name, c, amount in license_list])
    print(v)
    return amount <= sum([state.count(item_name, world.player) for code,item_name, c, seed_amount in license_list])

def requires_level(world, state, level):
    return state.can_reach_location(f"Level {level}", world.player),

def has_all_ghosts(world, state) -> bool:
    for ghost in ghostlist:
        if not state.has(ghost.itemName, world.player):
            return False
    return True

def get_rules(world):
    rules = {
        "locations": {
            "Basic Card Pack (64)":
                lambda state:
                    state.has("Progressive Basic Card Pack", world.player,1) or requires_level(world, state, 2),
            "Basic Card Box (4)":
                lambda state:
                    state.has("Progressive Basic Card Pack", world.player,2) or requires_level(world, state, 3),
            "Basic Card Box (8)":
                lambda state:
                    state.has("Progressive Basic Card Pack", world.player,3) or requires_level(world, state, 4),
            "Rare Card Pack (32)":
                lambda state:
                    state.has("Progressive Rare Card Pack", world.player,1) or requires_level(world, state, 5),
            "Rare Card Pack (64)":
                lambda state:
                    state.has("Progressive Rare Card Pack", world.player,2) or requires_level(world, state, 8),
            "Rare Card Box (4)":
                lambda state:
                    state.has("Progressive Rare Card Pack", world.player,3) or requires_level(world, state, 9),
            "Rare Card Box (8)":
                lambda state:
                    state.has("Progressive Rare Card Pack", world.player,4) or requires_level(world, state, 12),
            "Epic Card Pack (32)":
                lambda state:
                    state.has("Progressive Epic Card Pack", world.player,1) or requires_level(world, state, 12),
            "Epic Card Pack (64)":
                lambda state:
                    state.has("Progressive Epic Card Pack", world.player,2) or requires_level(world, state, 15),
            "Epic Card Box (4)":
                lambda state:
                    state.has("Progressive Epic Card Pack", world.player,3) or requires_level(world, state, 16),
            "Epic Card Box (8)":
                lambda state:
                    state.has("Progressive Epic Card Pack", world.player,4) or requires_level(world, state, 19),
            "Legendary Card Pack (32)":
                lambda state:
                    state.has("Progressive Legendary Card Pack", world.player,1) or requires_level(world, state, 20),
            "Legendary Card Pack (64)":
                lambda state:
                    state.has("Progressive Legendary Card Pack", world.player,2) or requires_level(world, state, 26),
            "Legendary Card Box (4)":
                lambda state:
                    state.has("Progressive Legendary Card Pack", world.player,3) or requires_level(world, state, 23),
            "Legendary Card Box (8)":
                lambda state:
                    state.has("Progressive Legendary Card Pack", world.player,4) or requires_level(world, state, 30),
            "Fire Battle Deck (18)":
                lambda state:
                    state.has("Fire Battle Deck (18)", world.player) or requires_level(world, state, 9),
            "Earth Battle Deck (18)":
                lambda state:
                    state.has("Earth Battle Deck (18)", world.player) or requires_level(world, state, 14),
            "Water Battle Deck (18)":
                lambda state:
                    state.has("Water Battle Deck (18)", world.player) or requires_level(world, state, 17),
            "Wind Battle Deck (18)":
                lambda state:
                    state.has("Wind Battle Deck (18)", world.player) or requires_level(world, state, 22),
            "Basic Destiny Pack (32)":
                lambda state:
                    state.has("Progressive Basic Destiny Pack", world.player, 1) or requires_level(world, state, 25),
            "Basic Destiny Pack (64)":
                lambda state:
                    state.has("Progressive Basic Destiny Pack", world.player, 2) or requires_level(world, state, 29),
            "Basic Destiny Box (4)":
                lambda state:
                    state.has("Progressive Basic Destiny Pack", world.player, 3) or requires_level(world, state, 27),
            "Basic Destiny Box (8)":
                lambda state:
                    state.has("Progressive Basic Destiny Pack", world.player, 4) or requires_level(world, state, 31),
            "Rare Destiny Pack (32)":
                lambda state:
                    state.has("Progressive Rare Destiny Pack", world.player, 1) or requires_level(world, state, 30),
            "Rare Destiny Pack (64)":
                lambda state:
                    state.has("Progressive Rare Destiny Pack", world.player, 2) or requires_level(world, state, 35),
            "Rare Destiny Box (4)":
                lambda state:
                    state.has("Progressive Rare Destiny Pack", world.player, 3) or requires_level(world, state, 32),
            "Rare Destiny Box (8)":
                lambda state:
                    state.has("Progressive Rare Destiny Pack", world.player, 4) or requires_level(world, state, 37),
            "Epic Destiny Pack (32)":
                lambda state:
                    state.has("Progressive Epic Destiny Pack", world.player, 1) or requires_level(world, state, 40),
            "Epic Destiny Pack (64)":
                lambda state:
                    state.has("Progressive Epic Destiny Pack", world.player, 2) or requires_level(world, state, 48),
            "Epic Destiny Box (4)":
                lambda state:
                    state.has("Progressive Epic Destiny Pack", world.player, 3) or requires_level(world, state, 45),
            "Epic Destiny Box (8)":
                lambda state:
                    state.has("Progressive Epic Destiny Pack", world.player, 4) or requires_level(world, state, 55),
            "Legendary Destiny Pack (32)":
                lambda state:
                    state.has("Progressive Legendary Destiny Pack", world.player, 1) or requires_level(world, state, 50),
            "Legendary Destiny Pack (64)":
                lambda state:
                    state.has("Progressive Legendary Destiny Pack", world.player, 2) or requires_level(world, state, 65),
            "Legendary Destiny Box (4)":
                lambda state:
                    state.has("Progressive Legendary Destiny Pack", world.player, 3) or requires_level(world, state, 60),
            "Legendary Destiny Box (8)":
                lambda state:
                    state.has("Progressive Legendary Destiny Pack", world.player, 4) or requires_level(world, state, 70),
            "Fire Destiny Deck (18)":
                lambda state:
                    state.has("Fire Destiny Deck (18)", world.player) or requires_level(world, state, 33),
            "Earth Destiny Deck (18)":
                lambda state:
                    state.has("Earth Destiny Deck (18)", world.player) or requires_level(world, state, 45),
            "Water Destiny Deck (18)":
                lambda state:
                    state.has("Water Destiny Deck (18)", world.player) or requires_level(world, state, 39),
            "Wind Destiny Deck (18)":
                lambda state:
                    state.has("Wind Destiny Deck (18)", world.player) or requires_level(world, state, 50),
            "Cleanser (8)":
                lambda state:
                    state.has("Progressive Cleanser", world.player, 1) or requires_level(world, state, 2),
            "Cleanser (16)":
                lambda state:
                    state.has("Progressive Cleanser", world.player, 2) or requires_level(world, state, 9),
            "Card Sleeves (Clear)":
                lambda state:
                    state.has("Card Sleeves (Clear)", world.player) or requires_level(world, state, 2),
            "Card Sleeves (Tetramon)":
                lambda state:
                    state.has("Card Sleeves (Tetramon)", world.player) or requires_level(world, state, 10),
            "D20 Dice Red (16)":
                lambda state:
                    state.has("D20 Dice Red (16)", world.player) or requires_level(world, state, 3),
            "D20 Dice Blue (16)":
                lambda state:
                    state.has("D20 Dice Blue (16)", world.player) or requires_level(world, state, 3),
            "D20 Dice Black (16)":
                lambda state:
                    state.has("D20 Dice Black (16)", world.player) or requires_level(world, state, 4),
            "D20 Dice White (16)":
                lambda state:
                    state.has("D20 Dice White (16)", world.player) or requires_level(world, state, 4),
            "Card Sleeves (Fire)":
                lambda state:
                    state.has("Card Sleeves (Fire)", world.player) or requires_level(world, state, 10),
            "Card Sleeves (Earth)":
                lambda state:
                    state.has("Card Sleeves (Earth)", world.player) or requires_level(world, state, 20),
            "Card Sleeves (Water)":
                lambda state:
                    state.has("Card Sleeves (Water)", world.player) or requires_level(world, state, 25),
            "Card Sleeves (Wind)":
                lambda state:
                    state.has("Card Sleeves (Wind)", world.player) or requires_level(world, state, 30),
            "Deck Box Red (8)":
                lambda state:
                    state.has("Progressive Deck Box Red", world.player, 1) or requires_level(world, state, 5),
            "Deck Box Red (16)":
                lambda state:
                    state.has("Progressive Deck Box Red", world.player, 2) or requires_level(world, state, 8),
            "Deck Box Green (8)":
                lambda state:
                    state.has("Progressive Deck Box Green", world.player, 1) or requires_level(world, state, 5),
            "Deck Box Green (16)":
                lambda state:
                    state.has("Progressive Deck Box Green", world.player, 2) or requires_level(world, state, 8),
            "Deck Box Blue (8)":
                lambda state:
                    state.has("Progressive Deck Box Blue", world.player, 1) or requires_level(world, state, 6),
            "Deck Box Blue (16)":
                lambda state:
                    state.has("Progressive Deck Box Blue", world.player, 2) or requires_level(world, state, 8),
            "Deck Box Yellow (8)":
                lambda state:
                    state.has("Progressive Deck Box Yellow", world.player, 1) or requires_level(world, state, 6),
            "Deck Box Yellow (16)":
                lambda state:
                    state.has("Progressive Deck Box Yellow", world.player, 2) or requires_level(world, state, 8),
            "Collection Book (4)":
                lambda state:
                    state.has("Collection Book (4)", world.player) or requires_level(world, state, 11),
            "Premium Collection Book (4)":
                lambda state:
                    state.has("Premium Collection Book (4)", world.player) or requires_level(world, state, 50),
            "Playmat (Drilceros)":
                lambda state:
                    state.has("Playmat (Drilceros)", world.player) or requires_level(world, state, 7),
            "Playmat (Clamigo)":
                lambda state:
                    state.has("Playmat (Clamigo)", world.player) or requires_level(world, state, 13),
            "Playmat (Wispo)":
                lambda state:
                    state.has("Playmat (Wispo)", world.player) or requires_level(world, state, 16),
            "Playmat (Lunight)":
                lambda state:
                    state.has("Playmat (Lunight)", world.player) or requires_level(world, state, 16),
            "Playmat (Kyrone)":
                lambda state:
                    state.has("Playmat (Kyrone)", world.player) or requires_level(world, state, 19),
            "Playmat (Duel)":
                lambda state:
                    state.has("Playmat (Duel)", world.player) or requires_level(world, state, 21),
            "Playmat (Dracunix)":
                lambda state:
                    state.has("Playmat (Dracunix)", world.player) or requires_level(world, state, 26),
            "Playmat (The Four Dragons)":
                lambda state:
                    state.has("Playmat (The Four Dragons)", world.player) or requires_level(world, state, 35),
            "Playmat (Drakon)":
                lambda state:
                    state.has("Playmat (Drakon)", world.player) or requires_level(world, state, 36),
            "Playmat (GigatronX Evo)":
                lambda state:
                    state.has("Playmat (GigatronX Evo)", world.player) or requires_level(world, state, 38),
            "Playmat (Fire)":
                lambda state:
                    state.has("Playmat (Fire)", world.player) or requires_level(world, state, 43),
            "Playmat (Earth)":
                lambda state:
                    state.has("Playmat (Earth)", world.player) or requires_level(world, state, 47),
            "Playmat (Water)":
                lambda state:
                    state.has("Playmat (Water)", world.player) or requires_level(world, state, 52),
            "Playmat (Wind)":
                lambda state:
                    state.has("Playmat (Wind)", world.player) or requires_level(world, state, 55),
            "Playmat (Tetramon)":
                lambda state:
                    state.has("Playmat (Tetramon)", world.player) or requires_level(world, state, 60),
            "Pigni Plushie (12)":
                lambda state:
                    state.has("Pigni Plushie (12)", world.player) or requires_level(world, state, 6),
            "Nanomite Plushie (16)":
                lambda state:
                    state.has("Nanomite Plushie (16)", world.player)  or requires_level(world, state, 8),
            "Minstar Plushie (24)":
                lambda state:
                    state.has("Minstar Plushie (24)", world.player) or requires_level(world, state, 10),
            "Nocti Plushie (6)":
                lambda state:
                    state.has("Nocti Plushie (6)", world.player) or requires_level(world, state, 12),
            "Burpig Figurine (12)":
                lambda state:
                    state.has("Burpig Figurine (12)", world.player) or requires_level(world, state, 15),
            "Decimite Figurine (8)":
                lambda state:
                    state.has("Decimite Figurine (8)", world.player) or requires_level(world, state, 18),
            "Trickstar Figurine (12)":
                lambda state:
                    state.has("Trickstar Figurine (12)", world.player) or requires_level(world, state, 20),
            "Lunight Figurine (8)":
                lambda state:
                    state.has("Lunight Figurine (8)", world.player) or requires_level(world, state, 24),
            "Inferhog Figurine (2)":
                lambda state:
                    state.has("Inferhog Figurine (2)", world.player) or requires_level(world, state, 30),
            "Meganite Figurine (2)":
                lambda state:
                    state.has("Meganite Figurine (2)", world.player) or requires_level(world, state, 34),
            "Princestar Figurine (2)":
                lambda state:
                    state.has("Princestar Figurine (2)", world.player) or requires_level(world, state, 42),
            "Vampicant Figurine (2)":
                lambda state:
                    state.has("Vampicant Figurine (2)", world.player) or requires_level(world, state, 50),
            "Blazoar Plushie (2)":
                lambda state:
                    state.has("Blazoar Plushie (2)", world.player) or requires_level(world, state, 55),
            "Giganite Statue (2)":
                lambda state:
                    state.has("Giganite Statue (2)", world.player) or requires_level(world, state, 70),
            "Kingstar Plushie (2)":
                lambda state:
                    state.has("Kingstar Plushie (2)", world.player) or requires_level(world, state, 65),
            "Dracunix Figurine (1)":
                lambda state:
                    state.has("Dracunix Figurine (1)", world.player) or requires_level(world, state, 75),
            "Bonfiox Plushie (8)":
                lambda state:
                    state.has("Bonfiox Plushie (8)", world.player) or requires_level(world, state, 28),
            "Drilceros Action Figure (4)":
                lambda state:
                    state.has("Drilceros Action Figure (4)", world.player) or requires_level(world, state, 80),
            "ToonZ Plushie (6)":
                lambda state:
                    state.has("ToonZ Plushie (6)", world.player) or requires_level(world, state, 12),
            "Small Cabinet":
                lambda state:
                    state.has("Small Cabinet", world.player) or requires_level(world, state, 2),
            "Small Metal Rack":
                lambda state:
                    state.has("Small Metal Rack", world.player) or requires_level(world, state, 2),
            "Single Sided Shelf":
                lambda state:
                    state.has("Single Sided Shelf", world.player) or requires_level(world, state, 3),
            "Double Sided Shelf":
                lambda state:
                    state.has("Double Sided Shelf", world.player) or requires_level(world, state, 11),
            "Wide Shelf":
                lambda state:
                    state.has("Wide Shelf", world.player) or requires_level(world, state, 30),
            "Card Table":
                lambda state:
                    state.has("Progressive Card Table", world.player, 1) or requires_level(world, state, 3),
            "Small Card Display":
                lambda state:
                    state.has("Progressive Card Display", world.player, 1) or requires_level(world, state, 8),
            "Card Display Table":
                lambda state:
                    state.has("Progressive Card Display", world.player, 2) or requires_level(world, state, 20),
            "Vintage Card Table":
                lambda state:
                    state.has("Progressive Card Table", world.player, 2) or requires_level(world, state, 25),
            "Big Card Display":
                lambda state:
                    state.has("Progressive Card Display", world.player, 3) or requires_level(world, state, 50),
            "Small Personal Shelf":
                lambda state:
                    state.has("Progressive Personal Shelf", world.player, 1) or requires_level(world, state, 3),
            "Big Personal Shelf":
                lambda state:
                    state.has("Progressive Personal Shelf", world.player, 2) or requires_level(world, state, 23),
            "Huge Personal Shelf":
                lambda state:
                    state.has("Progressive Personal Shelf", world.player, 3) or requires_level(world, state, 35),
            "Auto Scent M100":
                lambda state:
                    state.has("Progressive Auto Scent", world.player, 1) or requires_level(world, state, 5),
            "Auto Scent G500":
                lambda state:
                    state.has("Progressive Auto Scent", world.player, 2) or requires_level(world, state, 18),
            "Auto Scent T100":
                lambda state:
                    state.has("Progressive Auto Scent", world.player, 3) or requires_level(world, state, 40),
            "Small Warehouse Shelf":
                lambda state:
                    state.has("Small Warehouse Shelf", world.player) or requires_level(world, state, 5),
            "Big Warehouse Shelf":
                lambda state:
                    state.has("Big Warehouse Shelf", world.player) or requires_level(world, state, 13),
            "Play Table":
                lambda state:
                    state.has("Play Table", world.player) or requires_level(world, state, 3),
            "Workbench":
                lambda state:
                    state.has("Workbench", world.player) or requires_level(world, state, 10),
            "Trash Bin":
                lambda state:
                    state.has("Trash Bin", world.player) or requires_level(world, state, 10),
            "Checkout Counter":
                lambda state:
                    state.has("Checkout Counter", world.player) or requires_level(world, state, 15),
            "System Gate #1":
                lambda state:
                    state.has("System Gate #1", world.player) or requires_level(world, state, 5),
            "System Gate #2":
                lambda state:
                    state.has("System Gate #2", world.player) or requires_level(world, state, 7),
            "Mafia Works":
                lambda state:
                    state.has("Mafia Works", world.player) or requires_level(world, state, 11),
            "Necromonsters":
                lambda state:
                    state.has("Necromonsters", world.player) or requires_level(world, state, 17),
            "Claim!":
                lambda state:
                    state.has("Claim!", world.player) or requires_level(world, state, 24),
            "Penny Sleeves":
                lambda state:
                    state.has("Penny Sleeves", world.player) or requires_level(world, state, 10),
            "Tower Deckbox":
                lambda state:
                    state.has("Tower Deckbox", world.player) or requires_level(world, state, 14),
            "Magnetic Holder":
                lambda state:
                    state.has("Magnetic Holder", world.player) or requires_level(world, state, 19),
            "Toploader":
                lambda state:
                    state.has("Toploader", world.player) or requires_level(world, state, 23),
            "Card Preserver":
                lambda state:
                    state.has("Card Preserver", world.player) or requires_level(world, state, 28),
            "Playmat Gray":
                lambda state:
                    state.has("Playmat Gray", world.player) or requires_level(world, state, 31),
            "Playmat Green":
                lambda state:
                    state.has("Playmat Green", world.player) or requires_level(world, state, 32),
            "Playmat Purple":
                lambda state:
                    state.has("Playmat Purple", world.player) or requires_level(world, state, 33),
            "Playmat Yellow":
                lambda state:
                    state.has("Pocket Pages", world.player) or requires_level(world, state, 34),
            "Pocket Pages":
                lambda state:
                state.has("Pocket Pages", world.player) or requires_level(world, state, 39),
            "Card Holder":
                lambda state:
                    state.has("Card Holder", world.player) or requires_level(world, state, 44),
            "Collectors Album":
                lambda state:
                    state.has("Collectors Album", world.player) or requires_level(world, state, 49),
        }
    }
    return rules


def set_rules(world):
    # Set access rules for levels
    card_types = ["Basic Card", "Rare Card", "Epic Card", "Legendary Card", "Basic Destiny", "Rare Destiny",
                  "Epic Destiny"]
    # AP cant handle for looping this. I hate this
    world.get_location(f"Level {5}").access_rule = lambda state: state.has(f"Progressive {card_types[0]} Pack",world.player,1)
    world.get_location(f"Level {10}").access_rule = lambda state: state.can_reach_location(f"Level {5}", world.player) and state.has("Progressive Shop Expansion A", world.player, 1)
    world.get_location(f"Level {15}").access_rule = lambda state: state.can_reach_location(f"Level {10}", world.player) and state.has(f"Progressive {card_types[1]} Pack",world.player,1)
    world.get_location(f"Level {20}").access_rule = lambda state: state.can_reach_location(f"Level {15}", world.player)and state.has("Progressive Shop Expansion A", world.player, 2)
    world.get_location(f"Level {25}").access_rule = lambda state: state.can_reach_location(f"Level {20}", world.player) and state.has(f"Progressive {card_types[1]} Pack",world.player,2)
    world.get_location(f"Level {30}").access_rule = lambda state: state.can_reach_location(f"Level {25}", world.player)and state.has("Progressive Shop Expansion A", world.player, 3)
    world.get_location(f"Level {35}").access_rule = lambda state: state.can_reach_location(f"Level {30}", world.player)and state.has(f"Progressive {card_types[2]} Pack",world.player,1)
    world.get_location(f"Level {40}").access_rule = lambda state: state.can_reach_location(f"Level {35}", world.player)and state.has("Progressive Shop Expansion A", world.player, 4)
    world.get_location(f"Level {45}").access_rule = lambda state: state.can_reach_location(f"Level {40}", world.player)and state.has(f"Progressive {card_types[2]} Pack",world.player,2)
    world.get_location(f"Level {50}").access_rule = lambda state: state.can_reach_location(f"Level {45}", world.player)and state.has("Progressive Shop Expansion A", world.player, 5)
    world.get_location(f"Level {55}").access_rule = lambda state: state.can_reach_location(f"Level {50}", world.player)and state.has(f"Progressive {card_types[3]} Pack",world.player,1)
    world.get_location(f"Level {60}").access_rule = lambda state: state.can_reach_location(f"Level {55}", world.player)and state.has("Progressive Shop Expansion A", world.player, 6)
    world.get_location(f"Level {65}").access_rule = lambda state: state.can_reach_location(f"Level {60}", world.player)and state.has(f"Progressive {card_types[3]} Pack",world.player,2)
    world.get_location(f"Level {70}").access_rule = lambda state: state.can_reach_location(f"Level {65}", world.player)and state.has("Progressive Shop Expansion A", world.player, 7)
    world.get_location(f"Level {75}").access_rule = lambda state: state.can_reach_location(f"Level {70}", world.player)and state.has(f"Progressive {card_types[4]} Pack",world.player,1)
    world.get_location(f"Level {80}").access_rule = lambda state: state.can_reach_location(f"Level {75}", world.player)and state.has("Progressive Shop Expansion A", world.player, 8)
    world.get_location(f"Level {85}").access_rule = lambda state: state.can_reach_location(f"Level {80}", world.player)and state.has(f"Progressive {card_types[4]} Pack",world.player,2)
    world.get_location(f"Level {90}").access_rule = lambda state: state.can_reach_location(f"Level {85}", world.player)and state.has("Progressive Shop Expansion A", world.player, 9)
    world.get_location(f"Level {95}").access_rule = lambda state: state.can_reach_location(f"Level {90}", world.player)and state.has(f"Progressive {card_types[5]} Pack",world.player,1)
    world.get_location(f"Level {100}").access_rule = lambda state: state.can_reach_location(f"Level {95}", world.player)and state.has("Progressive Shop Expansion A", world.player, 10)
    world.get_location(f"Level {105}").access_rule = lambda state: state.can_reach_location(f"Level {100}", world.player)and state.has(f"Progressive {card_types[5]} Pack",world.player,2)
    world.get_location(f"Level {110}").access_rule = lambda state: state.can_reach_location(f"Level {105}", world.player)and state.has("Progressive Shop Expansion A", world.player, 11)
    world.get_location(f"Level {115}").access_rule = lambda state: state.can_reach_location(f"Level {110}", world.player)and state.has(f"Progressive {card_types[6]} Pack",world.player,1)

    for j in range(1,23):
        for i in range(1,5):
            closest_multiple_of_5 = (-1+i+j*5) // 5 * 5
            world.get_location(f"Level {i+j*5}").access_rule = lambda state: state.can_reach_location(f"Level {closest_multiple_of_5}", world.player)

    for i in range(51,116):
        world.get_location(f"Level {i}").progress_type = LocationProgressType.EXCLUDED

    rules_lookup = get_rules(world)
    for location_name, rule in rules_lookup["locations"].items():
        try:
            world.get_location(location_name).access_rule = rule
        except KeyError:
            pass


    if world.options.card_sanity.value > 0:
        for location_name, item_name in rarity_item_dict.items():
            world.multiworld.get_location(location_name, world.player).access_rule = lambda state: state.has(item_name, world.player)

    if world.options.goal.value == 0:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Progressive Shop Expansion A", world.player, world.options.shop_expansion_goal.value)
    if world.options.goal.value == 1:
        world.multiworld.completion_condition[world.player] = lambda state: state.can_reach_location(f"Level {world.options.level_goal.value}", world.player),
    if world.options.goal.value == 2:
        world.multiworld.completion_condition[world.player] = lambda state: has_all_ghosts(world, state)