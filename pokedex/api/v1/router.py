from fastapi import APIRouter

from pokedex.api.v1.endpoints import pokemon

api_router = APIRouter()
api_router.include_router(pokemon.router, prefix="/pokemon", tags=["pokemon"])