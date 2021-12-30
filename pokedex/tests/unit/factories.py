"""
This module provides fake data for the client responses.
"""
from random import choice

from pydantic_factories import ModelFactory, Use

from pokedex.clients.models import (FlavourText, Language,
                                    PokemonClientResponse, TranslationResponse)


class FlavourTextFactory(ModelFactory):
    __model__ = FlavourText
    language = Use(choice, [Language(name="en"), Language(name="EU")])


class PokemonClientFactory(ModelFactory):
    __model__ = PokemonClientResponse
    flavor_text_entries = FlavourTextFactory.batch(size=5)


class TranslationFactory(ModelFactory):
    __model__ = TranslationResponse
