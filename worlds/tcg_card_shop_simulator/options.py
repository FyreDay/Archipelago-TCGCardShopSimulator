from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions,OptionGroup, DeathLink,Range, Toggle, DefaultOnToggle

class MaxLevel(Range):
    """
    What is the maximum level you would like to reach?
    This will be rounded up to the nearest multiple of 5

    The host can limit this setting to 50 for syncs
    """

    display_name = "Max Level"
    range_start = 10
    range_end = 100
    default = 20

class RequiredLicensesPercentage(Range):
    """
    How many More Product Licenses are required to unlock the next 5 levels? low numbers are easier.

    Every 5 levels, you will stop leveling up until you have a certain number of licenses unlocked for items that you can sell.
    Every 5 levels how many more product licenses do you need to be sent in order to progress?

    """

    display_name = "Required licenses"
    range_start = 0
    range_end = 10
    default = 5


class Goal(Choice):
    """
    The victory condition for your run.
    Collection Builder is about getting your card collection to a collected percentage
    Sell Ghost Cards hides ghost cards in locations to be found
    """

    display_name = "Goal"
    option_reach_max_level = 0
    option_collection_builder = 1
    option_sell_ghost_cards = 2
    default = 0

class GhostGoalAmount(Range):
    """
    If on Ghost cards Goal, How many do you need to sell?
    This causes ghost card items to be seeded in the multiworld
    """

    display_name = "Ghost Goal Amount"
    range_start = 1
    range_end = 80
    default = 40

class CollectionGoalPercentage(Range):
    """
    If on Collection Goal, What percentage of the collection do you need to collect?
    the host can limit this setting to 50%
    """

    display_name = "Collection Goal Percentage"
    range_start = 10
    range_end = 100
    default = 20

class StartWithWorker(Choice):
    """
    Choose a worker to start with.
    Reminder, you still have to pay their salary every day
    """
    display_name = "Starting Worker"
    option_none = 0
    option_zachery = 1
    option_terence = 2
    option_dennis = 3
    option_clark = 4
    option_angus = 5
    option_benji = 6
    option_lauren = 7
    option_axel = 8
    default = 0

class AutoRenovate(Toggle):
    """
    This automatically renovates shop expansions for you when you receive expansions. Never look at RENO BIGG again!
    """
    display_name = "Auto Renovate"

class ExtraStartingItemChecks(Range):
    """
    This setting stops generation failures from very limited starts.
    The maximum checks per item are capped to 16 regardless of this setting
    """

    display_name = "Extra Starting Item Checks"
    range_start = 5
    range_end = 8
    default = 5

class SellCheckAmount(Range):
    """
    Selling all of a Box of an ordered product is a check. How many sell checks will each product have?

    The host can limit this to 8
    """
    display_name = "Sell Check Amount"
    range_start = 2
    range_end = 16
    default = 2

class CardOpeningCheckDifficulty(Choice):
    """
    Open Cards to complete goals for checks. How hard do you want these goals to be?

    examples of checks:
        "First common foil card" is an easy check.
        "open 20 gold border foils from legendary packs" is medium
        "Collect all 12 versions of one card" is hard
        "Collect all full arts from a pack" is impossible
    """
    display_name = "Card Opening Check Difficulty"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_impossible = 3
    default = 1

class CardSanity(Choice):
    """
    Enables each card to be a unique check. This follows your card opening difficulty set above. Each version adds 242 checks

    Easy : Basic cards are checks
    medium: Basic, 1st Edition, and Silver Edition cards are checks
    hard: basic, 1st Edition, Silver Edition, gold edition are checks
    impossible: All cards are checks

    Normally foils will count the same as the non-foil card. "Unique foils" will cause the foil version to be a unique check

    At Card Opening Difficulty "Impossible" this adds 1452 checks. doubled to 2904 if on foil setting
    """
    display_name = "Card Sanity"
    option_disabled = 0
    option_enabled = 1
    option_uniqueFoils = 2
    default = 0

class CardSellingCheckDifficulty(Choice):
    """
    Sell Cards to complete goals for checks. How hard do you want these goals to be?

    examples of checks:
        "Sell 20 commons" is an easy check.
        "Sell 100 foils" is medium
        "sell 1000 cards" is hard
        "sell 50 foil full arts" is impossible
    """
    display_name = "Card Selling Check Difficulty"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_impossible = 3
    default = 1

class CardGradingCheckDifficulty(Choice):
    """
    Grade Cards to complete goals for checks. How hard do you want these goals to be?

    examples of checks:
    """
    display_name = "Card Grading Check Difficulty"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_impossible = 3
    default = 1

class PlayTableChecks(Range):
    """
    How many checks are there for each format on playtables?
    """
    display_name = "Number of PlayTable Checks"
    range_start = 0
    range_end = 50
    default = 10

