from typing import Union

from aiohttp import ClientSession, ClientTimeout
from fastapi import status

from pokedex.exceptions import PokemonNotFoundError

from .models import PokemonClientResponse


class PokemonClient:

    def __init__(self, base_url: str, timeout: int):
        self.base_url = base_url
        self.timeout = ClientTimeout(timeout)

    async def get_pokemon_species(self, name: str) -> Union[PokemonClientResponse, None]:
        url = self.base_url + name

        async with ClientSession(timeout=self.timeout) as session:
            async with session.get(url) as response:
                if response.status == status.HTTP_404_NOT_FOUND:
                    raise PokemonNotFoundError(f"Pokemon - {name} not found.")
                # Handle other client errors and send the exact reason to the caller.
                elif response.status != status.HTTP_200_OK:
                    response.raise_for_status()
                result = await response.json()
                return PokemonClientResponse(**result)
