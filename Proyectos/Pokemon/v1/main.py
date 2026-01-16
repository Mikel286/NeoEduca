from testing import data
from testing import pokemon
from testing import pokedex
from random import randint

if __name__ == "__main__":
    url = "config/data.txt"
    with open(url, "r", encoding = "utf-8") as file:
        pokedex = []
        for _ in range(150):
            name, type, id = data.line_decompress(line = data.data_read(file = file))
            pokemon = pokemon.Pokemon(id, name, type)
            pokedex.append(pokemon)

    pokemon = pokedex[randint(0,150)]
    print(pokemon)
    pokemon.pokemon_shout()
