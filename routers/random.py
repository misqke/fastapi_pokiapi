from fastapi import APIRouter
from pydantic import BaseModel
import random

from pokemon import pokemon

class Random_Body(BaseModel):
    pokemon: list[str] = []


router = APIRouter(prefix="/api/random")
    
@router.post("/")
def get_random_pokemon(body: Random_Body, limit: int = 12):
    new_pokemon = []
    used_pokemon = body.pokemon
    available_pokemon = []

    for p in pokemon:
        if not p["name"] in used_pokemon:
            available_pokemon.append(p)

    used_indexes = []
    while len(new_pokemon) < limit:
        random_index = random.randint(0, (len(available_pokemon) - 1))
        if random_index not in used_indexes:
            new_pokemon.append(available_pokemon[random_index])
            used_indexes.append(random_index)

    return {"data": new_pokemon}