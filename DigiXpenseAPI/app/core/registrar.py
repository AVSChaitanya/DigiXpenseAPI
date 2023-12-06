#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from fastapi_limiter import FastAPILimiter
from fastapi_pagination import add_pagination
from starlette.middleware.authentication import AuthenticationMiddleware
#SocialAnalytics

from app.api.routers import v1
from app.common.exception.exception_handler import register_exception
# from SocialAnalytics.app.common.redis import redis_client
# from SocialAnalytics.app.common.task import scheduler
from app.core.conf import settings
from app.database.db_psql import create_table
from app.middleware.jwt_auth_middleware import JwtAuthMiddleware
# from SocialAnalytics.app.middleware.opera_log_middleware import OperaLogMiddleware
# from app.utils.demo_site import demo_site
from app.utils.health_check import ensure_unique_route_names, http_limit_callback
from app.utils.openapi import simplify_operation_ids


@asynccontextmanager
async def register_init(app: FastAPI):
    """
    Start initialization

    :return:
    """
    # Create database table
    await create_table()
    # connect redis
    await redis_client.open()
    # initialization limiter
    await FastAPILimiter.init(redis_client, prefix=settings.LIMITER_REDIS_PREFIX, http_callback=http_limit_callback)
    # Start a scheduled task
    scheduler.start()

    yield

    # Close redis connection
    await redis_client.close()
    # Close limiter
    await FastAPILimiter.close()
    # Close scheduled tasks
    scheduler.shutdown()


def register_app():
    # FastAPI
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOCS_URL,
        openapi_url=settings.OPENAPI_URL,
        lifespan=register_init,
    )

    # static files
    register_static_file(app)

    # middleware
    register_middleware(app)

    # routing
    register_router(app)

    # Pagination
    register_page(app)

    # Global exception handling
    register_exception(app)

    return app


def register_static_file(app: FastAPI):
    """
    Static file interactive development mode, production uses nginx static resource service

    :param app:
    :return:
    """
    if settings.STATIC_FILES:
        import os
        from fastapi.staticfiles import StaticFiles

        if not os.path.exists('./static'):
            os.mkdir('./static')
        SocialAnalytics.app.mount('/static', StaticFiles(directory='static'), name='static')


def register_middleware(app: FastAPI):
    """
    Middleware, execution order from bottom to top

    :param app:
    :return:
    """
    # Gzip
    if settings.MIDDLEWARE_GZIP:
        from fastapi.middleware.gzip import GZipMiddleware

        app.add_middleware(GZipMiddleware)
    # Access log
    # TODO: opera log Middleware will be removed when it is fully viable
    if settings.MIDDLEWARE_ACCESS:
        from app.middleware.access_middleware import AccessMiddleware

        app.add_middleware(AccessMiddleware)
    # Opera log
    app.add_middleware(OperaLogMiddleware)
    # JWT auth: Always open
    app.add_middleware(
        AuthenticationMiddleware, DigiXpenseAPI=JwtAuthMiddleware(), on_error=JwtAuthMiddleware.auth_exception_handler
    )
    # CORS: Always at the end
    if settings.MIDDLEWARE_CORS:
        from fastapi.middleware.cors import CORSMiddleware

        app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )


def register_router(app: FastAPI):
    """
    routing

    :param app: FastAPI
    :return:
    """
    dependencies = [Depends(demo_site)] if settings.DEMO_MODE else None

    # API
    SocialAnalytics.app.include_router(v1, dependencies=dependencies)

    # Extra
    ensure_unique_route_names(app)
    simplify_operation_ids(app)


def register_page(app: FastAPI):
    """
    Paging query

    :param app:
    :return:
    """
    add_pagination(app)
