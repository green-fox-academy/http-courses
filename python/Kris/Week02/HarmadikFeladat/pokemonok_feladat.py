from Pokemon import Pokemon

def initialize_pokemons():
    pokemon = []
    pokemon.append(Pokemon("Balbasaur", "fű", "víz"))
    pokemon.append(Pokemon("Pikatchu", "elektromos", "víz"))
    pokemon.append(Pokemon("Charizard", "tűz", "fű"))
    pokemon.append(Pokemon("Balbasaur", "víz", "tűz"))
    pokemon.append(Pokemon("Kingler", "víz", "tűz"))
    return pokemon

ash_pokemonjai = initialize_pokemons()

# Minden pokémonnak van neve és típusa.
# Bizonyos tipusok hatásosak más típusokkal szemben, pl. víz hatásos tűz ellen.

# Ash-nek van néhány pokémonja.
# Felbukkant egy vad pokémon!

vad_pokemon = Pokemon("Oddish", "fű", "víz")

# Melyik pokémonját válassza Ash a küzdelemhez?

for pokemon in ash_pokemonjai:
    if pokemon.hatasos_ellene(vad_pokemon):
        print(pokemon.nev + " téged választalak!")
    

# print("..., téged választalak!")
