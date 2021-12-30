import logging

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from pokedex.containers import Container
from pokedex.models import PokemonSummary, Response
from pokedex.services.pokemon import PokemonService

router = APIRouter()
logger = logging.getLogger("uvicorn")


@router.get("/{name}", status_code=200, response_model=Response[PokemonSummary])
@inject
async def get_pokemon_summary(name: str, pokemon_service: PokemonService = Depends(Provide[Container.pokemon_service])):
    logger.info(f"Getting pokemon basic information for the name - {name}")
    result = await pokemon_service.get_pokemon(name)
    return Response[PokemonSummary](data=result)


@router.get("/transalted/{name}", status_code=200, response_model=Response[PokemonSummary])
@inject
async def get_fun_translation(name: str, pokemon_service: PokemonService = Depends(Provide[Container.pokemon_service])):
    logger.info(f"Translate pokemon description for the pokemon - {name}")
    result = await pokemon_service.translate(name)
    return Response[PokemonSummary](data=result)
