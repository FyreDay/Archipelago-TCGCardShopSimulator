from typing import Optional, NamedTuple, Dict

from BaseClasses import Item, ItemClassification


class TCGSimulatorItem(Item):
    game: str = "TCG Card Shop Simulator"


class ItemData(NamedTuple):
    code: int
    classification: ItemClassification
    amount: Optional[int] = 1


def create_item(world, name: str, classification: ItemClassification, amount: Optional[int] = 1):
    for i in range(amount):
        world.itempool.append(Item(name, classification, world.item_name_to_id[name], world.player))


def create_items(world):
    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))

    ghost_val = 80 if world.options.ghost_goal_amount.value > 75 else world.options.ghost_goal_amount.value + 5
    if world.options.goal.value == 2:
        progressive_dict["Progressive Ghost Card"].amount = ghost_val

    for item_name, item_data in item_dict:
        create_item(world, item_name, item_data.classification, item_data.amount)

    for item_name, item_data in progressive_dict:
        create_item(world, item_name, item_data.classification, item_data.amount)

    remaining_locations: int = total_location_count - len(world.itempool)
    print(f"Remaining items here: {remaining_locations}")
    trap_count = round(remaining_locations * world.options.trap_fill.value / 100)
    junk_count = remaining_locations - trap_count

    trap_weights = {
        "Stink Trap": world.options.stink_trap,
        "Poltergeist Trap": world.options.poltergeist_trap
    }

    junk_weights["Small Xp"] = world.options.xp_boosts * 0.5
    junk_weights["Medium Xp"] = world.options.xp_boosts * 0.3
    junk_weights["Large Xp"] = world.options.xp_boosts * 0.2
    junk_weights["Small Money"] = world.options.money_bags * 0.5
    junk_weights["Medium Money"] = world.options.money_bags * 0.3
    junk_weights["Large Money"] = world.options.money_bags * 0.2
    junk_weights["Random Card"] = world.options.random_card
    junk_weights["Random New Card"] = world.options.random_new_card

    junk = get_junk_item_names(world.multiworld.random, junk_count)
    for name in junk:
        create_item(world, name, ItemClassification.filler)

    trap = get_trap_item_names(world.multiworld.random, trap_count, trap_weights)
    for name in trap:
        create_item(world, name, ItemClassification.trap)

    world.multiworld.itempool += world.itempool


def get_junk_item_names(rand, k: int) -> str:
    junk = rand.choices(
        list(junk_weights.keys()),
        weights=list(junk_weights.values()),
        k=k)
    return junk


def get_trap_item_names(rand, k: int, trap_weights) -> str:
    trap = rand.choices(
        list(trap_weights.keys()),
        weights=list(trap_weights.values()),
        k=k)
    return trap


start_id = 0x1F280000


