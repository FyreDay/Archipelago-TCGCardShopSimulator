from dataclasses import dataclass
from typing import Optional, NamedTuple, Dict

from BaseClasses import Item, ItemClassification


class TCGSimulatorItem(Item):
    game: str = "TCG Card Shop Simulator"

@dataclass
class ItemData:
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

    for item_name, item_data in item_dict.items():
        create_item(world, item_name, item_data.classification, item_data.amount)

    for item_name, item_data in progressive_dict.items():
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
    "Fire Battle Deck": ItemData(0x1F280005, ItemClassification.useful),
    "Earth Battle Deck": ItemData(0x1F280006, ItemClassification.useful),
    "Water Battle Deck": ItemData(0x1F280007, ItemClassification.useful),
    "Wind Battle Deck": ItemData(0x1F280008, ItemClassification.useful),
    "Fire Destiny Deck": ItemData(0x1F28000D, ItemClassification.useful),
    "Earth Destiny Deck": ItemData(0x1F28000E, ItemClassification.useful),
    "Water Destiny Deck": ItemData(0x1F28000F, ItemClassification.useful),
    "Wind Destiny Deck": ItemData(0x1F280010, ItemClassification.useful),
    "Card Sleeves (Clear)": ItemData(0x1F280012, ItemClassification.useful),
    "Card Sleeves (Tetramon)": ItemData(0x1F280013, ItemClassification.useful),
    "D20 Dice Red": ItemData(0x1F280014, ItemClassification.useful),
    "D20 Dice Blue": ItemData(0x1F280015, ItemClassification.useful),
    "D20 Dice Black": ItemData(0x1F280016, ItemClassification.useful),
    "D20 Dice White": ItemData(0x1F280017, ItemClassification.useful),
    "Card Sleeves (Fire)": ItemData(0x1F280018, ItemClassification.useful),
    "Card Sleeves (Earth)": ItemData(0x1F280019, ItemClassification.useful),
    "Card Sleeves (Water)": ItemData(0x1F28001A, ItemClassification.useful),
    "Card Sleeves (Wind)": ItemData(0x1F28001B, ItemClassification.useful),
    "Collection Book": ItemData(0x1F280020, ItemClassification.useful),
    "Premium Collection Book": ItemData(0x1F280021, ItemClassification.useful),
    "Playmat (Drilceros)": ItemData(0x1F280022, ItemClassification.useful),
    "Playmat (Clamigo)": ItemData(0x1F280023, ItemClassification.useful),
    "Playmat (Wispo)": ItemData(0x1F280024, ItemClassification.useful),
    "Playmat (Lunight)": ItemData(0x1F280025, ItemClassification.useful),
    "Playmat (Kyrone)": ItemData(0x1F280026, ItemClassification.useful),
    "Playmat (Duel)": ItemData(0x1F280027, ItemClassification.useful),
    "Playmat (Dracunix1)": ItemData(0x1F280028, ItemClassification.useful),
    "Playmat (The Four Dragons)": ItemData(0x1F280029, ItemClassification.useful),
    "Playmat (Drakon)": ItemData(0x1F28002A, ItemClassification.useful),
    "Playmat (GigatronX Evo)": ItemData(0x1F28002B, ItemClassification.useful),
    "Playmat (Fire)": ItemData(0x1F28002C, ItemClassification.useful),
    "Playmat (Earth)": ItemData(0x1F28002D, ItemClassification.useful),
    "Playmat (Water)": ItemData(0x1F28002E, ItemClassification.useful),
    "Playmat (Wind)": ItemData(0x1F28002F, ItemClassification.useful),
    "Playmat (Tetramon)": ItemData(0x1F280030, ItemClassification.useful),
    "Pigni Plushie": ItemData(0x1F280031, ItemClassification.useful),
    "Nanomite Plushie": ItemData(0x1F280032, ItemClassification.useful),
    "Minstar Plushie": ItemData(0x1F280033, ItemClassification.useful),
    "Nocti Plushie": ItemData(0x1F280034, ItemClassification.useful),
    "Burpig Figurine": ItemData(0x1F280035, ItemClassification.useful),
    "Decimite Figurine": ItemData(0x1F280036, ItemClassification.useful),
    "Trickstar Figurine": ItemData(0x1F280037, ItemClassification.useful),
    "Lunight Figurine": ItemData(0x1F280038, ItemClassification.useful),
    "Inferhog Figurine": ItemData(0x1F280039, ItemClassification.useful),
    "Meganite Figurine": ItemData(0x1F28003A, ItemClassification.useful),
    "Princestar Figurine": ItemData(0x1F28003B, ItemClassification.useful),
    "Vampicant Figurine": ItemData(0x1F28003C, ItemClassification.useful),
    "Blazoar Plushie": ItemData(0x1F28003D, ItemClassification.useful),
    "Giganite Statue": ItemData(0x1F28003E, ItemClassification.useful),
    "Kingstar Plushie": ItemData(0x1F28003F, ItemClassification.useful),
    "Dracunix Figurine": ItemData(0x1F280040, ItemClassification.useful),
    "Bonfiox Plushie": ItemData(0x1F280041, ItemClassification.useful),
    "Drilceros Action Figure": ItemData(0x1F280042, ItemClassification.useful),
    "ToonZ Plushie": ItemData(0x1F280043, ItemClassification.useful),
    "Small Cabinet": ItemData(0x1F280044, ItemClassification.useful),
    "Small Metal Rack": ItemData(0x1F280045, ItemClassification.useful),
    "Single Sided Shelf": ItemData(0x1F280046, ItemClassification.useful),
    "Double Sided Shelf": ItemData(0x1F280047, ItemClassification.useful),
    "Wide Shelf": ItemData(0x1F280048, ItemClassification.useful),
    "Play Table": ItemData(0x1F28004E, ItemClassification.useful),
    "Workbench": ItemData(0x1F28004F, ItemClassification.useful),
    "Trash Bin": ItemData(0x1F280050, ItemClassification.useful),
    "Checkout Counter": ItemData(0x1F280051, ItemClassification.useful),
    "System Gate #1": ItemData(0x1F280052, ItemClassification.useful),
    "System Gate #2": ItemData(0x1F280053, ItemClassification.useful),
    "Mafia Works": ItemData(0x1F280054, ItemClassification.useful),
    "Necromonsters": ItemData(0x1F280055, ItemClassification.useful),
    "Claim!": ItemData(0x1F280056, ItemClassification.useful),
    "Penny Sleeves": ItemData(0x1F280057, ItemClassification.useful),
    "Tower Deckbox": ItemData(0x1F280058, ItemClassification.useful),
    "Magnetic Holder": ItemData(0x1F280059, ItemClassification.useful),
    "Toploader": ItemData(0x1F28005A, ItemClassification.useful),
    "Card Preserver": ItemData(0x1F28005B, ItemClassification.useful),
    "Playmat Gray": ItemData(0x1F28005C, ItemClassification.useful),
    "Playmat Green": ItemData(0x1F28005D, ItemClassification.useful),
    "Playmat Purple": ItemData(0x1F28005E, ItemClassification.useful),
    "Playmat Yellow": ItemData(0x1F28005F, ItemClassification.useful),
    "Pocket Pages": ItemData(0x1F280060, ItemClassification.useful),
    "Card Holder": ItemData(0x1F280061, ItemClassification.useful),
    "Collectors Album": ItemData(0x1F2800B5, ItemClassification.useful),
    "Worker - Zachery": ItemData(0x1F2800B6, ItemClassification.useful),
    "Worker - Terence": ItemData(0x1F2800B7, ItemClassification.useful),
    "Worker - Dennis": ItemData(0x1F2800B8, ItemClassification.useful),
    "Worker - Clark": ItemData(0x1F2800B9, ItemClassification.useful),
    "Worker - Angus": ItemData(0x1F2800BA, ItemClassification.useful),
    "Worker - Benji": ItemData(0x1F2800BB, ItemClassification.useful),
    "Worker - Lauren": ItemData(0x1F2800BC, ItemClassification.useful),
    "Worker - Axel": ItemData(0x1F2800BD, ItemClassification.useful),
    "Playmat (Dracunix2)": ItemData(0x1F2800BE, ItemClassification.useful),
    "Playmat (GigatronX)": ItemData(0x1F2800BF, ItemClassification.useful),
    "Playmat (Katengu Black)": ItemData(0x1F2800C2, ItemClassification.useful),
    "Playmat (Katengu White)": ItemData(0x1F2800C3, ItemClassification.useful),
    "Manga 1": ItemData(0x1F2800C4, ItemClassification.useful),
    "Manga 2": ItemData(0x1F2800C5, ItemClassification.useful),
    "Manga 3": ItemData(0x1F2800C6, ItemClassification.useful),
    "Manga 4": ItemData(0x1F2800C7, ItemClassification.useful),
    "Manga 5": ItemData(0x1F2800C8, ItemClassification.useful),
    "Manga 6": ItemData(0x1F2800C9, ItemClassification.useful),
    "Manga 7": ItemData(0x1F2800CA, ItemClassification.useful),
    "Manga 8": ItemData(0x1F2800CB, ItemClassification.useful),
    "Manga 9": ItemData(0x1F2800CC, ItemClassification.useful),
    "Manga 10": ItemData(0x1F2800CD, ItemClassification.useful),
    "Manga 11": ItemData(0x1F2800CE, ItemClassification.useful),
    "Manga 12": ItemData(0x1F2800CF, ItemClassification.useful),
    "Warehouse Unlock": ItemData(0x1F2800D8, ItemClassification.progression),
    "Basic Card Pack (32)": ItemData(0x1F280001, ItemClassification.progression),
    "Basic Card Pack (64)": ItemData(0x1F2800D8, ItemClassification.progression),
    "Basic Card Box (4)": ItemData(0x1F2800D9, ItemClassification.progression),
    "Basic Card Box (8)": ItemData(0x1F2800DA, ItemClassification.progression),
    "Rare Card Pack (32)": ItemData(0x1F280002, ItemClassification.progression),
    "Rare Card Pack (64)": ItemData(0x1F2800DB, ItemClassification.progression),
    "Rare Card Box (4)": ItemData(0x1F2800DC, ItemClassification.progression),
    "Rare Card Box (8)": ItemData(0x1F2800DD, ItemClassification.progression),
    "Epic Card Pack (32)": ItemData(0x1F280003, ItemClassification.progression),
    "Epic Card Pack (64)": ItemData(0x1F2800DE, ItemClassification.progression),
    "Epic Card Box (4)": ItemData(0x1F2800DF, ItemClassification.progression),
    "Epic Card Box (8)": ItemData(0x1F2800E0, ItemClassification.progression),
    "Legendary Card Pack (32)": ItemData(0x1F280004, ItemClassification.progression),
    "Legendary Card Pack (64)": ItemData(0x1F2800E1, ItemClassification.progression),
    "Legendary Card Box (4)": ItemData(0x1F2800E2, ItemClassification.progression),
    "Legendary Card Box (8)": ItemData(0x1F2800E3, ItemClassification.progression),
    "Basic Destiny Pack (32)": ItemData(0x1F280009, ItemClassification.progression),
    "Basic Destiny Pack (64)": ItemData(0x1F2800E4, ItemClassification.progression),
    "Basic Destiny Box (4)": ItemData(0x1F2800E5, ItemClassification.progression),
    "Basic Destiny Box (8)": ItemData(0x1F2800E6, ItemClassification.progression),
    "Rare Destiny Pack (32)": ItemData(0x1F28000A, ItemClassification.progression),
    "Rare Destiny Pack (64)": ItemData(0x1F2800E7, ItemClassification.progression),
    "Rare Destiny Box (4)": ItemData(0x1F2800E8, ItemClassification.progression),
    "Rare Destiny Box (8)": ItemData(0x1F2800E9, ItemClassification.progression),
    "Epic Destiny Pack (32)": ItemData(0x1F28000B, ItemClassification.useful),
    "Epic Destiny Pack (64)": ItemData(0x1F2800EA, ItemClassification.useful),
    "Epic Destiny Box (4)": ItemData(0x1F2800EB, ItemClassification.useful),
    "Epic Destiny Box (8)": ItemData(0x1F2800EC, ItemClassification.useful),
    "Legendary Destiny Pack (32)": ItemData(0x1F28000C, ItemClassification.useful),
    "Legendary Destiny Pack (64)": ItemData(0x1F2800ED, ItemClassification.useful),
    "Legendary Destiny Box (4)": ItemData(0x1F2800EE, ItemClassification.useful),
    "Legendary Destiny Box (8)": ItemData(0x1F2800EF, ItemClassification.useful),
    "Cleanser (8)": ItemData(0x1F280011, ItemClassification.useful),
    "Cleanser (64)": ItemData(0x1F2800F0, ItemClassification.useful),
    "Deck Box Red (8)": ItemData(0x1F28001C, ItemClassification.useful),
    "Deck Box Red (16)": ItemData(0x1F2800F1, ItemClassification.useful),
    "Deck Box Green (8)": ItemData(0x1F28001D, ItemClassification.useful),
    "Deck Box Green (16)": ItemData(0x1F2800F2, ItemClassification.useful),
    "Deck Box Blue (8)": ItemData(0x1F28001E, ItemClassification.useful),
    "Deck Box Blue (16)": ItemData(0x1F2800F3, ItemClassification.useful),
    "Deck Box Yellow (8)": ItemData(0x1F28001F, ItemClassification.useful),
    "Deck Box Yellow (16)": ItemData(0x1F2800F4, ItemClassification.useful),
}

