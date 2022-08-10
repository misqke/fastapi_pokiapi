import json

with open("pokemon.json", "r", encoding="utf-8") as pokemon_json:
    pokemon = json.load(pokemon_json)