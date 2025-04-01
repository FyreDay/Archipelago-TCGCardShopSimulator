from typing import Dict, Optional, List, Tuple, NamedTuple
import math

from BaseClasses import Item, ItemClassification


class TCGSimulatorItem(Item):
    game: str = "TCG Card Shop Simulator"

class ItemData(NamedTuple):
    code: int
    itemName: str
    classification: ItemClassification
    amount: Optional[int] = 1



def create_item(world, name: str, classification: ItemClassification, amount: Optional[int] = 1):
    for i in range(amount):
        world.multiworld.itempool.append(Item(name, classification, world.item_name_to_id[name], world.player))

def create_items(world):
    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))

    for item in itemList:
        create_item(world, item.itemName, item.classification)

    for item in progressivelist:
        create_item(world, item.itemName, item.classification, item.amount)

    create_item(world, expB.itemName, expB.classification, expB.amount)
    if (world.options.goal.value == 2):
        for item in ghostlist:
            create_item(world, item.itemName, item.classification)

    if (world.options.goal.value == 0):
        create_item(world, expA.itemName, ItemClassification.progression,expA.amount)
    else:
        create_item(world, expA.itemName, ItemClassification.progression,expA.amount)

    remaining_locations = total_location_count - len(itemList) - (len(progressivelist) + 36) - 14 - 30 - (0 if world.options.goal.value != 2 else 80)
    print(f"Remaining items here: {remaining_locations}")
    trap_count = round(remaining_locations * world.options.trap_fill.value / 100)
    junk_count = remaining_locations - trap_count

    trap_weights = {
        "Stink Trap": 10,
    }


    junk = get_junk_item_names(world.multiworld.random, junk_count)
    for name in junk:
        create_item(world, name, ItemClassification.filler)

    trap = get_trap_item_names(world.multiworld.random, trap_count, trap_weights)
    for name in trap:
        create_item(world, name, ItemClassification.trap)

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

startid = 0x1F280000