item_dict: Dict[str, ItemData] = {
    "Fire Battle Deck": ItemData(0x5, ItemClassification.useful),
    "Earth Battle Deck": ItemData(0x6, ItemClassification.useful),
    "Water Battle Deck": ItemData(0x7, ItemClassification.useful),
    "Wind Battle Deck": ItemData(0x8, ItemClassification.useful),
    "Fire Destiny Deck": ItemData(0xD, ItemClassification.useful),
    "Earth Destiny Deck": ItemData(0xE, ItemClassification.useful),
    "Water Destiny Deck": ItemData(0xF, ItemClassification.useful),
    "Wind Destiny Deck": ItemData(0x0, ItemClassification.useful),
    "Card Sleeves (Clear)": ItemData(0x12, ItemClassification.useful),
    "Card Sleeves (Tetramon)": ItemData(0x13, ItemClassification.useful),
    "D20 Dice Red": ItemData(0x14, ItemClassification.useful),
    "D20 Dice Blue": ItemData(0x15, ItemClassification.useful),
    "D20 Dice Black": ItemData(0x16, ItemClassification.useful),
    "D20 Dice White": ItemData(0x17, ItemClassification.useful),
    "Card Sleeves (Fire)": ItemData(0x18, ItemClassification.useful),
    "Card Sleeves (Earth)": ItemData(0x19, ItemClassification.useful),
    "Card Sleeves (Water)": ItemData(0x1A, ItemClassification.useful),
    "Card Sleeves (Wind)": ItemData(0x1B, ItemClassification.useful),
    "Collection Book": ItemData(0x20, ItemClassification.useful),
    "Premium Collection Book": ItemData(0x21, ItemClassification.useful),
    "Playmat (Drilceros)": ItemData(0x22, ItemClassification.useful),
    "Playmat (Clamigo)": ItemData(0x23, ItemClassification.useful),
    "Playmat (Wispo)": ItemData(0x24, ItemClassification.useful),
    "Playmat (Lunight)": ItemData(0x25, ItemClassification.useful),
    "Playmat (Kyrone)": ItemData(0x26, ItemClassification.useful),
    "Playmat (Duel)": ItemData(0x27, ItemClassification.useful),
    "Playmat (Dracunix1)": ItemData(0x28, ItemClassification.useful),
    "Playmat (The Four Dragons)": ItemData(0x29, ItemClassification.useful),
    "Playmat (Drakon)": ItemData(0x2A, ItemClassification.useful),
    "Playmat (GigatronX Evo)": ItemData(0x2B, ItemClassification.useful),
    "Playmat (Fire)": ItemData(0x2C, ItemClassification.useful),
    "Playmat (Earth)": ItemData(0x2D, ItemClassification.useful),
    "Playmat (Water)": ItemData(0x2E, ItemClassification.useful),
    "Playmat (Wind)": ItemData(0x2F, ItemClassification.useful),
    "Playmat (Tetramon)": ItemData(0x30, ItemClassification.useful),
    "Pigni Plushie": ItemData(0x31, ItemClassification.useful),
    "Nanomite Plushie": ItemData(0x32, ItemClassification.useful),
    "Minstar Plushie": ItemData(0x33, ItemClassification.useful),
    "Nocti Plushie": ItemData(0x34, ItemClassification.useful),
    "Burpig Figurine": ItemData(0x35, ItemClassification.useful),
    "Decimite Figurine": ItemData(0x36, ItemClassification.useful),
    "Trickstar Figurine": ItemData(0x37, ItemClassification.useful),
    "Lunight Figurine": ItemData(0x38, ItemClassification.useful),
    "Inferhog Figurine": ItemData(0x39, ItemClassification.useful),
    "Meganite Figurine": ItemData(0x3A, ItemClassification.useful),
    "Princestar Figurine": ItemData(0x3B, ItemClassification.useful),
    "Vampicant Figurine": ItemData(0x3C, ItemClassification.useful),
    "Blazoar Plushie": ItemData(0x3D, ItemClassification.useful),
    "Giganite Statue": ItemData(0x3E, ItemClassification.useful),
    "Kingstar Plushie": ItemData(0x3F, ItemClassification.useful),
    "Dracunix Figurine": ItemData(0x40, ItemClassification.useful),
    "Bonfiox Plushie": ItemData(0x41, ItemClassification.useful),
    "Drilceros Action Figure": ItemData(0x42, ItemClassification.useful),
    "ToonZ Plushie": ItemData(0x43, ItemClassification.useful),
    "Small Cabinet": ItemData(0x44, ItemClassification.useful),
    "Small Metal Rack": ItemData(0x45, ItemClassification.useful),
    "Single Sided Shelf": ItemData(0x46, ItemClassification.useful),
    "Double Sided Shelf": ItemData(0x47, ItemClassification.useful),
    "Wide Shelf": ItemData(0x48, ItemClassification.useful),
    "Play Table": ItemData(0x4E, ItemClassification.useful),
    "Workbench": ItemData(0x4F, ItemClassification.useful),
    "Trash Bin": ItemData(0x50, ItemClassification.useful),
    "Checkout Counter": ItemData(0x51, ItemClassification.useful),
    "System Gate #1": ItemData(0x52, ItemClassification.useful),
    "System Gate #2": ItemData(0x53, ItemClassification.useful),
    "Mafia Works": ItemData(0x54, ItemClassification.useful),
    "Necromonsters": ItemData(0x55, ItemClassification.useful),
    "Claim!": ItemData(0x56, ItemClassification.useful),
    "Penny Sleeves": ItemData(0x57, ItemClassification.useful),
    "Tower Deckbox": ItemData(0x58, ItemClassification.useful),
    "Magnetic Holder": ItemData(0x59, ItemClassification.useful),
    "Toploader": ItemData(0x5A, ItemClassification.useful),
    "Card Preserver": ItemData(0x5B, ItemClassification.useful),
    "Playmat Gray": ItemData(0x5C, ItemClassification.useful),
    "Playmat Green": ItemData(0x5D, ItemClassification.useful),
    "Playmat Purple": ItemData(0x5E, ItemClassification.useful),
    "Playmat Yellow": ItemData(0x5F, ItemClassification.useful),
    "Pocket Pages": ItemData(0x60, ItemClassification.useful),
    "Card Holder": ItemData(0x61, ItemClassification.useful),
    "Collectors Album": ItemData(0xB5, ItemClassification.useful),
    "Worker - Zachery": ItemData(0xB6, ItemClassification.useful),
    "Worker - Terence": ItemData(0xB7, ItemClassification.useful),
    "Worker - Dennis": ItemData(0xB8, ItemClassification.useful),
    "Worker - Clark": ItemData(0xB9, ItemClassification.useful),
    "Worker - Angus": ItemData(0xBA, ItemClassification.useful),
    "Worker - Benji": ItemData(0xBB, ItemClassification.useful),
    "Worker - Lauren": ItemData(0xBC, ItemClassification.useful),
    "Worker - Axel": ItemData(0xBD, ItemClassification.useful),
    "Playmat (Dracunix2)": ItemData(0xBE, ItemClassification.useful),
    "Playmat (GigatronX)": ItemData(0xBF, ItemClassification.useful),
    "Playmat (Katengu Black)": ItemData(0xC2, ItemClassification.useful),
    "Playmat (Katengu White)": ItemData(0xC3, ItemClassification.useful),
    "Manga 1": ItemData(0xC4, ItemClassification.useful),
    "Manga 2": ItemData(0xC5, ItemClassification.useful),
    "Manga 3": ItemData(0xC6, ItemClassification.useful),
    "Manga 4": ItemData(0xC7, ItemClassification.useful),
    "Manga 5": ItemData(0xC8, ItemClassification.useful),
    "Manga 6": ItemData(0xC9, ItemClassification.useful),
    "Manga 7": ItemData(0xCA, ItemClassification.useful),
    "Manga 8": ItemData(0xCB, ItemClassification.useful),
    "Manga 9": ItemData(0xCC, ItemClassification.useful),
    "Manga 10": ItemData(0xCD, ItemClassification.useful),
    "Manga 11": ItemData(0xCE, ItemClassification.useful),
    "Manga 12": ItemData(0xCF, ItemClassification.useful),
    "Warehouse Unlock": ItemData(0xD8, ItemClassification.progression),
    "Basic Card Pack (32)": ItemData(0x01, ItemClassification.progression),
    "Basic Card Pack (64)": ItemData(0xD8, ItemClassification.progression),
    "Basic Card Box (4)": ItemData(0xD9, ItemClassification.progression),
    "Basic Card Box (8)": ItemData(0xDA, ItemClassification.progression),
    "Rare Card Pack (32)": ItemData(0x02, ItemClassification.progression),
    "Rare Card Pack (64)": ItemData(0xDB, ItemClassification.progression),
    "Rare Card Box (4)": ItemData(0xDC, ItemClassification.progression),
    "Rare Card Box (8)": ItemData(0xDD, ItemClassification.progression),
    "Epic Card Pack (32)": ItemData(0x03, ItemClassification.progression),
    "Epic Card Pack (64)": ItemData(0xDE, ItemClassification.progression),
    "Epic Card Box (4)": ItemData(0xDF, ItemClassification.progression),
    "Epic Card Box (8)": ItemData(0xE0, ItemClassification.progression),
    "Legendary Card Pack (32)": ItemData(0x04, ItemClassification.progression),
    "Legendary Card Pack (64)": ItemData(0xE1, ItemClassification.progression),
    "Legendary Card Box (4)": ItemData(0xE2, ItemClassification.progression),
    "Legendary Card Box (8)": ItemData(0xE3, ItemClassification.progression),
    "Basic Destiny Pack (32)": ItemData(0x09, ItemClassification.progression),
    "Basic Destiny Pack (64)": ItemData(0xE4, ItemClassification.progression),
    "Basic Destiny Box (4)": ItemData(0xE5, ItemClassification.progression),
    "Basic Destiny Box (8)": ItemData(0xE6, ItemClassification.progression),
    "Rare Destiny Pack (32)": ItemData(0x0A, ItemClassification.progression),
    "Rare Destiny Pack (64)": ItemData(0xE7, ItemClassification.progression),
    "Rare Destiny Box (4)": ItemData(0xE8, ItemClassification.progression),
    "Rare Destiny Box (8)": ItemData(0xE9, ItemClassification.progression),
    "Epic Destiny Pack (32)": ItemData(0x0B, ItemClassification.useful),
    "Epic Destiny Pack (64)": ItemData(0xEA, ItemClassification.useful),
    "Epic Destiny Box (4)": ItemData(0xEB, ItemClassification.useful),
    "Epic Destiny Box (8)": ItemData(0xEC, ItemClassification.useful),
    "Legendary Destiny Pack (32)": ItemData(0x0C, ItemClassification.useful),
    "Legendary Destiny Pack (64)": ItemData(0xED, ItemClassification.useful),
    "Legendary Destiny Box (4)": ItemData(0xEE, ItemClassification.useful),
    "Legendary Destiny Box (8)": ItemData(0xEF, ItemClassification.useful),
    "Cleanser (8)": ItemData(0x11, ItemClassification.useful),
    "Cleanser (64)": ItemData(0xF0, ItemClassification.useful),
    "Deck Box Red (8)": ItemData(0x1C, ItemClassification.useful),
    "Deck Box Red (16)": ItemData(0xF1, ItemClassification.useful),
    "Deck Box Green (8)": ItemData(0x1D, ItemClassification.useful),
    "Deck Box Green (16)": ItemData(0xF2, ItemClassification.useful),
    "Deck Box Blue (8)": ItemData(0x1E, ItemClassification.useful),
    "Deck Box Blue (16)": ItemData(0xF3, ItemClassification.useful),
    "Deck Box Yellow (8)": ItemData(0x1F, ItemClassification.useful),
    "Deck Box Yellow (16)": ItemData(0xF4, ItemClassification.useful),
}

