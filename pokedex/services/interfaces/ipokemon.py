from abc import ABC, abstractmethod

from pokedex.models import PokemonSummary


class IPokemonService(ABC):

    @abstractmethod
    async def get_pokemon(self, name: str) -> PokemonSummary:
        pass

    @abstractmethod
    async def translate(self, name: str) -> PokemonSummary:
        pass
