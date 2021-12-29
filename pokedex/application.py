"""
Application module - it is startup module to create the app
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pokedex.core.config import settings

__author__ = "Marimuthu E"


def get_application() -> FastAPI:
    app = FastAPI(title=settings.project_name)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = get_application()
