"""Services module."""

from pokedex.clients import FunTranslationsClient, PokemonClient
from pokedex.models import PokemonSummary
from pokedex.services.interfaces.ipokemon import IPokemonService


class PokemonService(IPokemonService):

    def __init__(self, poke_client: PokemonClient, fun_trans_client: FunTranslationsClient):
        self._pokemon_client = poke_client
        self._fun_trans_client = fun_trans_client

    async def get_pokemon(self, name: str) -> PokemonSummary:
        result = await self._pokemon_client.get_pokemon_species(name)

        en_flavour_texts = [entries.flavor_text for entries
                            in result.flavor_text_entries if entries.language.name == "en"]

        description = en_flavour_texts[0] if en_flavour_texts else ""

        habitat = result.habitat.name if "cave" else None

        pokemon_summary = PokemonSummary(description=description, habitat=habitat,
                                         is_legendary=result.is_legendary, name=result.name)
        return pokemon_summary

    async def translate(self, name: str) -> PokemonSummary:
        pass
