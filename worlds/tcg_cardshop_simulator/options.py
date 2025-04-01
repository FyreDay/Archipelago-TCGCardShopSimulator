from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions,OptionGroup, Range, Toggle, DefaultOnToggle


class Goal(Choice):
    """The victory condition for your run. Stuff after the goal level/expasion level req will not be shuffled. 
    Collect Ghosts hides all ghost cards in locations to be found"""

    display_name = "Goal"
    option_shopExpansion = 0
    option_level = 1
    option_collect_Ghosts = 2
    default = 0


class ShopExpansionGoal(Range):
    """
    If on Shop Expansion Goal, What Shop expansion is your goal
    """

    display_name = "ShopExpansionGoal"
    range_start = 1
    range_end = 30
    default = 8

class LevelGoal(Range):
    """
    If on Level Goal, What level are you working to?
    """

    display_name = "LevelGoal"
    range_start = 1
    range_end = 100
    default = 20

class GhostGoalAmount(Range):
    """
    If on Level Goal, What level are you working to?
    """

    display_name = "GhostGoalAmount"
    range_start = 1
    range_end = 80
    default = 40

class CardSanity(Choice):
    """
    Enables new Cards from that rarity and below to be checks
    """
    display_name = "CardSanity"
    option_disabled = 0
    option_basic = 1
    option_rare = 2
    option_epic = 3
    option_legendary = 4
    option_destiny_basic = 5
    option_destiny_rare = 6
    option_destiny_epic = 7
    option_destiny_legendary = 8
    default = 0

class TrapFill(Range):
    """
    Determines the percentage of the junk fill which is filled with traps.
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 80
    default = 0



@dataclass
class tcg_cardshop_simulator_option_groups(PerGameCommonOptions):
    OptionGroup("Goal Options", [
        Goal,
        ShopExpansionGoal,
        LevelGoal,
        GhostGoalAmount
    ]),
    OptionGroup("Sanity", [
        CardSanity
    ]),
    OptionGroup("Traps", [
        TrapFill
    ])
    
@dataclass
class TCGSimulatorOptions(PerGameCommonOptions):
    goal: Goal
    shop_expansion_goal: ShopExpansionGoal
    level_goal: LevelGoal
    ghost_goal_amount: GhostGoalAmount
    card_sanity: CardSanity
    trap_fill: TrapFill
