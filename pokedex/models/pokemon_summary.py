from pydantic import BaseModel, Field


class PokemonSummary(BaseModel):
    name: str
    description: str = None
    habitat: str = None
    is_legendary: bool = Field(..., alias="isLegendary")

    class Config:
        allow_population_by_field_name = True
