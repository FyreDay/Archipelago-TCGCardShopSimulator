from BaseClasses import LocationProgressType, CollectionState
from .items import *
from .locations import *


def has_card_pack(world, state, rarity):
    return state.has(f"Progressive {rarity} Pack", world.player) or state.has(f"Progressive {rarity} Box", world.player)

def get_rules(world):
    rules = {
        "sell_locations": {
            "Basic Card Pack":
                lambda state:
                has_card_pack(world, state, "Basic Card"),
            "Basic Card Box":
                lambda state:
                state.has("Progressive Basic Card Box", world.player),
            "Rare Card Pack":
                lambda state:
                has_card_pack(world, state, "Rare Card"),
            "Rare Card Box":
                lambda state:
                state.has("Progressive Rare Card Box", world.player),
            "Epic Card Pack":
                lambda state:
                has_card_pack(world, state, "Epic Card"),
            "Epic Card Box":
                lambda state:
                state.has("Progressive Epic Card Box", world.player),
            "Legendary Card Pack":
                lambda state:
                has_card_pack(world, state, "Legendary Card"),
            "Legendary Card Box":
                lambda state:
                state.has("Progressive Legendary Card Box", world.player),
            "Fire Battle Deck":
                lambda state:
                state.has("Fire Battle Deck", world.player),
            "Earth Battle Deck":
                lambda state:
                state.has("Earth Battle Deck", world.player),
            "Water Battle Deck":
                lambda state:
                state.has("Water Battle Deck", world.player),
            "Wind Battle Deck":
                lambda state:
                state.has("Wind Battle Deck", world.player),
            "Basic Destiny Pack":
                lambda state:
                has_card_pack(world, state, "Basic Destiny"),
            "Basic Destiny Box":
                lambda state:
                state.has("Progressive Basic Destiny Box", world.player),
            "Rare Destiny Pack":
                lambda state:
                has_card_pack(world, state, "Rare Destiny"),
            "Rare Destiny Box":
                lambda state:
                state.has("Progressive Rare Destiny Box", world.player),
            "Epic Destiny Pack":
                lambda state:
                has_card_pack(world, state, "Epic Destiny"),
            "Epic Destiny Box":
                lambda state:
                state.has("Progressive Epic Destiny Box", world.player),
            "Legendary Destiny Pack":
                lambda state:
                has_card_pack(world, state, "Legendary Destiny"),
            "Legendary Destiny Box":
                lambda state:
                state.has("Progressive Legendary Destiny Box", world.player),
            "Fire Destiny Deck":
                lambda state:
                state.has("Fire Destiny Deck", world.player),
            "Earth Destiny Deck":
                lambda state:
                state.has("Earth Destiny Deck", world.player),
            "Water Destiny Deck":
                lambda state:
                state.has("Water Destiny Deck", world.player),
            "Wind Destiny Deck":
                lambda state:
                state.has("Wind Destiny Deck", world.player),
            "Cleanser":
                lambda state:
                state.has("Progressive Cleanser", world.player),
            "Card Sleeves (Clear)":
                lambda state:
                state.has("Card Sleeves (Clear)", world.player),
            "Card Sleeves (Tetramon)":
                lambda state:
                state.has("Card Sleeves (Tetramon)", world.player),
            "D20 Dice Red":
                lambda state:
                state.has("D20 Dice Red", world.player),
            "D20 Dice Blue":
                lambda state:
                state.has("D20 Dice Blue", world.player),
            "D20 Dice Black":
                lambda state:
                state.has("D20 Dice Black", world.player),
            "D20 Dice White":
                lambda state:
                state.has("D20 Dice White", world.player),
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
            "Deck Box Red":
                lambda state:
                state.has("Progressive Deck Box Red", world.player),
            "Deck Box Green":
                lambda state:
                state.has("DProgressive eck Box Green", world.player),
            "Deck Box Blue":
                lambda state:
                state.has("Progressive Deck Box Blue", world.player),
            "Deck Box Yellow":
                lambda state:
                state.has("Progressive Deck Box Yellow", world.player),
            "Collection Book":
                lambda state:
                state.has("Collection Book", world.player),
            "Premium Collection Book":
                lambda state:
                state.has("Premium Collection Book", world.player),
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
            "Manga 1":
                lambda state:
                state.has("Manga 1", world.player),
            "Manga 2":
                lambda state:
                state.has("Manga 2", world.player),
            "Manga 3":
                lambda state:
                state.has("Manga 3", world.player),
            "Manga 4":
                lambda state:
                state.has("Manga 4", world.player),
            "Manga 5":
                lambda state:
                state.has("Manga 5", world.player),
            "Manga 6":
                lambda state:
                state.has("Manga 6", world.player),
            "Manga 7":
                lambda state:
                state.has("Manga 7", world.player),
            "Manga 8":
                lambda state:
                state.has("Manga 8", world.player),
            "Manga 9":
                lambda state:
                state.has("Manga 9", world.player),
            "Manga 10":
                lambda state:
                state.has("Manga 10", world.player),
            "Manga 11":
                lambda state:
                state.has("Manga 11", world.player),
            "Manga 12":
                lambda state:
                state.has("Manga 12", world.player),
            "Pigni Plushie":
                lambda state:
                state.has("Pigni Plushie", world.player),
            "Nanomite Plushie":
                lambda state:
                state.has("Nanomite Plushie", world.player),
            "Minstar Plushie":
                lambda state:
                state.has("Minstar Plushie", world.player),
            "Nocti Plushie":
                lambda state:
                state.has("Nocti Plushie", world.player),
            "Burpig Figurine":
                lambda state:
                state.has("Burpig Figurine", world.player),
            "Decimite Figurine":
                lambda state:
                state.has("Decimite Figurine", world.player),
            "Trickstar Figurine":
                lambda state:
                state.has("Trickstar Figurine", world.player),
            "Lunight Figurine":
                lambda state:
                state.has("Lunight Figurine", world.player),
            "Inferhog Figurine":
                lambda state:
                state.has("Inferhog Figurine", world.player),
            "Meganite Figurine":
                lambda state:
                state.has("Meganite Figurine", world.player),
            "Princestar Figurine":
                lambda state:
                state.has("Princestar Figurine", world.player),
            "Vampicant Figurine":
                lambda state:
                state.has("Vampicant Figurine", world.player),
            "Blazoar Plushie":
                lambda state:
                state.has("Blazoar Plushie", world.player),
            "Giganite Statue":
                lambda state:
                state.has("Giganite Statue", world.player),
            "Kingstar Plushie":
                lambda state:
                state.has("Kingstar Plushie", world.player),
            "Dracunix Figurine":
                lambda state:
                state.has("Dracunix Figurine", world.player),
            "Bonfiox Plushie":
                lambda state:
                state.has("Bonfiox Plushie", world.player),
            "Drilceros Action Figure":
                lambda state:
                state.has("Drilceros Action Figure", world.player),
            "ToonZ Plushie":
                lambda state:
                state.has("ToonZ Plushie", world.player),
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
                state.has("Playmat Yellow", world.player),
            "Pocket Pages":
                lambda state:
                state.has("Pocket Pages", world.player),
            "Card Holder":
                lambda state:
                state.has("Card Holder", world.player),
            "Collectors Album":
                lambda state:
                state.has("Collectors Album", world.player),
            "Playmat (Dracunix2)":
                lambda state:
                state.has("Playmat (Dracunix2)", world.player),
            "Playmat (GigatronX)":
                lambda state:
                state.has("Playmat (GigatronX)", world.player),
            "Playmat (Katengu Black)":
                lambda state:
                state.has("Playmat (Katengu Black)", world.player),
            "Playmat (Katengu White)":
                lambda state:
                state.has("Playmat (Katengu White)", world.player),
        },
        "entrances": {
            "Level 5":
                lambda state:
                state.has_group_unique("licenses", world.player, 1 * world.options.required_licenses.value),
            "Level 10":
                lambda state:
                 state.has_group_unique("licenses", world.player, 2 * world.options.required_licenses.value),
            "Level 15":
                lambda state:
                  state.has_group_unique("licenses", world.player, 3 * world.options.required_licenses.value),
            "Level 20":
                lambda state:
                 state.has_group_unique("licenses", world.player, 4 * world.options.required_licenses.value),
            "Level 25":
                lambda state:
                state.has_group_unique("licenses", world.player, 5 * world.options.required_licenses.value),
            "Level 30":
                lambda state:
                state.has_group_unique("licenses", world.player, 6 * world.options.required_licenses.value),
            "Level 35":
                lambda state:
                state.has_group_unique("licenses", world.player, 7 * world.options.required_licenses.value),
            "Level 40":
                lambda state:
                state.has_group_unique("licenses", world.player, 8 * world.options.required_licenses.value),
            "Level 45":
                lambda state:
                state.has_group_unique("licenses", world.player, 9 * world.options.required_licenses.value),
            "Level 50":
                lambda state:
                state.has_group_unique("licenses", world.player, 10 * world.options.required_licenses.value),
            "Level 55":
                lambda state:
                state.has_group_unique("licenses", world.player, 11 * world.options.required_licenses.value),
            "Level 60":
                lambda state:
                state.has_group_unique("licenses", world.player, 12 * world.options.required_licenses.value),
            "Level 65":
                lambda state:
                state.has_group_unique("licenses", world.player, 13 * world.options.required_licenses.value),
            "Level 70":
                lambda state:
                state.has_group_unique("licenses", world.player, 1 * world.options.required_licenses.value),
            "Level 75":
                lambda state:
                state.has_group_unique("licenses", world.player, 15 * world.options.required_licenses.value),
            "Level 80":
                lambda state:
                state.has_group_unique("licenses", world.player, 16 * world.options.required_licenses.value),
            "Level 85":
                lambda state:
                state.has_group_unique("licenses", world.player, 17 * world.options.required_licenses.value),
            "Level 90":
                lambda state:
                state.has_group_unique("licenses", world.player, 18 * world.options.required_licenses.value),
            "Level 95":
                lambda state:
                state.has_group_unique("licenses", world.player, 19 * world.options.required_licenses.value),
            "Level 100":
                lambda state:
                state.has_group_unique("licenses", world.player, 20 * world.options.required_licenses.value),
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
            "Play Table Found":
                lambda state:
                state.has("Play Table", world.player),
            "Sell Tetramon":
                lambda state:
                has_card_pack(world, state, "Basic Card") or has_card_pack(world, state, "Rare Card")
                or has_card_pack(world, state, "Epic Card") or has_card_pack(world, state, "Legendary Card"),
            "Sell Destiny":
                lambda state:
                has_card_pack(world, state, "Basic Destiny") or has_card_pack(world, state, "Rare Destiny")
                or has_card_pack(world, state, "Epic Destiny") or has_card_pack(world, state, "Legendary Destiny"),

        }
    }
    return rules


