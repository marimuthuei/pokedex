from .common import DomainException, NotFoundError


class PokemonNotFoundError(NotFoundError):
    code = "pokemon_not_found"


class DescriptionNotFoundError(NotFoundError):
    code = "description_not_found"


class TranslationException(DomainException):
    code = "translation_exception"
