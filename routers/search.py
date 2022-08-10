from curses.ascii import isdigit
from fastapi import APIRouter
from pydantic import BaseModel
from .helpers import filter_by_number, filter_by_name, filter_by_types, filter_by_weaknesses, filter_by_ability, filter_by_heights, filter_by_weights
import math

from pokemon import pokemon

class Search_Body(BaseModel):
    search: str = ""
    types: list[str] = [] 
    weaknesses: list[str] = []
    ability: str = ""
    heights: list[str] = []
    weights: list[str] = []
    minNum: int = 1
    maxNum: int = len(pokemon)

def sort_func(p):
    return p.name

router = APIRouter(prefix="/api/search")

@router.get("/")
def get_pokemon_by_number(num:int):
    return {"data": pokemon[num-1]}

@router.post("/")
def advanced_search(body: Search_Body, page: int = 1, limit: int = 12, sort: str = "01"):

    data = pokemon.copy()

    if (body.minNum > 1) | (body.maxNum < len(pokemon)):
        data = data[body.minNum - 1: body.maxNum]

    if body.search != "":
        if body.search.isdigit():
            data = filter_by_number(body.search, data)
        else:
            data = filter_by_name(body.search, data)

    if body.types != []:
        data = filter_by_types(body.types, data)

    if body.weaknesses != []:
        data = filter_by_weaknesses(body.weaknesses, data)

    if body.ability != "":
        data = filter_by_ability(body.ability, data)

    if (body.heights != []) & (len(body.heights) < 3):
        data = filter_by_heights(body.heights, data)

    if (body.weights != []) & (len(body.weights) < 3):
        data = filter_by_weights(body.weights, data)

    if sort != "01":

        if sort == "10":
            data = data[::-1]
        elif sort == "az":
            data = sorted(data, key= lambda item: item.get("name"))
        else:
            data = sorted(data, key= lambda item: item.get("name"), reverse=True)
    
    pages = math.ceil(len(data) / limit)
    starting_index = (page - 1) * limit
    data = data[starting_index: starting_index + limit]

    return {"pages": pages, "data": data}