itemList: List[ItemData] = [
    
    ItemData(0x1F280005, "Fire Battle Deck", ItemClassification.useful),
    ItemData(0x1F280006, "Earth Battle Deck", ItemClassification.useful),
    ItemData(0x1F280007, "Water Battle Deck", ItemClassification.useful),
    ItemData(0x1F280008, "Wind Battle Deck", ItemClassification.useful),

    ItemData(0x1F28000D, "Fire Destiny Deck", ItemClassification.useful),
    ItemData(0x1F28000E, "Earth Destiny Deck", ItemClassification.useful),
    ItemData(0x1F28000F, "Water Destiny Deck", ItemClassification.useful),
    ItemData(0x1F280010, "Wind Destiny Deck", ItemClassification.useful),
    
    ItemData(0x1F280012, "Card Sleeves (Clear)", ItemClassification.useful),
    ItemData(0x1F280013, "Card Sleeves (Tetramon)", ItemClassification.useful),
    ItemData(0x1F280014, "D20 Dice Red", ItemClassification.useful),
    ItemData(0x1F280015, "D20 Dice Blue", ItemClassification.useful),
    ItemData(0x1F280016, "D20 Dice Black", ItemClassification.useful),
    ItemData(0x1F280017, "D20 Dice White", ItemClassification.useful),
    ItemData(0x1F280018, "Card Sleeves (Fire)", ItemClassification.useful),
    ItemData(0x1F280019, "Card Sleeves (Earth)", ItemClassification.useful),
    ItemData(0x1F28001A, "Card Sleeves (Water)", ItemClassification.useful),
    ItemData(0x1F28001B, "Card Sleeves (Wind)", ItemClassification.useful),
    
    ItemData(0x1F280020, "Collection Book", ItemClassification.useful),
    ItemData(0x1F280021, "Premium Collection Book", ItemClassification.useful),
    ItemData(0x1F280022, "Playmat (Drilceros)", ItemClassification.useful),
    ItemData(0x1F280023, "Playmat (Clamigo)", ItemClassification.useful),
    ItemData(0x1F280024, "Playmat (Wispo)", ItemClassification.useful),
    ItemData(0x1F280025, "Playmat (Lunight)", ItemClassification.useful),
    ItemData(0x1F280026, "Playmat (Kyrone)", ItemClassification.useful),
    ItemData(0x1F280027, "Playmat (Duel)", ItemClassification.useful),
    ItemData(0x1F280028, "Playmat (Dracunix1)", ItemClassification.useful),
    ItemData(0x1F280029, "Playmat (The Four Dragons)", ItemClassification.useful),
    ItemData(0x1F28002A, "Playmat (Drakon)", ItemClassification.useful),
    ItemData(0x1F28002B, "Playmat (GigatronX Evo)", ItemClassification.useful),
    ItemData(0x1F28002C, "Playmat (Fire)", ItemClassification.useful),
    ItemData(0x1F28002D, "Playmat (Earth)", ItemClassification.useful),
    ItemData(0x1F28002E, "Playmat (Water)", ItemClassification.useful),
    ItemData(0x1F28002F, "Playmat (Wind)", ItemClassification.useful),
    ItemData(0x1F280030, "Playmat (Tetramon)", ItemClassification.useful),
    ItemData(0x1F280031, "Pigni Plushie (12)", ItemClassification.useful),
    ItemData(0x1F280032, "Nanomite Plushie (16)", ItemClassification.useful),
    ItemData(0x1F280033, "Minstar Plushie (24)", ItemClassification.useful),
    ItemData(0x1F280034, "Nocti Plushie (6)", ItemClassification.useful),
    ItemData(0x1F280035, "Burpig Figurine (12)", ItemClassification.useful),
    ItemData(0x1F280036, "Decimite Figurine (8)", ItemClassification.useful),
    ItemData(0x1F280037, "Trickstar Figurine (12)", ItemClassification.useful),
    ItemData(0x1F280038, "Lunight Figurine (8)", ItemClassification.useful),
    ItemData(0x1F280039, "Inferhog Figurine (2)", ItemClassification.useful),
    ItemData(0x1F28003A, "Meganite Figurine (2)", ItemClassification.useful),
    ItemData(0x1F28003B, "Princestar Figurine (2)", ItemClassification.useful),
    ItemData(0x1F28003C, "Vampicant Figurine (2)", ItemClassification.useful),
    ItemData(0x1F28003D, "Blazoar Plushie (2)", ItemClassification.useful),
    ItemData(0x1F28003E, "Giganite Statue (2)", ItemClassification.useful),
    ItemData(0x1F28003F, "Kingstar Plushie (2)", ItemClassification.useful),
    ItemData(0x1F280040, "Dracunix Figurine (1)", ItemClassification.useful),
    ItemData(0x1F280041, "Bonfiox Plushie (8)", ItemClassification.useful),
    ItemData(0x1F280042, "Drilceros Action Figure (4)", ItemClassification.useful),
    ItemData(0x1F280043, "ToonZ Plushie (6)", ItemClassification.useful),
    # ItemData(0x1F280044, "Small Cabinet", ItemClassification.useful),
    ItemData(0x1F280045, "Small Metal Rack", ItemClassification.useful),
    ItemData(0x1F280046, "Single Sided Shelf", ItemClassification.useful),
    ItemData(0x1F280047, "Double Sided Shelf", ItemClassification.useful),
    ItemData(0x1F280048, "Wide Shelf", ItemClassification.useful),
    
    ItemData(0x1F28004E, "Play Table", ItemClassification.useful),
    ItemData(0x1F28004F, "Workbench", ItemClassification.useful),
    ItemData(0x1F280050, "Trash Bin", ItemClassification.useful),
    ItemData(0x1F280051, "Checkout Counter", ItemClassification.useful),
    ItemData(0x1F280052, "System Gate #1", ItemClassification.useful),
    ItemData(0x1F280053, "System Gate #2", ItemClassification.useful),
    ItemData(0x1F280054, "Mafia Works", ItemClassification.useful),
    ItemData(0x1F280055, "Necromonsters", ItemClassification.useful),
    ItemData(0x1F280056, "Claim!", ItemClassification.useful),
    ItemData(0x1F280057, "Penny Sleeves", ItemClassification.useful),
    ItemData(0x1F280058, "Tower Deckbox", ItemClassification.useful),
    ItemData(0x1F280059, "Magnetic Holder", ItemClassification.useful),
    ItemData(0x1F28005A, "Toploader", ItemClassification.useful),
    ItemData(0x1F28005B, "Card Preserver", ItemClassification.useful),
    ItemData(0x1F28005C, "Playmat Gray", ItemClassification.useful),
    ItemData(0x1F28005D, "Playmat Green", ItemClassification.useful),
    ItemData(0x1F28005E, "Playmat Purple", ItemClassification.useful),
    ItemData(0x1F28005F, "Playmat Yellow", ItemClassification.useful),
    ItemData(0x1F280060, "Pocket Pages", ItemClassification.useful),
    ItemData(0x1F280061, "Card Holder", ItemClassification.useful),
    ItemData(0x1F2800B5, "Collectors Album", ItemClassification.useful),
    ItemData(0x1F2800B6, "Worker - Zachery", ItemClassification.useful),
    ItemData(0x1F2800B7, "Worker - Terence", ItemClassification.useful),
    ItemData(0x1F2800B8, "Worker - Dennis", ItemClassification.useful),
    ItemData(0x1F2800B9, "Worker - Clark", ItemClassification.useful),
    ItemData(0x1F2800BA, "Worker - Angus", ItemClassification.useful),
    ItemData(0x1F2800BB, "Worker - Benji", ItemClassification.useful),
    ItemData(0x1F2800BC, "Worker - Lauren", ItemClassification.useful),
    ItemData(0x1F2800BD, "Worker - Axel", ItemClassification.useful),
    ItemData(0x1F2800BE, "Playmat (Dracunix2)", ItemClassification.useful),
    ItemData(0x1F2800BF, "Playmat (GigatronX)", ItemClassification.useful),
    ItemData(0x1F2800C2, "Playmat (Katengu Black)", ItemClassification.useful),
    ItemData(0x1F2800C3, "Playmat (Katengu White)", ItemClassification.useful),
    ItemData(0x1F2800C4, "Manga 1", ItemClassification.useful),
    ItemData(0x1F2800C5, "Manga 2", ItemClassification.useful),
    ItemData(0x1F2800C6, "Manga 3", ItemClassification.useful),
    ItemData(0x1F2800C7, "Manga 4", ItemClassification.useful),
    ItemData(0x1F2800C8, "Manga 5", ItemClassification.useful),
    ItemData(0x1F2800C9, "Manga 6", ItemClassification.useful),
    ItemData(0x1F2800CA, "Manga 7", ItemClassification.useful),
    ItemData(0x1F2800CB, "Manga 8", ItemClassification.useful),
    ItemData(0x1F2800CC, "Manga 9", ItemClassification.useful),
    ItemData(0x1F2800CD, "Manga 10", ItemClassification.useful),
    ItemData(0x1F2800CE, "Manga 11", ItemClassification.useful),
    ItemData(0x1F2800CF, "Manga 12", ItemClassification.useful),

]

