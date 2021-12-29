"""Services module."""

from pokedex.models import PokemonSummary
from pokedex.services.interfaces.ipokemon import IPokemonService


class PokemonService(IPokemonService):

    async def get_pokemon(self, name: str) -> PokemonSummary:
        pass

    async def translate(self, name: str) -> PokemonSummary:
        pass