progressive_dict: Dict[str, ItemData] = {
    "Progressive Card Table": ItemData(0x1F280049, ItemClassification.useful, 2),
    "Progressive Card Display": ItemData(0x1F28004A, ItemClassification.useful, 3),
    "Progressive Personal Shelf": ItemData(0x1F28004B, ItemClassification.useful, 3),
    "Progressive Auto Scent": ItemData(0x1F28004C, ItemClassification.useful, 3),
    "Progressive Warehouse Shelf": ItemData(0x1F28004D, ItemClassification.useful, 2),
    "Progressive Shop Expansion A": ItemData(0x1F2800C0, ItemClassification.progression, 30),
    "Progressive Shop Expansion B": ItemData(0x1F2800C1, ItemClassification.useful, 14),
    "Progressive Ghost Card": ItemData(0x1F2800D7, ItemClassification.progression_skip_balancing, 0)
}

ghost_dict: Dict[str, ItemData] = {
    "Ghost Blazoar (white)": ItemData(0x1F280062, ItemClassification.progression_skip_balancing),
    "Ghost Blazoar (Black)": ItemData(0x1F280063, ItemClassification.progression_skip_balancing),
    "Foil Ghost Blazoar (white)": ItemData(0x1F280064, ItemClassification.progression_skip_balancing),
    "Foil Ghost Blazoar (Black)": ItemData(0x1F280065, ItemClassification.progression_skip_balancing),
    "Ghost Kyuenbi (white)": ItemData(0x1F280066, ItemClassification.progression_skip_balancing),
    "Ghost Kyuenbi (Black)": ItemData(0x1F280067, ItemClassification.progression_skip_balancing),
    "Foil Ghost Kyuenbi (white)": ItemData(0x1F280068, ItemClassification.progression_skip_balancing),
    "Foil Ghost Kyuenbi (Black)": ItemData(0x1F280069, ItemClassification.progression_skip_balancing),
    "Ghost Giganite (white)": ItemData(0x1F28006A, ItemClassification.progression_skip_balancing),
    "Ghost Giganite (Black)": ItemData(0x1F28006B, ItemClassification.progression_skip_balancing),
    "Foil Ghost Giganite (white)": ItemData(0x1F28006C, ItemClassification.progression_skip_balancing),
    "Foil Ghost Giganite (Black)": ItemData(0x1F28006D, ItemClassification.progression_skip_balancing),
    "Ghost Mammotree (white)": ItemData(0x1F28006E, ItemClassification.progression_skip_balancing),
    "Ghost Mammotree (Black)": ItemData(0x1F28006F, ItemClassification.progression_skip_balancing),
    "Foil Ghost Mammotree (white)": ItemData(0x1F280070, ItemClassification.progression_skip_balancing),
    "Foil Ghost Mammotree (Black)": ItemData(0x1F280071, ItemClassification.progression_skip_balancing),
    "Ghost Kingstar (white)": ItemData(0x1F280072, ItemClassification.progression_skip_balancing),
    "Ghost Kingstar (Black)": ItemData(0x1F280073, ItemClassification.progression_skip_balancing),
    "Foil Ghost Kingstar (white)": ItemData(0x1F280074, ItemClassification.progression_skip_balancing),
    "Foil Ghost Kingstar (Black)": ItemData(0x1F280075, ItemClassification.progression_skip_balancing),
    "Ghost Fistronk (white)": ItemData(0x1F280076, ItemClassification.progression_skip_balancing),
    "Ghost Fistronk (Black)": ItemData(0x1F280077, ItemClassification.progression_skip_balancing),
    "Foil Ghost Fistronk (white)": ItemData(0x1F280078, ItemClassification.progression_skip_balancing),
    "Foil Ghost Fistronk (Black)": ItemData(0x1F280079, ItemClassification.progression_skip_balancing),
    "Ghost Royalama (white)": ItemData(0x1F28007A, ItemClassification.progression_skip_balancing),
    "Ghost Royalama (Black)": ItemData(0x1F28007B, ItemClassification.progression_skip_balancing),
    "Foil Ghost Royalama (white)": ItemData(0x1F28007C, ItemClassification.progression_skip_balancing),
    "Foil Ghost Royalama (Black)": ItemData(0x1F28007D, ItemClassification.progression_skip_balancing),
    "Ghost Dracunix (white)": ItemData(0x1F28007E, ItemClassification.progression_skip_balancing),
    "Ghost Dracunix (Black)": ItemData(0x1F28007F, ItemClassification.progression_skip_balancing),
    "Foil Ghost Dracunix (white)": ItemData(0x1F280080, ItemClassification.progression_skip_balancing),
    "Foil Ghost Dracunix (Black)": ItemData(0x1F280081, ItemClassification.progression_skip_balancing),
    "Ghost Magnoria (white)": ItemData(0x1F280082, ItemClassification.progression_skip_balancing),
    "Ghost Magnoria (Black)": ItemData(0x1F280083, ItemClassification.progression_skip_balancing),
    "Foil Ghost Magnoria (white)": ItemData(0x1F280084, ItemClassification.progression_skip_balancing),
    "Foil Ghost Magnoria (Black)": ItemData(0x1F280085, ItemClassification.progression_skip_balancing),
    "Ghost Hydroid (white)": ItemData(0x1F280086, ItemClassification.progression_skip_balancing),
    "Ghost Hydroid (Black)": ItemData(0x1F280087, ItemClassification.progression_skip_balancing),
    "Foil Ghost Hydroid (white)": ItemData(0x1F280088, ItemClassification.progression_skip_balancing),
    "Foil Ghost Hydroid (Black)": ItemData(0x1F280089, ItemClassification.progression_skip_balancing),
    "Ghost Drakon (white)": ItemData(0x1F28008A, ItemClassification.progression_skip_balancing),
    "Ghost Drakon (Black)": ItemData(0x1F28008B, ItemClassification.progression_skip_balancing),
    "Foil Ghost Drakon (white)": ItemData(0x1F28008C, ItemClassification.progression_skip_balancing),
    "Foil Ghost Drakon (Black)": ItemData(0x1F28008D, ItemClassification.progression_skip_balancing),
    "Ghost Bogon (white)": ItemData(0x1F28008E, ItemClassification.progression_skip_balancing),
    "Ghost Bogon (Black)": ItemData(0x1F28008F, ItemClassification.progression_skip_balancing),
    "Foil Ghost Bogon (white)": ItemData(0x1F280090, ItemClassification.progression_skip_balancing),
    "Foil Ghost Bogon (Black)": ItemData(0x1F280091, ItemClassification.progression_skip_balancing),
    "Ghost Hydron (white)": ItemData(0x1F280092, ItemClassification.progression_skip_balancing),
    "Ghost Hydron (Black)": ItemData(0x1F280093, ItemClassification.progression_skip_balancing),
    "Foil Ghost Hydron (white)": ItemData(0x1F280094, ItemClassification.progression_skip_balancing),
    "Foil Ghost Hydron (Black)": ItemData(0x1F280095, ItemClassification.progression_skip_balancing),
    "Ghost Raizon (white)": ItemData(0x1F280096, ItemClassification.progression_skip_balancing),
    "Ghost Raizon (Black)": ItemData(0x1F280097, ItemClassification.progression_skip_balancing),
    "Foil Ghost Raizon (white)": ItemData(0x1F280098, ItemClassification.progression_skip_balancing),
    "Foil Ghost Raizon (Black)": ItemData(0x1F280099, ItemClassification.progression_skip_balancing),
    "Ghost Lucadence (white)": ItemData(0x1F28009A, ItemClassification.progression_skip_balancing),
    "Ghost Lucadence (Black)": ItemData(0x1F28009B, ItemClassification.progression_skip_balancing),
    "Foil Ghost Lucadence (white)": ItemData(0x1F28009C, ItemClassification.progression_skip_balancing),
    "Foil Ghost Lucadence (Black)": ItemData(0x1F28009D, ItemClassification.progression_skip_balancing),
    "Ghost Jigajawr (white)": ItemData(0x1F28009E, ItemClassification.progression_skip_balancing),
    "Ghost Jigajawr (Black)": ItemData(0x1F28009F, ItemClassification.progression_skip_balancing),
    "Foil Ghost Jigajawr (white)": ItemData(0x1F2800A0, ItemClassification.progression_skip_balancing),
    "Foil Ghost Jigajawr (Black)": ItemData(0x1F2800A1, ItemClassification.progression_skip_balancing),
    "Ghost Jacktern (white)": ItemData(0x1F2800A2, ItemClassification.progression_skip_balancing),
    "Ghost Jacktern (Black)": ItemData(0x1F2800A3, ItemClassification.progression_skip_balancing),
    "Foil Ghost Jacktern (white)": ItemData(0x1F2800A4, ItemClassification.progression_skip_balancing),
    "Foil Ghost Jacktern (Black)": ItemData(0x1F2800A5, ItemClassification.progression_skip_balancing),
    "Ghost GigatronX (white)": ItemData(0x1F2800A6, ItemClassification.progression_skip_balancing),
    "Ghost GigatronX (Black)": ItemData(0x1F2800A7, ItemClassification.progression_skip_balancing),
    "Foil Ghost GigatronX (white)": ItemData(0x1F2800A8, ItemClassification.progression_skip_balancing),
    "Foil Ghost GigatronX (Black)": ItemData(0x1F2800A9, ItemClassification.progression_skip_balancing),
    "Ghost Clawcifear (white)": ItemData(0x1F2800AA, ItemClassification.progression_skip_balancing),
    "Ghost Clawcifear (Black)": ItemData(0x1F2800AB, ItemClassification.progression_skip_balancing),
    "Foil Ghost Clawcifear (white)": ItemData(0x1F2800AC, ItemClassification.progression_skip_balancing),
    "Foil Ghost Clawcifear (Black)": ItemData(0x1F2800AD, ItemClassification.progression_skip_balancing),
    "Ghost Katengu (white)": ItemData(0x1F2800AE, ItemClassification.progression_skip_balancing),
    "Ghost Katengu (Black)": ItemData(0x1F2800AF, ItemClassification.progression_skip_balancing),
    "Foil Ghost Katengu (white)": ItemData(0x1F2800B0, ItemClassification.progression_skip_balancing),
    "Foil Ghost Katengu (Black)": ItemData(0x1F2800B1, ItemClassification.progression_skip_balancing),
}

junk_dict: Dict[str, ItemData] = {
    "Small Xp": ItemData(0x1F2800B2, ItemClassification.filler),
    "Small Money": ItemData(0x1F2800B3, ItemClassification.filler),
    "Medium Xp": ItemData(0x1F2800D0, ItemClassification.filler),
    "Medium Money": ItemData(0x1F2800D1, ItemClassification.filler),
    "Large Xp": ItemData(0x1F2800D2, ItemClassification.filler),
    "Large Money": ItemData(0x1F2800D3, ItemClassification.filler),
    "Random Card": ItemData(0x1F2800D4, ItemClassification.filler),
    "Random New Card": ItemData(0x1F2800D5, ItemClassification.filler),
}

trap_dict: Dict[str, ItemData] = {
    "Stink Trap": ItemData(0x1F2800B4, ItemClassification.trap),
    "Poltergeist Trap": ItemData(0x1F2800D6, ItemClassification.trap),
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