progressivelist: List[ItemData] = [
    ItemData(0x1F280001, "Progressive Basic Card Pack", ItemClassification.progression, 3),
    ItemData(0x1F280002, "Progressive Rare Card Pack", ItemClassification.progression, 4),
    ItemData(0x1F280003, "Progressive Epic Card Pack", ItemClassification.progression, 4),
    ItemData(0x1F280004, "Progressive Legendary Card Pack", ItemClassification.progression, 4),
    ItemData(0x1F280009, "Progressive Basic Destiny Pack", ItemClassification.progression, 4),
    ItemData(0x1F28000A, "Progressive Rare Destiny Pack", ItemClassification.progression, 4),
    ItemData(0x1F28000B, "Progressive Epic Destiny Pack", ItemClassification.useful, 4),
    ItemData(0x1F28000C, "Progressive Legendary Destiny Pack", ItemClassification.useful, 4),
    ItemData(0x1F280011, "Progressive Cleanser", ItemClassification.useful, 2),
    ItemData(0x1F28001C, "Progressive Deck Box Red", ItemClassification.useful, 2),
    ItemData(0x1F28001D, "Progressive Deck Box Green", ItemClassification.useful, 2),
    ItemData(0x1F28001E, "Progressive Deck Box Blue", ItemClassification.useful, 2),
    ItemData(0x1F28001F, "Progressive Deck Box Yellow", ItemClassification.useful, 2),
    ItemData(0x1F280049, "Progressive Card Table", ItemClassification.useful, 2),
    ItemData(0x1F28004A, "Progressive Card Display", ItemClassification.useful, 3),
    ItemData(0x1F28004B, "Progressive Personal Shelf", ItemClassification.useful, 3),
    ItemData(0x1F28004C, "Progressive Auto Scent", ItemClassification.useful, 3),
    ItemData(0x1F28004D, "Progressive Warehouse Shelf", ItemClassification.useful,2),
]

junklist: List[ItemData] = [
    ItemData(0x1F2800B2, "Small Xp", ItemClassification.filler),
    ItemData(0x1F2800B3, "Small Money", ItemClassification.filler),
    ItemData(0x1F2800D0, "Medium Xp", ItemClassification.filler),
    ItemData(0x1F2800D1, "Medium Money", ItemClassification.filler),
    ItemData(0x1F2800D2, "Large Xp", ItemClassification.filler),
    ItemData(0x1F2800D3, "Large Money", ItemClassification.filler),
    ItemData(0x1F2800D4, "Random Card", ItemClassification.filler),
    ItemData(0x1F2800D5, "Random New Card", ItemClassification.filler),
]

