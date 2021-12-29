from aiohttp import ClientSession, ClientTimeout
from fastapi import status

from pokedex.models import TranslationsEnum

from .models import TranslationResponse


class FunTranslationsClient:

    def __init__(self, base_url: str, timeout: int):
        self.base_url = base_url
        self.timeout = ClientTimeout(timeout)

    async def get_yoda_translation(self, description: str) -> TranslationResponse:
        url = f"{self.base_url}{TranslationsEnum.yoda}.json?text={description}"
        response = await self.get_response(url)
        return TranslationResponse(**response)

    async def get_shakespeare_translation(self, description: str) -> TranslationResponse:
        url = f"{self.base_url}{TranslationsEnum.shakespeare}.json?text={description}"
        response = await self.get_response(url)
        return TranslationResponse(**response)

    async def get_response(self, url: str):
        async with ClientSession(timeout=self.timeout) as session:
            async with session.get(url) as response:
                if response.status != status.HTTP_200_OK:
                    response.raise_for_status()
                return await response.json()
