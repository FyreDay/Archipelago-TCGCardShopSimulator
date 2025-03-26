import json

strings = {
    "Basic Card Pack (32)",
    "Basic Card Pack (64)",
    "Basic Card Box (4)",
    "Basic Card Box (8)",
    "Rare Card Pack (32)",
    "Rare Card Pack (64)",
    "Rare Card Box (4)",
    "Rare Card Box (8)",
    "Epic Card Pack (32)",
    "Epic Card Pack (64)",
    "Epic Card Box (4)",
    "Epic Card Box (8)",
    "Legendary Card Pack (32)",
    "Legendary Card Pack (64)",
    "Legendary Card Box (4)",
    "Legendary Card Box (8)",
    "Fire Battle Deck (18)",
    "Earth Battle Deck (18)",
    "Water Battle Deck (18)",
    "Wind Battle Deck (18)",
    "Basic Destiny Pack (32)",
    "Basic Destiny Pack (64)",
    "Basic Destiny Box (4)",
    "Basic Destiny Box (8)",
    "Rare Destiny Pack (32)",
    "Rare Destiny Pack (64)",
    "Rare Destiny Box (4)",
    "Rare Destiny Box (8)",
    "Epic Destiny Pack (32)",
    "Epic Destiny Pack (64)",
    "Epic Destiny Box (4)",
    "Epic Destiny Box (8)",
    "Legendary Destiny Pack (32)",
    "Legendary Destiny Pack (64)",
    "Legendary Destiny Box (4)",
    "Legendary Destiny Box (8)",
    "Fire Destiny Deck (18)",
    "Earth Destiny Deck (18)",
    "Water Destiny Deck (18)",
    "Wind Destiny Deck (18)",
    "Cleanser (8)",
    "Cleanser (16)",
    "Card Sleeves (Clear)",
    "Card Sleeves (Tetramon)",
    "D20 Dice Red (16)",
    "D20 Dice Blue (16)",
    "D20 Dice Black (16)",
    "D20 Dice White (16)",
    "Card Sleeves (Fire)",
    "Card Sleeves (Earth)",
    "Card Sleeves (Water)",
    "Card Sleeves (Wind)",
    "Deck Box Red (8)",
    "Deck Box Red (16)",
    "Deck Box Green (8)",
    "Deck Box Green (16)",
    "Deck Box Blue (8)",
    "Deck Box Blue (16)",
    "Deck Box Yellow (8)",
    "Deck Box Yellow (16)",
    "Collection Book (4)",
    "Premium Collection Book (4)",
    "Playmat (Drilceros)",
    "Playmat (Clamigo)",
    "Playmat (Wispo)",
    "Playmat (Lunight)",
    "Playmat (Kyrone)",
    "Playmat (Duel)",
    "Playmat (Dracunix)",
    "Playmat (The Four Dragons)",
    "Playmat (Drakon)",
    "Playmat (GigatronX Evo)",
    "Playmat (Fire)",
    "Playmat (Earth)",
    "Playmat (Water)",
    "Playmat (Wind)",
    "Playmat (Tetramon)",
    "Pigni Plushie (12)",
    "Nanomite Plushie (16)",
    "Minstar Plushie (24)",
    "Nocti Plushie (6)",
    "Burpig Figurine (12)",
    "Decimite Figurine (8)",
    "Trickstar Figurine (12)",
    "Lunight Figurine (8)",
    "Inferhog Figurine (2)",
    "Meganite Figurine (2)",
    "Princestar Figurine (2)",
    "Vampicant Figurine (2)",
    "Blazoar Plushie (2)",
    "Giganite Statue (2)",
    "Kingstar Plushie (2)",
    "Dracunix Figurine (1)",
    "Bonfiox Plushie (8)",
    "Drilceros Action Figure (4)",
    "ToonZ Plushie (6)",
    "Small Cabinet",
    "Small Metal Rack",
    "Single Sided Shelf",
    "Double Sided Shelf",
    "Wide Shelf",
    "Card Table",
    "Small Card Display",
    "Card Display Table",
    "Vintage Card Table",
    "Big Card Display",
    "Small Personal Shelf",
    "Big Personal Shelf",
    "Huge Personal Shelf",
    "Auto Scent M100",
    "Auto Scent G500",
    "Auto Scent T100",
    "Small Warehouse Shelf",
    "Big Warehouse Shelf",
    "Play Table",
    "Workbench",
    "Trash Bin",
    "Checkout Counter",
    "System Gate #1",
    "System Gate #2",
    "Mafia Works",
    "Necromonsters",
    "Claim!",
    "Penny Sleeves",
    "Tower Deckbox",
    "Magnetic Holder",
    "Toploader",
    "Card Preserver",
    "Playmat Gray",
    "Playmat Green",
    "Playmat Purple",
    "Playmat YellowPocket Pages",
    "Card Holder",
    "Collectors Album",
}

rules = {
    "locations": {s: (lambda s: lambda state: state.has(s, world.player))(s) for s in strings},
    "items": set()
}

# Save rules to a Python file for manual editing
with open("rulesOutput.py", "w") as f:
    f.write("rules = " + str({
        "locations": set(rules["locations"].keys()),
        "items": set(rules["items"])
    }))

print("Rules saved to rules.py")