junk_weights = {
    "Small Xp": 50,
    "Small Money": 50,
    "Medium Money": 25,
    "Medium Xp": 25,
    "Large Money": 10,
    "Large Xp": 10,
    "Random Card": 50
}

traplist: List[ItemData] = [
    ItemData(0x1F2800B4, "Stink Trap", ItemClassification.trap),#be
    ItemData(0x1F2800D6, "Stink Trap", ItemClassification.trap),#be
]

ghostlist: List[ItemData] = [
    ItemData(0x1F280062, "Ghost Blazoar (white)", ItemClassification.progression),
    ItemData(0x1F280063, "Ghost Blazoar (Black)", ItemClassification.progression),
    ItemData(0x1F280064, "Foil Ghost Blazoar (white)", ItemClassification.progression),
    ItemData(0x1F280065, "Foil Ghost Blazoar (Black)", ItemClassification.progression),
    ItemData(0x1F280066, "Ghost Kyuenbi (white)", ItemClassification.progression),
    ItemData(0x1F280067, "Ghost Kyuenbi (Black)", ItemClassification.progression),
    ItemData(0x1F280068, "Foil Ghost Kyuenbi (white)", ItemClassification.progression),
    ItemData(0x1F280069, "Foil Ghost Kyuenbi (Black)", ItemClassification.progression),
    ItemData(0x1F28006A, "Ghost Giganite (white)", ItemClassification.progression),
    ItemData(0x1F28006B, "Ghost Giganite (Black)", ItemClassification.progression),
    ItemData(0x1F28006C, "Foil Ghost Giganite (white)", ItemClassification.progression),
    ItemData(0x1F28006D, "Foil Ghost Giganite (Black)", ItemClassification.progression),
    ItemData(0x1F28006E, "Ghost Mammotree (white)", ItemClassification.progression),
    ItemData(0x1F28006F, "Ghost Mammotree (Black)", ItemClassification.progression),
    ItemData(0x1F280070, "Foil Ghost Mammotree (white)", ItemClassification.progression),
    ItemData(0x1F280071, "Foil Ghost Mammotree (Black)", ItemClassification.progression),
    ItemData(0x1F280072, "Ghost Kingstar (white)", ItemClassification.progression),
    ItemData(0x1F280073, "Ghost Kingstar (Black)", ItemClassification.progression),
    ItemData(0x1F280074, "Foil Ghost Kingstar (white)", ItemClassification.progression),
    ItemData(0x1F280075, "Foil Ghost Kingstar (Black)", ItemClassification.progression),
    ItemData(0x1F280076, "Ghost Fistronk (white)", ItemClassification.progression),
    ItemData(0x1F280077, "Ghost Fistronk (Black)", ItemClassification.progression),
    ItemData(0x1F280078, "Foil Ghost Fistronk (white)", ItemClassification.progression),
    ItemData(0x1F280079, "Foil Ghost Fistronk (Black)", ItemClassification.progression),
    ItemData(0x1F28007A, "Ghost Royalama (white)", ItemClassification.progression),
    ItemData(0x1F28007B, "Ghost Royalama (Black)", ItemClassification.progression),
    ItemData(0x1F28007C, "Foil Ghost Royalama (white)", ItemClassification.progression),
    ItemData(0x1F28007D, "Foil Ghost Royalama (Black)", ItemClassification.progression),
    ItemData(0x1F28007E, "Ghost Dracunix (white)", ItemClassification.progression),
    ItemData(0x1F28007F, "Ghost Dracunix (Black)", ItemClassification.progression),
    ItemData(0x1F280080, "Foil Ghost Dracunix (white)", ItemClassification.progression),
    ItemData(0x1F280081, "Foil Ghost Dracunix (Black)", ItemClassification.progression),
    ItemData(0x1F280082, "Ghost Magnoria (white)", ItemClassification.progression),
    ItemData(0x1F280083, "Ghost Magnoria (Black)", ItemClassification.progression),
    ItemData(0x1F280084, "Foil Ghost Magnoria (white)", ItemClassification.progression),
    ItemData(0x1F280085, "Foil Ghost Magnoria (Black)", ItemClassification.progression),
    ItemData(0x1F280086, "Ghost Hydroid (white)", ItemClassification.progression),
    ItemData(0x1F280087, "Ghost Hydroid (Black)", ItemClassification.progression),
    ItemData(0x1F280088, "Foil Ghost Hydroid (white)", ItemClassification.progression),
    ItemData(0x1F280089, "Foil Ghost Hydroid (Black)", ItemClassification.progression),
    ItemData(0x1F28008A, "Ghost Drakon (white)", ItemClassification.progression),
    ItemData(0x1F28008B, "Ghost Drakon (Black)", ItemClassification.progression),
    ItemData(0x1F28008C, "Foil Ghost Drakon (white)", ItemClassification.progression),
    ItemData(0x1F28008D, "Foil Ghost Drakon (Black)", ItemClassification.progression),
    ItemData(0x1F28008E, "Ghost Bogon (white)", ItemClassification.progression),
    ItemData(0x1F28008F, "Ghost Bogon (Black)", ItemClassification.progression),
    ItemData(0x1F280090, "Foil Ghost Bogon (white)", ItemClassification.progression),
    ItemData(0x1F280091, "Foil Ghost Bogon (Black)", ItemClassification.progression),
    ItemData(0x1F280092, "Ghost Hydron (white)", ItemClassification.progression),
    ItemData(0x1F280093, "Ghost Hydron (Black)", ItemClassification.progression),
    ItemData(0x1F280094, "Foil Ghost Hydron (white)", ItemClassification.progression),
    ItemData(0x1F280095, "Foil Ghost Hydron (Black)", ItemClassification.progression),
    ItemData(0x1F280096, "Ghost Raizon (white)", ItemClassification.progression),
    ItemData(0x1F280097, "Ghost Raizon (Black)", ItemClassification.progression),
    ItemData(0x1F280098, "Foil Ghost Raizon (white)", ItemClassification.progression),
    ItemData(0x1F280099, "Foil Ghost Raizon (Black)", ItemClassification.progression),
    ItemData(0x1F28009A, "Ghost Lucadence (white)", ItemClassification.progression),
    ItemData(0x1F28009B, "Ghost Lucadence (Black)", ItemClassification.progression),
    ItemData(0x1F28009C, "Foil Ghost Lucadence (white)", ItemClassification.progression),
    ItemData(0x1F28009D, "Foil Ghost Lucadence (Black)", ItemClassification.progression),
    ItemData(0x1F28009E, "Ghost Jigajawr (white)", ItemClassification.progression),
    ItemData(0x1F28009F, "Ghost Jigajawr (Black)", ItemClassification.progression),
    ItemData(0x1F2800A0, "Foil Ghost Jigajawr (white)", ItemClassification.progression),
    ItemData(0x1F2800A1, "Foil Ghost Jigajawr (Black)", ItemClassification.progression),
    ItemData(0x1F2800A2, "Ghost Jacktern (white)", ItemClassification.progression),
    ItemData(0x1F2800A3, "Ghost Jacktern (Black)", ItemClassification.progression),
    ItemData(0x1F2800A4, "Foil Ghost Jacktern (white)", ItemClassification.progression),
    ItemData(0x1F2800A5, "Foil Ghost Jacktern (Black)", ItemClassification.progression),
    ItemData(0x1F2800A6, "Ghost GigatronX (white)", ItemClassification.progression),
    ItemData(0x1F2800A7, "Ghost GigatronX (Black)", ItemClassification.progression),
    ItemData(0x1F2800A8, "Foil Ghost GigatronX (white)", ItemClassification.progression),
    ItemData(0x1F2800A9, "Foil Ghost GigatronX (Black)", ItemClassification.progression),
    ItemData(0x1F2800AA, "Ghost Clawcifear (white)", ItemClassification.progression),
    ItemData(0x1F2800AB, "Ghost Clawcifear (Black)", ItemClassification.progression),
    ItemData(0x1F2800AC, "Foil Ghost Clawcifear (white)", ItemClassification.progression),
    ItemData(0x1F2800AD, "Foil Ghost Clawcifear (Black)", ItemClassification.progression),
    ItemData(0x1F2800AE, "Ghost Katengu (white)", ItemClassification.progression),
    ItemData(0x1F2800AF, "Ghost Katengu (Black)", ItemClassification.progression),
    ItemData(0x1F2800B0, "Foil Ghost Katengu (white)", ItemClassification.progression),
    ItemData(0x1F2800B1, "Foil Ghost Katengu (Black)", ItemClassification.progression),
]
expA = ItemData(0x1F2800C0, "Progressive Shop Expansion A", ItemClassification.progression,30)
expB = ItemData(0x1F2800C1, "Progressive Shop Expansion B", ItemClassification.useful,14)

full_item_list: List[ItemData] = [*itemList, *progressivelist, *junklist, *traplist, *ghostlist,expA, expB]

license_item_list: List[ItemData] = [*itemList, *progressivelist,expA, expB]