def set_rules(world):

    rules_lookup = get_rules(world)

    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            match = re.search(r'Level (\d+)', entrance_name)
            if match and world.options.max_level.value <= int(match.group(1)):
                continue
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError as e:
            print(f"Entrance Key error, {e}")
            pass

    for location_name, rule in rules_lookup["sell_locations"].items():
        try:
            location_id = world.location_name_to_id.get(f"Sell 1 Box of {location_name}")
            if (location_id in world.pg1_licenses or
                    location_id in world.pg2_licenses or
                    location_id in world.pg3_licenses or
                    location_id in world.tt_licenses) and (location_id not in world.starting_item_ids):
                for n in range(1, world.options.sell_check_amount.value + 1):
                    world.get_location(f"Sell {n} {"Boxes" if n>1 else "Box"} of {location_name}").access_rule = rule
        except KeyError as e:
            print(f"Sell Key error, {e}")
            pass

    for expansion in Expansion:
        for i in range(world.options.sell_card_check_count.value):
            name = f"Sell {expansion.name} cards #{i + 1}"
            try:
                loc = world.get_location(name)
            except KeyError:
                continue
            world.get_location(name).access_rule = lambda state: state.has(
                "Progressive Card Table", world.player, 1)

    if world.options.goal.value == 0:
        world.multiworld.get_location(f"Level {world.options.max_level.value}", world.player).place_locked_item(
            TCGSimulatorItem("Victory", ItemClassification.progression, None, world.player))
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)

    if world.options.goal.value == 1:
        raise OptionError("Goal 1 Not Implemented")

    if world.options.goal.value == 2:
        lambdas = {}
        for bagsize, amount in world.ghost_item_counts.items():
            plural = "s" if bagsize > 1 else ""
            item_name = f"{bagsize} Ghost Card{plural}"
            lambdas[bagsize] = (lambda state, item=item_name, count=amount: state.has(item, world.player, count))
        world.multiworld.completion_condition[world.player] = lambda state: all(check(state) for check in lambdas.values())