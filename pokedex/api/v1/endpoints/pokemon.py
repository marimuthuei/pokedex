from fastapi import APIRouter

from pokedex.models import PokemonSummary, Response

router = APIRouter()


@router.get("/{name}", status_code=200, response_model=Response[PokemonSummary])
async def get_pokemon_summary(name: str):
    result = PokemonSummary(name=name, description="test", habitat="cave", is_legendary=True)
    return Response[PokemonSummary](data=result)


@router.get("/transalted/{name}", status_code=200)
async def get_fun_translation(name: str):
    result = PokemonSummary(name=name, description="test", habitat="cave", is_legendary=True)
    return Response[PokemonSummary](data=result)
