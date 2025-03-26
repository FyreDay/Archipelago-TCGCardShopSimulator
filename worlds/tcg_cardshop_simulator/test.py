def format_text_file(input_file, output_file, start_id=0x1F2800F0):
    monster_type = {
    1: "PiggyA",
    2: "PiggyB",
    3: "PiggyC",
    4: "PiggyD",
    5: "FoxA",
    6: "FoxB",
    7: "FoxC",
    8: "FoxD",
    9: "GolemA",
    10: "GolemB",
    11: "GolemC",
    12: "GolemD",
    13: "TreeA",
    14: "TreeB",
    15: "TreeC",
    16: "TreeD",
    17: "StarfishA",
    18: "StarfishB",
    19: "StarfishC",
    20: "StarfishD",
    21: "ShellyA",
    22: "ShellyB",
    23: "ShellyC",
    24: "ShellyD",
    25: "BugA",
    26: "BugB",
    27: "BugC",
    28: "BugD",
    29: "BatA",
    30: "BatB",
    31: "BatC",
    32: "BatD",
    33: "Skull",
    34: "Beetle",
    35: "Bear",
    36: "Jellyfish",
    37: "Wisp",
    38: "MummyMan",
    39: "FlowerA",
    40: "FlowerB",
    41: "FlowerC",
    42: "FlowerD",
    43: "WeirdBirdA",
    44: "FireSpirit",
    45: "Angez",
    46: "Mosquito",
    47: "HydraA",
    48: "HydraB",
    49: "HydraC",
    50: "HydraD",
    51: "DragonFire",
    52: "DragonEarth",
    53: "DragonWater",
    54: "DragonThunder",
    55: "Turtle",
    56: "FireWolfA",
    57: "FireWolfB",
    58: "FireWolfC",
    59: "FireWolfD",
    60: "FishA",
    61: "FishB",
    62: "FishC",
    63: "FishD",
    64: "HalloweenA",
    65: "HalloweenB",
    66: "HalloweenC",
    67: "HalloweenD",
    68: "TronA",
    69: "TronB",
    70: "TronC",
    71: "TronD",
    72: "LobsterA",
    73: "LobsterB",
    74: "LobsterC",
    75: "LobsterD",
    76: "FireBirdA",
    77: "FireBirdB",
    78: "FireBirdC",
    79: "SerpentA",
    80: "SerpentB",
    81: "SerpentC",
    82: "CloudA",
    83: "CloudB",
    84: "CloudC",
    85: "EmeraldA",
    86: "EmeraldB",
    87: "EmeraldC",
    88: "Crystalmon",
    89: "ElecDragon",
    90: "CrabA",
    91: "CrabB",
    92: "FireUmbrellaDragon",
    93: "Lanternmon",
    94: "SeedBugA",
    95: "SeedBugB",
    96: "SeedBugC",
    97: "NinjaBirdA",
    98: "NinjaBirdB",
    99: "NinjaBirdC",
    100: "NinjaBirdD",
    101: "NinjaCrowC",
    102: "NinjaCrowD",
    103: "MuffinTreeA",
    104: "MuffinTreeB",
    105: "MuffinTreeC",
    106: "SharkFishA",
    107: "SharkFishB",
    108: "SharkFishC",
    109: "FireGeckoA",
    110: "FireGeckoB",
    111: "EarthDino",
    112: "FireChickenA",
    113: "FireChickenB",
    114: "SeahorseA",
    115: "SeahorseB",
    116: "SeahorseC",
    117: "SeahorseD",
    118: "SlimeA",
    119: "SlimeB",
    120: "SlimeC",
    121: "SlimeD",
}
    
    card_border = {
        0: 'Base',
        1: 'FirstEdition',
        2: 'Silver',
        3: 'Gold',
        4: 'EX',
        5: 'FullArt'
    }
    
    card_expansion = {
        0: 'Tetramon',
        1: 'Destiny'
    }
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    with open(output_file, 'w', encoding='utf-8') as outfile:

        locs_amount = 0

        for index, line in enumerate(lines):
            formatted_line = f"\"{line.strip()}\": 0x{start_id + index:X},\n"
            outfile.write(formatted_line)
            locs_amount = index
        
        for i in range(114):
            formatted_location = f"\"Level {i+2}\": 0x{start_id +locs_amount+ 1+i:X},\n"
            outfile.write(formatted_location)
        
        unique_id = start_id + len(lines)
        for expansion in card_expansion:
            for border in card_border:
                for foil in [0, 1]:
                    for monster in monster_type:
                        hex_id = 0x1F290000 | (expansion << 12) | (border << 8) | (foil << 7) | monster
                        formatted_line = f"\"{monster_type[monster]}_{card_border[border]}_{'Foil' if foil else 'NonFoil'}_{card_expansion[expansion]}\": 0x{hex_id:X},\n"
                        outfile.write(formatted_line)

# Usage example
input_file = "input.txt"  # Change this to your actual input file
output_file = "output.txt"  # Change this to your desired output file
format_text_file(input_file, output_file)
