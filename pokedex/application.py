"""
Application module - it is startup module to create the app
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pokedex.api.v1.router import api_router
from pokedex.containers import Container
from pokedex.core.config import settings
from pokedex.error_handlers import register_error_handlers


def get_application() -> FastAPI:
    container = Container()
    app = FastAPI(title=settings.project_name)
    app.container = container

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix=settings.api_v1_str)
    register_error_handlers(app)
    return app


app = get_application()

