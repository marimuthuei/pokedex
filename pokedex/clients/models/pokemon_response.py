from typing import List

from pydantic import BaseModel


class Language(BaseModel):
    name: str


class Habitat(BaseModel):
    name: str


class FlavourText(BaseModel):
    flavor_text: str
    language: Language


class PokemonClientResponse(BaseModel):
    name: str
    is_legendary: bool
    habitat: Habitat = None
    flavor_text_entries: List[FlavourText]
