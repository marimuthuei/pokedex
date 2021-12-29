from unittest import mock

import pytest

from pokedex.application import app
from pokedex.clients import FunTranslationsClient, PokemonClient
from pokedex.clients.models import Habitat
from pokedex.exceptions import TranslationException

from .factories import PokemonClientFactory, TranslationFactory


class TestTranslations:

    @pytest.mark.asyncio
    async def test_is_legendary_return__200(self, client):
        pokemon_client_mock = mock.AsyncMock(spec=PokemonClient)
        translation_client_mock = mock.AsyncMock(spec=FunTranslationsClient)
        pokemon_response = PokemonClientFactory.build(is_legendary=True)
        translation_response = TranslationFactory.build()
        pokemon_client_mock.get_pokemon_species.return_value = pokemon_response
        translation_client_mock.get_yoda_translation.return_value = translation_response

        app.container.pokemon_client.override(pokemon_client_mock)
        app.container.fun_trans_client.override(translation_client_mock)
        response = await client.get(
            "/api/v1/pokemon/transalted/test",
        )
        assert response.status_code == 200
        assert translation_client_mock.get_yoda_translation.called

    @pytest.mark.asyncio
    async def test_habitat_cave_return__200(self, client):
        pokemon_client_mock = mock.AsyncMock(spec=PokemonClient)
        translation_client_mock = mock.AsyncMock(spec=FunTranslationsClient)
        habitat = Habitat(name="cave")
        pokemon_response = PokemonClientFactory.build(is_legendary=False, habitat=habitat)
        translation_response = TranslationFactory.build()
        pokemon_client_mock.get_pokemon_species.return_value = pokemon_response
        translation_client_mock.get_yoda_translation.return_value = translation_response

        app.container.pokemon_client.override(pokemon_client_mock)
        app.container.fun_trans_client.override(translation_client_mock)
        response = await client.get(
            "/api/v1/pokemon/transalted/test",
        )
        response_json = response.json()
        assert response.status_code == 200
        assert translation_client_mock.get_yoda_translation.called
        assert response_json["data"]['description'] == translation_response.contents.translated

    @pytest.mark.asyncio
    async def test_shakespeare_trans_return__200(self, client):
        pokemon_client_mock = mock.AsyncMock(spec=PokemonClient)
        translation_client_mock = mock.AsyncMock(spec=FunTranslationsClient)
        habitat = Habitat(name="fire")
        pokemon_response = PokemonClientFactory.build(is_legendary=False, habitat=habitat)
        translation_response = TranslationFactory.build()
        pokemon_client_mock.get_pokemon_species.return_value = pokemon_response
        translation_client_mock.get_shakespeare_translation.return_value = translation_response

        app.container.pokemon_client.override(pokemon_client_mock)
        app.container.fun_trans_client.override(translation_client_mock)
        response = await client.get(
            "/api/v1/pokemon/transalted/test",
        )
        response_json = response.json()
        assert response.status_code == 200
        assert not translation_client_mock.get_yoda_translation.called
        assert translation_client_mock.get_shakespeare_translation.called
        assert response_json["data"]['description'] == translation_response.contents.translated

    @pytest.mark.asyncio
    async def test_translation_exception__200(self, client):
        pokemon_client_mock = mock.AsyncMock(spec=PokemonClient)
        translation_client_mock = mock.AsyncMock(spec=FunTranslationsClient)
        pokemon_response = PokemonClientFactory.build(is_legendary=True)
        translation_response = TranslationFactory.build()
        pokemon_client_mock.get_pokemon_species.return_value = pokemon_response
        translation_client_mock.get_yoda_translation.side_effect = TranslationException("Exception occurred "
                                                                                        "while translating.")

        app.container.pokemon_client.override(pokemon_client_mock)
        app.container.fun_trans_client.override(translation_client_mock)
        response = await client.get(
            "/api/v1/pokemon/transalted/test",
        )
        response_json = response.json()
        assert response.status_code == 200
        assert translation_client_mock.get_yoda_translation.called
        assert response_json["data"]['description'] != translation_response.contents.translated
