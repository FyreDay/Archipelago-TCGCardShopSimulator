
import typing
import string
from typing import ClassVar, Dict, List, Set, TextIO
import math
import dataclasses
from Options import OptionError
#SonicHeroesItem, item_name_to_id, create_items, junk_weights
from worlds.AutoWorld import WebWorld, World

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Region
from .options import *
from .regions import *
from .locations import *
from .items import *
from .rules import *

class TCGSimulatorWeb(WebWorld):
    theme = "partyTime"

    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the TCG Card Shop Simulator randomizer connected to an Archipelago Multiworld.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["FyreDay"]
    )

    tutorials = [setup_en]

class TCGSimulatorWorld(World):

    game = "TCG Card Shop Simulator"
    web = TCGSimulatorWeb()
    options_dataclass = TCGSimulatorOptions
    options: TCGSimulatorOptions

    option_groups = tcg_cardshop_simulator_option_groups

    item_name_to_id: ClassVar[Dict[str, int]] = {item.itemName: item.code for item in full_item_list}
    location_name_to_id: ClassVar[Dict[str, int]] = full_location_dict


    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

    def generate_early(self) -> None:
        generate_locations(self)

    def create_regions(self):
        create_regions(self)

    def create_item(self, item: str) -> TCGSimulatorItem:
        if item in junk_weights.keys():
            return TCGSimulatorItem(item, ItemClassification.filler, self.item_name_to_id[item], self.player)
        return TCGSimulatorItem(item, ItemClassification.progression, self.item_name_to_id[item], self.player)
    
    def create_items(self):
        create_items(self)
    
    def set_rules(self):
        set_rules(self)

    
    def fill_slot_data(self) -> id:
         return {
            "ModVersion": "0.0.1",
            "Goal": self.options.goal.value,
            "ShopExpansionGoal": self.options.shop_expansion_goal.value, 
            "LevelGoal": self.options.level_goal.value,
            "CardSanity": self.options.card_sanity.value,
            "GhostGoalAmount": self.options.ghost_goal_amount.value,
            "BetterTrades": self.options.better_trades.value,
            "TrapFill": self.options.trap_fill.value,
        }