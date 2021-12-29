"""
This module registers custom error handlers and formats error response based on
common error format.
"""

import logging

from aiohttp.client_exceptions import ClientResponseError
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from pokedex.exceptions import (DomainException, NotFoundError,
                                TranslationException)
from pokedex.models import Response


def json_error_formatter(error, status_code):
    """
    The function formats the error type to common error response format.
    :param error: exception
    :param status_code: int
    :return: Json response
    """
    
    if issubclass(type(error), RequestValidationError):
        error_msg = error.errors()
    else:
        error_msg = str(error) or error.detail

    logging.error(error_msg)
    response = {"code": error.code or status_code, "detail": error_msg}
    error_msg = Response(error=response).dict()
    return JSONResponse(status_code=status_code, content=error_msg)


def register_error_handlers(app):
    @app.exception_handler(DomainException)
    async def handle_domain_exception(request: Request, exc: DomainException):
        mapper = [
            (NotFoundError, 404),
            (TranslationException, 400)
        ]

        for error_type, status_code in mapper:
            if issubclass(type(exc), error_type):
                return json_error_formatter(exc, status_code)

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request, exc):
        exc.code = "domain_error"
        return json_error_formatter(exc, exc.status_code)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        exc.code = "validation_error"
        return json_error_formatter(exc, status_code=400)

    @app.exception_handler(ClientResponseError)
    async def client_exception_handler(request, exc):
        exc.code = "client_error"
        return json_error_formatter(exc, exc.status)

    @app.exception_handler(Exception)
    async def client_exception_handler(request, exc):
        exc.code = "server_error"
        return json_error_formatter(exc, status_code=500)
