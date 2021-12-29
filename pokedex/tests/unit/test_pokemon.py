"""Tests module."""

from unittest import mock

import pytest

from pokedex.application import app
from pokedex.clients import PokemonClient
from pokedex.clients.models import Language
from pokedex.exceptions import PokemonNotFoundError

from .factories import FlavourTextFactory, PokemonClientFactory


class TestPokemon:

    @pytest.mark.asyncio
    async def test_get_valid_response__200(self, client):
        pokemon_client_mock = mock.AsyncMock(spec=PokemonClient)
        pokemon_response = PokemonClientFactory.build()
        pokemon_client_mock.get_pokemon_species.return_value = pokemon_response

        with app.container.pokemon_client.override(pokemon_client_mock):
            response = await client.get(
                "/api/v1/pokemon/test",
            )
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["data"]['name'] == pokemon_response.name

    @pytest.mark.asyncio
    async def test_pokemon_not_found__404(self, client):
        pokemon_client_mock = mock.AsyncMock(spec=PokemonClient)
        pokemon_client_mock.get_pokemon_species.side_effect = PokemonNotFoundError("Pokemon not found.")

        with app.container.pokemon_client.override(pokemon_client_mock):
            response = await client.get(
                "/api/v1/pokemon/test",
            )
        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_pokemon_without_en_flavour__200(self, client):
        pokemon_client_mock = mock.AsyncMock(spec=PokemonClient)
        flavour_texts = FlavourTextFactory.batch(language=Language(name="EU"), size=2)
        pokemon_response = PokemonClientFactory.build(flavor_text_entries=flavour_texts)
        pokemon_client_mock.get_pokemon_species.return_value = pokemon_response

        with app.container.pokemon_client.override(pokemon_client_mock):
            response = await client.get(
                "/api/v1/pokemon/test",
            )
        response_json = response.json()
        assert response.status_code == 200
        assert not response_json["data"]['description']
