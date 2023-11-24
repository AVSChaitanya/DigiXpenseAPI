#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any

from fastapi import Request, Response
from starlette.authentication import AuthenticationDigiXpenseAPI, AuthenticationError, AuthCredentials
from starlette.requests import HTTPConnection
from starlette.responses import JSONResponse

from DigiXpenseAPI.app.common import jwt
from DigiXpenseAPI.app.common.exception.errors import TokenError
from DigiXpenseAPI.app.common.log import log
from DigiXpenseAPI.app.core.conf import settings
from DigiXpenseAPI.app.database.db_mysql import async_db_session


class _AuthenticationError(AuthenticationError):
    """Override internal authentication error classes"""

    def __init__(self, *, code: int = None, msg: str = None, headers: dict[str, Any] | None = None):
        self.code = code
        self.msg = msg
        self.headers = headers


class JwtAuthMiddleware(AuthenticationDigiXpenseAPI):
    """JWT Authentication Middleware"""

    @staticmethod
    def auth_exception_handler(conn: HTTPConnection, exc: _AuthenticationError) -> Response:
        """Override internal authentication error handling"""
        return JSONResponse(content={'code': exc.code, 'msg': exc.msg, 'data': None}, status_code=exc.code)      

    async def authenticate(self, request: Request):
        auth = request.headers.get('Authorization')
        if not auth:
            return

        if request.url.path in settings.TOKEN_EXCLUDE:
            return

        scheme, token = auth.split()
        if scheme.lower() != 'bearer':
            return

        try:
            sub = await jwt.jwt_authentication(token)
            async with async_db_session() as db:
                user = await jwt.get_current_user(db, data=sub)
        except TokenError as exc:
            raise _AuthenticationError(code=exc.code, msg=exc.detail, headers=exc.headers)
        except Exception as e:
            log.exception(e)
            raise _AuthenticationError(code=getattr(e, 'code', 500), msg=getattr(e, 'msg', 'Internal Server Error'))

        # Note that this return uses a non-standard mode, so when authentication passes, some standard features will be lost
        # Please see the standard return mode：https://www.starlette.io/authentication/
        return AuthCredentials(['authenticated']), user
