"""
Dependency injector module.
"""

from dependency_injector import containers, providers

from pokedex.clients import FunTranslationsClient, PokemonClient
from pokedex.core.config import settings
from pokedex.services.pokemon import PokemonService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["pokedex.api.v1.endpoints.pokemon"])

    pokemon_client = providers.Factory(PokemonClient, base_url=settings.pokemon_url, timeout=settings.client_timeout)
    fun_trans_client = providers.Factory(FunTranslationsClient, base_url=settings.translation_url,
                                         timeout=settings.client_timeout)

    pokemon_service = providers.Factory(PokemonService, pokemon_client, fun_trans_client)
