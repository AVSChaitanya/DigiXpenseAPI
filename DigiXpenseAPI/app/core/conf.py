#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import lru_cache
from typing import Literal

from pydantic import BaseSettings, root_validator

class Settings(BaseSettings):
    # Env Config
    ENVIRONMENT: Literal['dev', 'pro']

    # Env PostgreSQL
    DB_HOST: str = "192.168.11.63"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "Stay@340"

    # Env Redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str
    REDIS_DATABASE: int

    # Env APScheduler Redis
    APS_REDIS_HOST: str
    APS_REDIS_PORT: int
    APS_REDIS_PASSWORD: str
    APS_REDIS_DATABASE: int

    # Env Token
    TOKEN_SECRET_KEY: str  # key secrets.token_urlsafe(32)

    # Env Opera Log
    OPERA_LOG_ENCRYPT_SECRET_KEY: str  # key os.urandom(32), Need to use bytes.hex() method converted to str

    # FastAPI
    API_V1_STR: str = '/api/v1'
    TITLE: str = 'FastAPI'
    VERSION: str = '0.0.1'
    DESCRIPTION: str = 'FastAPI Best Architecture'
    DOCS_URL: str | None = f'{API_V1_STR}/docs'
    REDOCS_URL: str | None = f'{API_V1_STR}/redocs'
    OPENAPI_URL: str | None = f'{API_V1_STR}/openapi'

    @root_validator
    def validator_api_url(cls, values):
        if values['ENVIRONMENT'] == 'pro':
            values['OPENAPI_URL'] = None
        return values

    # Demo mode
    # Only GET, OPTIONS requests are allowed
    DEMO_MODE: bool = False
    DEMO_MODE_EXCLUDE: set[tuple[str, str]] = {
        ('POST', f'{API_V1_STR}/auth/login'),
        ('POST', f'{API_V1_STR}/auth/logout'),
        ('GET', f'{API_V1_STR}/auth/captcha'),
    }

    # Uvicorn
    UVICORN_HOST: str = '127.0.0.1'
    UVICORN_PORT: int = 8000
    UVICORN_RELOAD: bool = True

    # Static Server
    STATIC_FILES: bool = False

    # Location Parse
    LOCATION_PARSE: Literal['online', 'offline', 'false'] = 'offline'

    # Limiter
    LIMITER_REDIS_PREFIX: str = 'fba_limiter'

    # DateTime
    DATETIME_TIMEZONE: str = 'Asia/Shanghai'
    DATETIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'

    # MySQL
    DB_ECHO: bool = False
    DB_DATABASE: str = 'DigiXpenseAPI-Final5'
    DB_CHARSET: str = 'UTF8'

    # Redis
    REDIS_TIMEOUT: int = 5

    # APScheduler Redis
    APS_REDIS_TIMEOUT: int = 10

    # APScheduler Default
    APS_COALESCE: bool = False  # Whether to merge and run
    APS_MAX_INSTANCES: int = 3  # Maximum number of instances
    APS_MISFIRE_GRACE_TIME: int = 60  # After the task misses the execution time, the maximum fault tolerance time will not be executed after expiration, unit: seconds

    # Token
    TOKEN_ALGORITHM: str = 'HS256'  # algorithm
    TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 1  # Expiration time, unit: seconds
    TOKEN_REFRESH_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Refresh expiration time, unit: seconds
    TOKEN_URL_SWAGGER: str = f'{API_V1_STR}/auth/swagger_login'
    TOKEN_REDIS_PREFIX: str = 'fba_token'
    TOKEN_REFRESH_REDIS_PREFIX: str = 'fba_refresh_token'
    TOKEN_EXCLUDE: list[str] = [  # whitelist
        f'{API_V1_STR}/auth/login',
    ]

    # Captcha
    CAPTCHA_LOGIN_REDIS_PREFIX: str = 'fba_login_captcha'
    CAPTCHA_LOGIN_EXPIRE_SECONDS: int = 60 * 5  # Expiration time, unit: seconds

    # Log
    LOG_STDOUT_FILENAME: str = 'fba_access.log'
    LOG_STDERR_FILENAME: str = 'fba_error.log'

    # Middleware
    MIDDLEWARE_CORS: bool = True
    MIDDLEWARE_GZIP: bool = True
    MIDDLEWARE_ACCESS: bool = False

    # Casbin
    CASBIN_RBAC_MODEL_NAME: str = 'rbac_model.conf'
    CASBIN_EXCLUDE: set[tuple[str, str]] = {
        ('POST', f'{API_V1_STR}/auth/swagger_login'),
        ('POST', f'{API_V1_STR}/auth/login'),
        ('POST', f'{API_V1_STR}/auth/logout'),
        ('POST', f'{API_V1_STR}/auth/register'),
        ('GET', f'{API_V1_STR}/auth/captcha'),
    }

    # Menu
    MENU_PERMISSION: bool = False  # Dangerous behavior, if this function is turned on, Casbin authentication will be invalid and role menu authentication will be used (off by default)
    MENU_EXCLUDE: list[str] = [
        'auth:swagger_login:post',
        'auth:login:post',
        'auth:logout:post',
        'auth:register:post',
        'auth:captcha:get',
    ]

    # Opera log
    OPERA_LOG_EXCLUDE: list[str] = [
        '/favicon.ico',
        DOCS_URL,
        REDOCS_URL,
        OPENAPI_URL,
        f'{API_V1_STR}/auth/swagger_login',
    ]
    OPERA_LOG_ENCRYPT: int = 1  # 0: AES (Performance loss); 1: md5; 2: ItsDangerous; 3: No encryption, others: Replace with ******
    OPERA_LOG_ENCRYPT_INCLUDE: list[str] = ['password', 'old_password', 'new_password', 'confirm_password']

    # ip location
    IP_LOCATION_REDIS_PREFIX: str = 'fba_ip_location'
    IP_LOCATION_EXPIRE_SECONDS: int = 60 * 60 * 24 * 1  # Expiration time, unit: seconds

    class Config:
        # https://docs.pydantic.dev/usage/settings/#dotenv-env-support
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache
def get_settings():
    """Read configuration optimization writing method"""
    return Settings()


settings = get_settings()
