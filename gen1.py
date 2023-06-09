import random

GEN1_LOOT = [
    {"pokemon": "Bulbasaur", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Ivysaur", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Venusaur", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Charmander", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Charmeleon", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Charizard", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Squirtle", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Wartortle", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Blastoise", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Caterpie", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Metapod", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Butterfree", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Weedle", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Kakuna", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Beedrill", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Pidgey", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Pidgeotto", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Pidgeot", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Rattata", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Raticate", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Spearow", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Fearow", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Ekans", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Arbok", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Pikachu", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Raichu", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Sandshrew", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Sandslash", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Nidoran♀", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Nidorina", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Nidoqueen", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Nidoran♂", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Nidorino", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Nidoking", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Clefairy", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Clefable", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Vulpix", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Ninetales", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Jigglypuff", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Wigglytuff", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Zubat", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Golbat", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Oddish", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Gloom", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Vileplume", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Paras", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Parasect", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Venonat", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Venomoth", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Diglett", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Dugtrio", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Meowth", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Persian", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Psyduck", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Golduck", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Mankey", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Primeape", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Growlithe", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Arcanine", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Poliwag", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Poliwhirl", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Poliwrath", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Abra", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Kadabra", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Alakazam", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Machop", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Machoke", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Machamp", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Bellsprout", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Weepinbell", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Victreebel", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Tentacool", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Tentacruel", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Geodude", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Graveler", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Golem", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Ponyta", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Rapidash", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Slowpoke", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Slowbro", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Magnemite", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Magneton", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Farfetch'd", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Doduo", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Dodrio", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Seel", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Dewgong", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Grimer", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Muk", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Shellder", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Cloyster", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Gastly", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Haunter", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Gengar", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Onix", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Drowzee", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Hypno", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Krabby", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Kingler", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Voltorb", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Electrode", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Exeggcute", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Exeggutor", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Cubone", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Marowak", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Hitmonlee", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Hitmonchan", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Lickitung", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Koffing", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Weezing", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Rhyhorn", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Rhydon", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Chansey", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Tangela", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Kangaskhan", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Horsea", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Seadra", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Goldeen", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Seaking", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Staryu", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Starmie", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Mr. Mime", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Scyther", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Jynx", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Electabuzz", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Magmar", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Pinsir", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Tauros", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Magikarp", "rarity": "Common", "rarity_weight": 5},
    {"pokemon": "Gyarados", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Lapras", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Ditto", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Eevee", "rarity": "Uncommon", "rarity_weight": 4},
    {"pokemon": "Vaporeon", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Jolteon", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Flareon", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Porygon", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Omanyte", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Omastar", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Kabuto", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Kabutops", "rarity": "Rare", "rarity_weight": 3},
    {"pokemon": "Aerodactyl", "rarity": "Rare", "rarity_weight": 1},
    {"pokemon": "Snorlax", "rarity": "Rare", "rarity_weight": 1},
    {"pokemon": "Articuno", "rarity": "Legendary", "rarity_weight": 1},
    {"pokemon": "Zapdos", "rarity": "Legendary", "rarity_weight": 1},
    {"pokemon": "Moltres", "rarity": "Legendary", "rarity_weight": 1},
    {"pokemon": "Dratini", "rarity": "Rare", "rarity_weight": 1},
    {"pokemon": "Dragonair", "rarity": "Rare", "rarity_weight": 1},
    {"pokemon": "Dragonite", "rarity": "Legendary", "rarity_weight": 1},
    {"pokemon": "Mewtwo", "rarity": "Legendary", "rarity_weight": 1},
    {"pokemon": "Mew", "rarity": "Legendary", "rarity_weight": 1}
]

def select_pokemon(loot_table):
    # Calculate the total weight of all rarities
    total_weight = sum(item['rarity_weight'] for item in loot_table)

    # Generate a random number between 0 and the total weight
    random_number = random.uniform(0, total_weight)

    # Iterate through the loot table and subtract the rarity weights
    # from the random number until it reaches zero or goes negative
    for item in loot_table:
        random_number -= item['rarity_weight']
        if random_number <= 0:
            return item['pokemon']