class DecoShop(Toggle):
    """
    Turns the Deco Screen into a shop you can buy AP items in
    """
    display_name = "Decoration Shop"


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
    If your goal is Level goal, these are disabled
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

class ProgressiveCustomerWealth(Range):
    """
    Determines the percentage of Filler
    increases how much money your customers have
    """
    display_name = "Progressive Customer Wealth"
    range_start = 0
    range_end = 100
    default = 25

class CardLuck(Range):
    """
    Determines the percentage of Filler
    increases your chances to find better cards in packs
    """
    display_name = "Card Luck"
    range_start = 0
    range_end = 100
    default = 25

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

class MarketChangeTrap(Range):
    """
    Causes prices to randomize
    Determines the percentage of Traps are Market Change Traps.
    Traps must be enabled for this to have any effect.
    """
    display_name = "Market Change Trap"
    range_start = 0
    range_end = 100
    default = 50
class CurrencyTrap(Range):
    """
    Causes Currency to Randomize
    Determines the percentage of Traps are Currency Traps.
    Traps must be enabled for this to have any effect.
    """
    display_name = "Currency Trap"
    range_start = 0
    range_end = 100
    default = 0

class DecreaseCardLuckTrap(Range):
    """
    Lowers your card luck
    Determines the percentage of Traps are Decrease Card Luck Traps.
    Traps must be enabled for this to have any effect.
    """
    display_name = "Reduce Card Luck Trap"
    range_start = 0
    range_end = 100
    default = 20

class CreditCardFailureTrap(Range):
    """
    Credit cards fail to work for a little while
    Determines the percentage of Traps are Credit Card Failure Traps.
    Traps must be enabled for this to have any effect.
    """
    display_name = "Credit Card Failure Trap"
    range_start = 0
    range_end = 100
    default = 50

@dataclass
class tcg_cardshop_simulator_option_groups(PerGameCommonOptions):
    OptionGroup("Goal Options", [
        MaxLevel,
        LicensesPerLevelGroup,
        RequiredLicensesPercentage,
        Goal,
        # CollectionGoalPercentage,
        GhostGoalAmount,
    ]),
    OptionGroup("General", [
        StartWithWorker,
        AutoRenovate,
        ExtraStartingItemChecks,
        SellCheckAmount,
        ChecksPerPack,
        CardCollectPercentage,
        PlayTableChecks,
        GamesPerCheck,
        NumberOfSellCardChecks,
        SellCardsPerCheck,
        AllLevelsAreChecks,
        # DecoShop
    ]),
    OptionGroup("Sanity", [
        CardSanity,
        FoilInSanity,
        BorderInSanity
    ]),
    OptionGroup("Death Link", [
        DeathLink
    ])
    OptionGroup("Filler and Traps", [
        MoneyBags,
        XpBoosts,
        RandomCard,
        RandomNewCard,
        ProgressiveCustomerWealth,
        CardLuck,
        TrapFill,
        StinkTrap,
        PoltergeistTrap,
        CreditCardFailureTrap,
        MarketChangeTrap,
        CurrencyTrap,
        DecreaseCardLuckTrap
    ])
    
@dataclass
class TCGSimulatorOptions(PerGameCommonOptions):
    max_level: MaxLevel
    licenses_per_region: LicensesPerLevelGroup
    required_licenses: RequiredLicensesPercentage
    goal: Goal
    # collection_goal_percentage: CollectionGoalPercentage
    ghost_goal_amount: GhostGoalAmount
    start_with_worker: StartWithWorker
    auto_renovate: AutoRenovate
    extra_starting_item_checks: ExtraStartingItemChecks
    sell_check_amount: SellCheckAmount
    checks_per_pack: ChecksPerPack
    card_collect_percent: CardCollectPercentage
    play_table_checks: PlayTableChecks
    games_per_check: GamesPerCheck
    sell_card_check_count: NumberOfSellCardChecks
    sell_cards_per_check: SellCardsPerCheck
    all_level_checks: AllLevelsAreChecks
    # deco_shop: DecoShop
    deathlink: DeathLink
    card_sanity: CardSanity
    foil_sanity: FoilInSanity
    border_sanity: BorderInSanity
    money_bags: MoneyBags
    xp_boosts: XpBoosts
    random_card: RandomCard
    random_new_card: RandomNewCard
    customer_wealth: ProgressiveCustomerWealth
    card_luck: CardLuck
    trap_fill: TrapFill
    stink_trap: StinkTrap
    poltergeist_trap: PoltergeistTrap
    credit_card_failure_trap: CreditCardFailureTrap
    market_change_trap: MarketChangeTrap
    currency_trap: CurrencyTrap
    decrease_card_luck_trap: DecreaseCardLuckTrap