progressive_dict: Dict[str, ItemData] = {
    "Progressive Card Table": ItemData(0x49, ItemClassification.useful, 2),
    "Progressive Card Display": ItemData(0x4A, ItemClassification.useful, 3),
    "Progressive Personal Shelf": ItemData(0x4B, ItemClassification.useful, 3),
    "Progressive Auto Scent": ItemData(0x4C, ItemClassification.useful, 3),
    "Progressive Warehouse Shelf": ItemData(0x4D, ItemClassification.useful, 2),
    "Progressive Shop Expansion A": ItemData(0xC0, ItemClassification.progression, 30),
    "Progressive Shop Expansion B": ItemData(0xC1, ItemClassification.useful, 14),
    "Progressive Ghost Card": ItemData(0xD7, ItemClassification.progression_skip_balancing, 0)
}

ghost_dict: Dict[str, ItemData] = {
    "Ghost Blazoar (white)": ItemData(0x62, ItemClassification.progression_skip_balancing),
    "Ghost Blazoar (Black)": ItemData(0x63, ItemClassification.progression_skip_balancing),
    "Foil Ghost Blazoar (white)": ItemData(0x64, ItemClassification.progression_skip_balancing),
    "Foil Ghost Blazoar (Black)": ItemData(0x65, ItemClassification.progression_skip_balancing),
    "Ghost Kyuenbi (white)": ItemData(0x66, ItemClassification.progression_skip_balancing),
    "Ghost Kyuenbi (Black)": ItemData(0x67, ItemClassification.progression_skip_balancing),
    "Foil Ghost Kyuenbi (white)": ItemData(0x68, ItemClassification.progression_skip_balancing),
    "Foil Ghost Kyuenbi (Black)": ItemData(0x69, ItemClassification.progression_skip_balancing),
    "Ghost Giganite (white)": ItemData(0x6A, ItemClassification.progression_skip_balancing),
    "Ghost Giganite (Black)": ItemData(0x6B, ItemClassification.progression_skip_balancing),
    "Foil Ghost Giganite (white)": ItemData(0x6C, ItemClassification.progression_skip_balancing),
    "Foil Ghost Giganite (Black)": ItemData(0x6D, ItemClassification.progression_skip_balancing),
    "Ghost Mammotree (white)": ItemData(0x6E, ItemClassification.progression_skip_balancing),
    "Ghost Mammotree (Black)": ItemData(0x6F, ItemClassification.progression_skip_balancing),
    "Foil Ghost Mammotree (white)": ItemData(0x70, ItemClassification.progression_skip_balancing),
    "Foil Ghost Mammotree (Black)": ItemData(0x71, ItemClassification.progression_skip_balancing),
    "Ghost Kingstar (white)": ItemData(0x72, ItemClassification.progression_skip_balancing),
    "Ghost Kingstar (Black)": ItemData(0x73, ItemClassification.progression_skip_balancing),
    "Foil Ghost Kingstar (white)": ItemData(0x74, ItemClassification.progression_skip_balancing),
    "Foil Ghost Kingstar (Black)": ItemData(0x75, ItemClassification.progression_skip_balancing),
    "Ghost Fistronk (white)": ItemData(0x76, ItemClassification.progression_skip_balancing),
    "Ghost Fistronk (Black)": ItemData(0x77, ItemClassification.progression_skip_balancing),
    "Foil Ghost Fistronk (white)": ItemData(0x78, ItemClassification.progression_skip_balancing),
    "Foil Ghost Fistronk (Black)": ItemData(0x79, ItemClassification.progression_skip_balancing),
    "Ghost Royalama (white)": ItemData(0x7A, ItemClassification.progression_skip_balancing),
    "Ghost Royalama (Black)": ItemData(0x7B, ItemClassification.progression_skip_balancing),
    "Foil Ghost Royalama (white)": ItemData(0x7C, ItemClassification.progression_skip_balancing),
    "Foil Ghost Royalama (Black)": ItemData(0x7D, ItemClassification.progression_skip_balancing),
    "Ghost Dracunix (white)": ItemData(0x7E, ItemClassification.progression_skip_balancing),
    "Ghost Dracunix (Black)": ItemData(0x7F, ItemClassification.progression_skip_balancing),
    "Foil Ghost Dracunix (white)": ItemData(0x80, ItemClassification.progression_skip_balancing),
    "Foil Ghost Dracunix (Black)": ItemData(0x81, ItemClassification.progression_skip_balancing),
    "Ghost Magnoria (white)": ItemData(0x82, ItemClassification.progression_skip_balancing),
    "Ghost Magnoria (Black)": ItemData(0x83, ItemClassification.progression_skip_balancing),
    "Foil Ghost Magnoria (white)": ItemData(0x84, ItemClassification.progression_skip_balancing),
    "Foil Ghost Magnoria (Black)": ItemData(0x85, ItemClassification.progression_skip_balancing),
    "Ghost Hydroid (white)": ItemData(0x86, ItemClassification.progression_skip_balancing),
    "Ghost Hydroid (Black)": ItemData(0x87, ItemClassification.progression_skip_balancing),
    "Foil Ghost Hydroid (white)": ItemData(0x88, ItemClassification.progression_skip_balancing),
    "Foil Ghost Hydroid (Black)": ItemData(0x89, ItemClassification.progression_skip_balancing),
    "Ghost Drakon (white)": ItemData(0x8A, ItemClassification.progression_skip_balancing),
    "Ghost Drakon (Black)": ItemData(0x8B, ItemClassification.progression_skip_balancing),
    "Foil Ghost Drakon (white)": ItemData(0x8C, ItemClassification.progression_skip_balancing),
    "Foil Ghost Drakon (Black)": ItemData(0x8D, ItemClassification.progression_skip_balancing),
    "Ghost Bogon (white)": ItemData(0x8E, ItemClassification.progression_skip_balancing),
    "Ghost Bogon (Black)": ItemData(0x8F, ItemClassification.progression_skip_balancing),
    "Foil Ghost Bogon (white)": ItemData(0x90, ItemClassification.progression_skip_balancing),
    "Foil Ghost Bogon (Black)": ItemData(0x91, ItemClassification.progression_skip_balancing),
    "Ghost Hydron (white)": ItemData(0x92, ItemClassification.progression_skip_balancing),
    "Ghost Hydron (Black)": ItemData(0x93, ItemClassification.progression_skip_balancing),
    "Foil Ghost Hydron (white)": ItemData(0x94, ItemClassification.progression_skip_balancing),
    "Foil Ghost Hydron (Black)": ItemData(0x95, ItemClassification.progression_skip_balancing),
    "Ghost Raizon (white)": ItemData(0x96, ItemClassification.progression_skip_balancing),
    "Ghost Raizon (Black)": ItemData(0x97, ItemClassification.progression_skip_balancing),
    "Foil Ghost Raizon (white)": ItemData(0x98, ItemClassification.progression_skip_balancing),
    "Foil Ghost Raizon (Black)": ItemData(0x99, ItemClassification.progression_skip_balancing),
    "Ghost Lucadence (white)": ItemData(0x9A, ItemClassification.progression_skip_balancing),
    "Ghost Lucadence (Black)": ItemData(0x9B, ItemClassification.progression_skip_balancing),
    "Foil Ghost Lucadence (white)": ItemData(0x9C, ItemClassification.progression_skip_balancing),
    "Foil Ghost Lucadence (Black)": ItemData(0x9D, ItemClassification.progression_skip_balancing),
    "Ghost Jigajawr (white)": ItemData(0x9E, ItemClassification.progression_skip_balancing),
    "Ghost Jigajawr (Black)": ItemData(0x9F, ItemClassification.progression_skip_balancing),
    "Foil Ghost Jigajawr (white)": ItemData(0xA0, ItemClassification.progression_skip_balancing),
    "Foil Ghost Jigajawr (Black)": ItemData(0xA1, ItemClassification.progression_skip_balancing),
    "Ghost Jacktern (white)": ItemData(0xA2, ItemClassification.progression_skip_balancing),
    "Ghost Jacktern (Black)": ItemData(0xA3, ItemClassification.progression_skip_balancing),
    "Foil Ghost Jacktern (white)": ItemData(0xA4, ItemClassification.progression_skip_balancing),
    "Foil Ghost Jacktern (Black)": ItemData(0xA5, ItemClassification.progression_skip_balancing),
    "Ghost GigatronX (white)": ItemData(0xA6, ItemClassification.progression_skip_balancing),
    "Ghost GigatronX (Black)": ItemData(0xA7, ItemClassification.progression_skip_balancing),
    "Foil Ghost GigatronX (white)": ItemData(0xA8, ItemClassification.progression_skip_balancing),
    "Foil Ghost GigatronX (Black)": ItemData(0xA9, ItemClassification.progression_skip_balancing),
    "Ghost Clawcifear (white)": ItemData(0xAA, ItemClassification.progression_skip_balancing),
    "Ghost Clawcifear (Black)": ItemData(0xAB, ItemClassification.progression_skip_balancing),
    "Foil Ghost Clawcifear (white)": ItemData(0xAC, ItemClassification.progression_skip_balancing),
    "Foil Ghost Clawcifear (Black)": ItemData(0xAD, ItemClassification.progression_skip_balancing),
    "Ghost Katengu (white)": ItemData(0xAE, ItemClassification.progression_skip_balancing),
    "Ghost Katengu (Black)": ItemData(0xAF, ItemClassification.progression_skip_balancing),
    "Foil Ghost Katengu (white)": ItemData(0xB0, ItemClassification.progression_skip_balancing),
    "Foil Ghost Katengu (Black)": ItemData(0xB1, ItemClassification.progression_skip_balancing),
}

junk_dict: Dict[str, ItemData] = {
    "Small Xp": ItemData(0xB2, ItemClassification.filler),
    "Small Money": ItemData(0xB3, ItemClassification.filler),
    "Medium Xp": ItemData(0xD0, ItemClassification.filler),
    "Medium Money": ItemData(0xD1, ItemClassification.filler),
    "Large Xp": ItemData(0xD2, ItemClassification.filler),
    "Large Money": ItemData(0xD3, ItemClassification.filler),
    "Random Card": ItemData(0xD4, ItemClassification.filler),
    "Random New Card": ItemData(0xD5, ItemClassification.filler),
}

trap_dict: Dict[str, ItemData] = {
    "Stink Trap": ItemData(0xB4, ItemClassification.trap),
    "Poltergeist Trap": ItemData(0xD6, ItemClassification.trap),
}

junk_weights = {
    "Small Xp": 25,
    "Small Money": 25,
    "Medium Money": 15,
    "Medium Xp": 15,
    "Large Money": 10,
    "Large Xp": 10,
    "Random Card": 50,
    "Random New Card": 50
}

full_item_dict: Dict[str, ItemData] = {**item_dict, **progressive_dict, **junk_dict, **trap_dict, **ghost_dict}
