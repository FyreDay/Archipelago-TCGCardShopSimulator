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
    range_start = 10
    range_end = 30
    default = 10

class LevelGoal(Range):
    """
    If on Level Goal, What level are you working to?
    """

    display_name = "LevelGoal"
    range_start = 30
    range_end = 100
    default = 30

class GhostGoalAmount(Range):
    """
    If on Ghost cards Goal, How many do you need to find?
    """

    display_name = "GhostGoalAmount"
    range_start = 1
    range_end = 80
    default = 40

class BetterTrades(DefaultOnToggle):
    """
    Makes Customers always have New cards. If card sanity is on, the cards will always be Checks
    """
    display_name = "Better Trades"

class CardSanity(Choice):
    """
    Enables new Cards from that rarity and below to be checks. For each level you add 360 locations. at legendary it is 1452 locations
    Basic is recommended if you wish this to be on
    """
    display_name = "Card Sanity"
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

class MoneyBags(Range):
    """
    Determines the percentage of Filler contain money
    """
    display_name = "Money Filler"
    range_start = 0
    range_end = 100
    default = 50

class XpBoosts(Range):
    """
    Determines the percentage of Filler contain Shop Xp
    """
    display_name = "XP Filler"
    range_start = 0
    range_end = 100
    default = 50

class RandomCard(Range):
    """
    Determines the percentage of Filler are random cards. Watch out for repeats!
    """
    display_name = "Random Card"
    range_start = 0
    range_end = 100
    default = 50

class RandomNewCard(Range):
    """
    Determines the percentage of Filler are random cards that will always be new
    if card sanity is checked, these cards will always be a check
    """
    display_name = "New Card"
    range_start = 0
    range_end = 100
    default = 50

class TrapFill(Range):
    """
    Determines the percentage of the junk fill which is filled with traps.
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 80
    default = 0

class StinkTrap(Range):
    """
    You know what this does. Stinky.
    Determines the percentage of Traps are Stink Traps.
    Traps must be enabled for this to have any effect.
    """
    display_name = "Stink Trap"
    range_start = 0
    range_end = 100
    default = 50

class PoltergeistTrap(Range):
    """
    Something is messing with the lights
    Determines the percentage of Traps are Poltergeist Traps.
    Traps must be enabled for this to have any effect.
    """
    display_name = "Poltergeist Trap"
    range_start = 0
    range_end = 100
    default = 50


@dataclass
class tcg_cardshop_simulator_option_groups(PerGameCommonOptions):
    OptionGroup("Goal Options", [
        Goal,
        ShopExpansionGoal,
        LevelGoal,
        GhostGoalAmount
    ]),
    OptionGroup("General", [
        BetterTrades
    ]),
    OptionGroup("Sanity", [
        CardSanity
    ]),
    OptionGroup("Filler and Traps", [
        MoneyBags,
        XpBoosts,
        RandomCard,
        RandomNewCard,
        TrapFill,
        StinkTrap,
        PoltergeistTrap
    ])
    
@dataclass
class TCGSimulatorOptions(PerGameCommonOptions):
    goal: Goal
    shop_expansion_goal: ShopExpansionGoal
    level_goal: LevelGoal
    ghost_goal_amount: GhostGoalAmount
    better_trades: BetterTrades
    card_sanity: CardSanity
    money_bags: MoneyBags
    xp_boosts: XpBoosts
    random_card: RandomCard
    random_new_card: RandomNewCard
    trap_fill: TrapFill
    stink_trap: StinkTrap
    poltergeist_trap: PoltergeistTrap
