"""
Dependency injector module.
"""

from dependency_injector import containers, providers

from pokedex.services.pokemon import PokemonService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["pokedex.api.v1.endpoints.pokemon"])

    pokemon_service = providers.Factory(PokemonService)
